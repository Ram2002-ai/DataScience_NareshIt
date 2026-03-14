import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("E:\logit classification.csv")

X=df.iloc[:,[2,3]].values
y=df.iloc[:,-1].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=100)




from sklearn.linear_model import LogisticRegression

lr=LogisticRegression(penalty='l1',solver='liblinear')
lr.fit(X_train, y_train)



y_pred=lr.predict(X_test)


from sklearn.metrics import confusion_matrix

cm=confusion_matrix(y_test, y_pred)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test, y_pred)

from sklearn.metrics import classification_report

cr=classification_report(y_test, y_pred)


bias=lr.score(X_train,y_train)

variance=lr.score(X_test, y_test)



























