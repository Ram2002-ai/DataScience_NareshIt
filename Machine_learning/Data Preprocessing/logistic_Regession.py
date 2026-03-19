import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"E:\data\data_set\logit classification.csv")

X=df.iloc[:,[2,3]].values
y=df.iloc[:,-1].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
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


# future prediction

df1=pd.read_csv("E:\data\data_set\Future prediction1.csv")

df1=df.iloc[:,[2,3]].values

df2=df1.copy
sc.fit_transform(df1)
X=df1.iloc[:,0].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

























