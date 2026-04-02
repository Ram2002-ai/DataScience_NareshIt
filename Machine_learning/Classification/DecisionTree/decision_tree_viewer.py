import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

# -------------------------------
# Function to create meshgrid
# -------------------------------
def draw_meshgrid(x):
    a = np.arange(start=x[:, 0].min() - 1, stop=x[:, 0].max() + 1, step=0.01)
    b = np.arange(start=x[:, 1].min() - 1, stop=x[:, 1].max() + 1, step=0.01)
    aa, bb = np.meshgrid(a, b)
    input_array = np.c_[aa.ravel(), bb.ravel()]
    return aa, bb, input_array


# -------------------------------
# Dataset
# -------------------------------
x, y = make_moons(n_samples=100, noise=0.25, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

plt.style.use('fivethirtyeight')

# -------------------------------
# Sidebar UI
# -------------------------------
st.sidebar.title('Decision Tree Classifier')

criterion = st.sidebar.selectbox('Criterion', ('gini', 'entropy'))
splitter = st.sidebar.selectbox('Splitter', ('best', 'random'))

max_depth = st.sidebar.slider('Max Depth', 0, 10, 1)
min_samples_split = st.sidebar.slider('Min Samples Split', 2, X_train.shape[0], 2)
min_samples_leaf = st.sidebar.slider('Min Samples Leaf', 1, X_train.shape[0], 1)
max_features = st.sidebar.slider('Max Features', 1, 2, 2)

max_leaf_nodes = int(st.sidebar.number_input('Max Leaf Nodes', value=0))
min_impurity_decrease = st.sidebar.number_input('Min Impurity Decrease', value=0.0)

# Handle None values
if max_depth == 0:
    max_depth = None

if max_leaf_nodes == 0:
    max_leaf_nodes = None

# -------------------------------
# Initial Plot
# -------------------------------
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x[:, 0], x[:, 1], c=y, cmap='rainbow')
ax.set_title("Original Data")
orig = st.pyplot(fig)

# -------------------------------
# Run Button
# -------------------------------
if st.sidebar.button('Run Algorithm'):

    orig.empty()

    clf = DecisionTreeClassifier(
        criterion=criterion,
        splitter=splitter,
        max_depth=max_depth,
        random_state=42,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features=max_features,
        max_leaf_nodes=max_leaf_nodes,
        min_impurity_decrease=min_impurity_decrease
    )

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # -------------------------------
    # Decision Boundary
    # -------------------------------
    XX, YY, input_array = draw_meshgrid(x)
    labels = clf.predict(input_array)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.contourf(XX, YY, labels.reshape(XX.shape), alpha=0.5, cmap='rainbow')
    ax.scatter(x[:, 0], x[:, 1], c=y, cmap='rainbow')
    ax.set_xlabel("Col1")
    ax.set_ylabel("Col2")

    st.pyplot(fig)

    # -------------------------------
    # Accuracy
    # -------------------------------
    acc = accuracy_score(y_test, y_pred)
    st.subheader(f"Accuracy for Decision Tree: {round(acc, 2)}")

    # -------------------------------
    # Tree Visualization
    # -------------------------------
    dot_data = export_graphviz(
        clf,
        feature_names=["Col1", "Col2"],
        filled=True,
        rounded=True
    )

    st.graphviz_chart(dot_data)