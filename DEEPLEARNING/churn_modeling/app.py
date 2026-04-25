import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc

# Page configuration
st.set_page_config(page_title="Churn Prediction App", page_icon="📊", layout="wide")

# Custom CSS for better aesthetics
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    .prediction-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        margin: 20px 0;
    }
    .metric-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Cached model training + preprocessing
# ------------------------------
@st.cache_resource
def train_and_cache_model(csv_file=None):
    if csv_file is not None:
        df = pd.read_csv(csv_file)
    else:
        # Try to load from default location; if fails, show upload option
        try:
            df = pd.read_csv("e:\\11. CAPSTONE PROJECT_DEPLOYMENT\\11. CAPSTONE PROJECT_DEPLOYMENT\\CHURN MODELING- TF\\Churn_Modelling.csv")
        except FileNotFoundError:
            st.error("❌ Default dataset not found. Please upload the CSV file.")
            st.stop()

    # Prepare features and target as in notebook
    X = df.iloc[:, 3:-1].values
    y = df.iloc[:, -1].values

    # Label encode Gender (column index 2)
    le_gender = LabelEncoder()
    X[:, 2] = le_gender.fit_transform(X[:, 2])

    # One‑hot encode Geography (column index 1)
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
    X = ct.fit_transform(X)

    # Feature scaling
    sc = StandardScaler()
    X = sc.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Build ANN (exactly as in notebook)
    ann = tf.keras.models.Sequential([
        tf.keras.layers.Dense(units=6, input_dim=X_train.shape[1]),
        tf.keras.layers.Dense(units=6, activation='relu'),
        tf.keras.layers.Dense(units=6, activation='relu'),
        tf.keras.layers.Dense(units=5, activation='relu'),
        tf.keras.layers.Dense(units=4, activation='relu'),
        tf.keras.layers.Dense(units=1, activation='sigmoid')
    ])
    ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train with early stopping callback to avoid overfitting
    early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    history = ann.fit(X_train, y_train, batch_size=32, epochs=100,
                      validation_split=0.1, callbacks=[early_stop], verbose=0)

    # Predictions and metrics
    y_pred_prob = ann.predict(X_test)
    y_pred = (y_pred_prob > 0.5).astype(int)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    return ann, ct, sc, le_gender, X_test, y_test, y_pred_prob, acc, cm, report, history

# ------------------------------
# Preprocessing for a single user input
# ------------------------------
def preprocess_input(data, le_gender, ct, sc):
    # Create a numpy array of shape (1, 10) with the same column order as original X
    # Order: CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary
    input_array = np.array([[
        data['CreditScore'],
        data['Geography'],
        data['Gender'],
        data['Age'],
        data['Tenure'],
        data['Balance'],
        data['NumOfProducts'],
        data['HasCrCard'],
        data['IsActiveMember'],
        data['EstimatedSalary']
    ]], dtype=object)

    # Apply Gender label encoding
    input_array[0, 2] = le_gender.transform([input_array[0, 2]])[0]

    # Apply OneHotEncoder for Geography (column index 1)
    input_array = ct.transform(input_array)

    # Apply standardization
    input_array = sc.transform(input_array)

    return input_array

