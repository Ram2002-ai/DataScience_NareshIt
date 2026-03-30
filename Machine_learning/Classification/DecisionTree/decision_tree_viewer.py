import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from os import system
from graphviz import Source
from sklearn.tree import export_graphviz
import graphviz

def draw_meshgrid():
    a=np.arange(start=x[:,0].min()-1, stop=x[:,0].max()+1, step=0.01)
    b=np.arange(start=x[:,1].min()-1, stop=x[:,1].max()+1, step=0.01)
    aa,bb=np.meshgrid(a,b)
    input_array=np.c_[aa.ravel(),bb.ravel()]

    return aa,bb ,input_array

x,y=make_moons(n_samples=100,noise=0.25,random_state=0)
X_train,X_test,y_train,y_test=train_test_split(x,y,random_state=0)

plt.style.use('fivethirtyeight')
st.sidebar.title('Decision Tree Classifier')
criterion=st.sidebar.selectbox('Criterion',('gini','entropy'))
splitter=st.sidebar.selectbox('Splitter',('best','random'))
max_depth=st.sidebar.slider('Max Depth' ,1,10,1,key=123)
min_samples_split=st.sidebar.slider('Min Samples Split',1,x_train.shape[0],1,key=1234)
min_samples_leaf = st.sidebar.slider('Min Samples Leaf', 1, X_train.shape[0], 1,key=1235)

max_features = st.sidebar.slider('Max Features', 1, 2, 2,key=1236)

max_leaf_nodes = int(st.sidebar.number_input('Max Leaf Nodes'))

min_impurity_decrease = st.sidebar.number_input('Min Impurity Decrease')

# load intial graph
fig,ax=plt.subplots(figsize=(10,6))
ax.scatter(X.T[0], X.T[1], c=y, cmap='rainbow')
orig = st.pyplot(fig)

if st.sidebar.button('Run Algorithm'):

    orig.empty()

    if max_depth == 0:
        max_depth = None

    if max_leaf_nodes == 0:
        max_leaf_nodes = None

    clf = DecisionTreeClassifier(criterion=criterion,splitter=splitter,max_depth=max_depth,random_state=42,min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf,max_features=max_features,max_leaf_nodes=max_leaf_nodes,min_impurity_decrease=min_impurity_decrease)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    XX, YY, input_array = draw_meshgrid()
    labels = clf.predict(input_array)

    ax.contourf(XX, YY, labels.reshape(XX.shape), alpha=0.5, cmap='rainbow')
    plt.xlabel("Col1")
    plt.ylabel("Col2")
    orig = st.pyplot(fig)
    st.subheader("Accuracy for Decision Tree  " + str(round(accuracy_score(y_test, y_pred), 2)))

    tree = export_graphviz(clf,feature_names=["Col1","Col2"])

    st.graphviz_chart(tree)