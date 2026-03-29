import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df=pd.read_csv('E:\data\data_set\logit classification.csv')

X=df.iloc[:,[2,3]].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier(criterion='entropy',max_depth=10,random_state=0,class_weight={0: 1, 1: 1})

dt.fit(X_train,y_train)

y_pred=dt.predict(X_test)

from sklearn.metrics import accuracy_score,confusion_matrix

ac=accuracy_score(y_test, y_pred)
confusion=confusion_matrix(y_test, y_pred)