# ------------------------------
# Main App
# ------------------------------
def main():
    st.title("📈 Bank Customer Churn Prediction")
    st.markdown("Predict if a customer will **exit** the bank using a deep neural network. "
                "Enter customer details below or upload a batch file.")

    # Sidebar: file upload or use default dataset
    with st.sidebar:
        st.header("📂 Data Source")
        uploaded_file = st.file_uploader("Upload Churn_Modelling.csv", type=["csv"])
        if uploaded_file is not None:
            st.success("Using uploaded dataset")
        else:
            st.info("Using default dataset (Churn_Modelling.csv)")

        st.markdown("---")
        st.header("⚙️ Model Training")
        st.write("The model will be trained once and cached. This may take 20‑30 seconds.")

    # Train / load model
    with st.spinner("Training neural network... Please wait."):
        (model, ct, sc, le_gender,
         X_test, y_test, y_pred_prob, acc, cm, report, history) = train_and_cache_model(uploaded_file)

    # ---- MODEL PERFORMANCE SECTION ----
    st.header("🎯 Model Performance on Test Set")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📐 Accuracy", f"{acc:.2%}")
    col2.metric("🎯 Precision (Churn)", f"{report['1']['precision']:.2f}")
    col3.metric("🔄 Recall (Churn)", f"{report['1']['recall']:.2f}")
    col4.metric("🌟 F1-Score (Churn)", f"{report['1']['f1-score']:.2f}")

    # Confusion matrix heatmap
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Stayed', 'Churned'], yticklabels=['Stayed', 'Churned'])
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)

    # Training history
    with st.expander("📈 View Training History (Loss & Accuracy)"):
        fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        ax1.plot(history.history['loss'], label='Training Loss')
        ax1.plot(history.history['val_loss'], label='Validation Loss')
        ax1.set_title('Loss over Epochs')
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Loss')
        ax1.legend()

        ax2.plot(history.history['accuracy'], label='Training Accuracy')
        ax2.plot(history.history['val_accuracy'], label='Validation Accuracy')
        ax2.set_title('Accuracy over Epochs')
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Accuracy')
        ax2.legend()
        st.pyplot(fig2)

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
    roc_auc = auc(fpr, tpr)
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.plot(fpr, tpr, label=f'ANN (AUC = {roc_auc:.2f})')
    ax3.plot([0, 1], [0, 1], 'k--')
    ax3.set_xlabel('False Positive Rate')
    ax3.set_ylabel('True Positive Rate')
    ax3.set_title('ROC Curve')
    ax3.legend()
    st.pyplot(fig3)

    st.markdown("---")

    # ---- PREDICTION INTERFACE ----
    st.header("🔮 Predict Churn for a Single Customer")
    col1, col2 = st.columns(2)

    with col1:
        credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650, step=5)
        geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
        gender = st.radio("Gender", ["Female", "Male"], horizontal=True)
        age = st.slider("Age", 18, 100, 35)
        tenure = st.slider("Tenure (years with bank)", 0, 10, 5)

    with col2:
        balance = st.number_input("Account Balance (€)", min_value=0.0, max_value=300000.0, value=50000.0, step=1000.0)
        num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
        has_cr_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
        is_active_member = st.selectbox("Is Active Member?", ["Yes", "No"])
        estimated_salary = st.number_input("Estimated Salary (€)", min_value=0.0, max_value=300000.0, value=100000.0, step=1000.0)

    # Convert binary inputs to 0/1
    has_cr_card = 1 if has_cr_card == "Yes" else 0
    is_active_member = 1 if is_active_member == "Yes" else 0

    input_data = {
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active_member,
        'EstimatedSalary': estimated_salary
    }

    if st.button("🚀 Predict Churn Probability", use_container_width=True):
        # Preprocess and predict
        processed_input = preprocess_input(input_data, le_gender, ct, sc)
        prediction_proba = model.predict(processed_input)[0][0]
        prediction_class = 1 if prediction_proba > 0.5 else 0

        # Stylish output
        st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
        if prediction_class == 1:
            st.error(f"⚠️ **High Churn Risk** – Probability: {prediction_proba:.2%}")
        else:
            st.success(f"✅ **Low Churn Risk** – Probability: {prediction_proba:.2%}")
        st.markdown('</div>', unsafe_allow_html=True)

        # Show feature importance-like effects? Not possible directly, but we can show explanation.
        st.info("💡 The model uses a 5‑layer neural network. The threshold for churn is 0.5.")

    st.markdown("---")

    # ---- BATCH PREDICTION ----
    st.header("📁 Batch Prediction (Upload CSV)")
    batch_file = st.file_uploader("Upload a CSV with the same 10 input features", type=["csv"], key="batch")
    if batch_file is not None:
        batch_df = pd.read_csv(batch_file)
        # Check required columns (exact names as used in manual input)
        required_cols = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
                         'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
        if all(col in batch_df.columns for col in required_cols):
            # Transform each row
            predictions = []
            for _, row in batch_df.iterrows():
                inp = {
                    'CreditScore': row['CreditScore'],
                    'Geography': row['Geography'],
                    'Gender': row['Gender'],
                    'Age': row['Age'],
                    'Tenure': row['Tenure'],
                    'Balance': row['Balance'],
                    'NumOfProducts': row['NumOfProducts'],
                    'HasCrCard': row['HasCrCard'],
                    'IsActiveMember': row['IsActiveMember'],
                    'EstimatedSalary': row['EstimatedSalary']
                }
                proc = preprocess_input(inp, le_gender, ct, sc)
                prob = model.predict(proc, verbose=0)[0][0]
                predictions.append(prob)
            batch_df['Churn_Probability'] = predictions
            batch_df['Churn_Prediction'] = (batch_df['Churn_Probability'] > 0.5).astype(int)

            st.subheader("Batch Prediction Results")
            st.dataframe(batch_df.style.format({'Churn_Probability': '{:.2%}'}))

            # Download button
            csv_output = batch_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Predictions as CSV", data=csv_output,
                               file_name="churn_predictions.csv", mime="text/csv")
        else:
            st.error(f"CSV must contain columns: {required_cols}")

if __name__ == "__main__":
    main()