# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re
import joblib
import warnings
warnings.filterwarnings('ignore')

# Text preprocessing
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords', quiet=True)

# Feature extraction & ML
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Classifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from xgboost import XGBClassifier

# ------------------------------
# 1. Load and duplicate dataset
# ------------------------------
file_path = r"E:\data\data_set\Restaurant_Reviews.tsv"   # change if needed
df = pd.read_csv(file_path, delimiter='\t', quoting=3)

# Duplicate the dataset once and concatenate
df_augmented = pd.concat([df, df], ignore_index=True)
print(f"Original size: {len(df)}, Augmented size: {len(df_augmented)}")

# ------------------------------
# 2. Preprocess reviews
# ------------------------------
def preprocess_text(text):
    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Lowercase
    text = text.lower()
    # Tokenize
    words = text.split()
    # Remove stopwords and stem
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    words = [ps.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

df_augmented['cleaned_review'] = df_augmented['Review'].apply(preprocess_text)

# Features and target
X = df_augmented['cleaned_review'].values
y = df_augmented['Liked'].values

# ------------------------------
# 3. Train / test split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------
# 4. Define models and parameter grids
# ------------------------------
models = {
    'LogisticRegression': {
        'model': LogisticRegression(max_iter=1000, random_state=42),
        'params': {
            'clf__C': [0.1, 1.0, 10.0],
            'clf__solver': ['liblinear', 'lbfgs']
        }
    },
    'DecisionTree': {
        'model': DecisionTreeClassifier(random_state=42),
        'params': {
            'clf__max_depth': [10, 20, None],
            'clf__min_samples_split': [2, 5, 10]
        }
    },
    'RandomForest': {
        'model': RandomForestClassifier(random_state=42),
        'params': {
            'clf__n_estimators': [100, 200],
            'clf__max_depth': [10, 20, None],
            'clf__min_samples_split': [2, 5]
        }
    },
    'MultinomialNB': {
        'model': MultinomialNB(),
        'params': {
            'clf__alpha': [0.1, 0.5, 1.0]
        }
    },
    'SVM': {
        'model': SVC(random_state=42),
        'params': {
            'clf__C': [0.1, 1, 10],
            'clf__kernel': ['linear', 'rbf']
        }
    },
    'XGBoost': {
        'model': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
        'params': {
            'clf__n_estimators': [100, 200],
            'clf__max_depth': [3, 5],
            'clf__learning_rate': [0.01, 0.1]
        }
    }
}

# Common TF-IDF vectorizer (included in pipeline)
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2))

# Store results
results = []
best_overall_score = -1
best_overall_pipeline = None
best_overall_name = ""

# ------------------------------
# 5. Run GridSearchCV for each model
# ------------------------------
for name, mp in models.items():
    print(f"\n--- Processing {name} ---")
    # Create pipeline: TF-IDF + classifier
    pipeline = Pipeline([
        ('tfidf', tfidf),
        ('clf', mp['model'])
    ])
    
    # Grid search with 5-fold CV
    grid = GridSearchCV(
        pipeline, mp['params'], cv=5, scoring='accuracy', n_jobs=-1, verbose=1
    )
    grid.fit(X_train, y_train)
    
    # Best model from grid search
    best_model = grid.best_estimator_
    best_params = grid.best_params_
    cv_score = grid.best_score_  # mean CV accuracy
    
    # Evaluate on train and test sets
    y_train_pred = best_model.predict(X_train)
    y_test_pred = best_model.predict(X_test)
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)
    
    # Bias (train score) and Variance (test score) – simplified interpretation
    bias = train_acc
    variance = test_acc
    gap = train_acc - test_acc   # large gap indicates overfitting
    
    # Additional cross-validation scores (for reference)
    cv_scores = cross_val_score(best_model, X_train, y_train, cv=5, scoring='accuracy')
    
    # Store results
    results.append({
        'Model': name,
        'Best Params': best_params,
        'CV Mean Accuracy': cv_score,
        'Train Accuracy (bias)': bias,
        'Test Accuracy (variance)': variance,
        'Train-Test Gap': gap,
        'CV Scores (std)': f"{cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})"
    })
    
    print(f"Best CV accuracy: {cv_score:.4f}")
    print(f"Train accuracy: {train_acc:.4f}")
    print(f"Test accuracy : {test_acc:.4f}")
    print(f"Gap: {gap:.4f}")
    
    # Keep track of overall best model (based on CV accuracy)
    if cv_score > best_overall_score:
        best_overall_score = cv_score
        best_overall_pipeline = best_model
        best_overall_name = name

# ------------------------------
# 6. Display results summary
# ------------------------------
print("\n" + "="*70)
print("FINAL COMPARISON OF ALL MODELS (with GridSearchCV)")
print("="*70)
results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))

print("\n" + "="*70)
print(f"🏆 BEST MODEL: {best_overall_name}")
print(f"Best CV Accuracy: {best_overall_score:.4f}")
print("Best Pipeline:", best_overall_pipeline)

# Evaluate best model on test set one more time (already done, but for clarity)
final_test_pred = best_overall_pipeline.predict(X_test)
final_test_acc = accuracy_score(y_test, final_test_pred)
print(f"Final Test Accuracy of best model: {final_test_acc:.4f}")

# ------------------------------
# 7. Save the best model for deployment
# ------------------------------
joblib.dump(best_overall_pipeline, 'best_review_classifier.pkl')
print("\n✅ Best model saved as 'best_review_classifier.pkl'")

# ------------------------------
# 8. Example deployment usage
# ------------------------------
def predict_sentiment(review_text):
    """Load the saved pipeline and predict sentiment (1=positive, 0=negative)."""
    pipeline = joblib.load('best_review_classifier.pkl')
    cleaned = preprocess_text(review_text)
    pred = pipeline.predict([cleaned])[0]
    return "Positive" if pred == 1 else "Negative"

# Quick test
example_review = "The food was absolutely amazing!"
print(f"\nDeployment test: '{example_review}' -> {predict_sentiment(example_review)}")