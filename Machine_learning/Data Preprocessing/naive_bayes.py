import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("E:\data\data_set\logit classification.csv")

X=df.iloc[:,[2,3]].values
y=df.iloc[:,-1].values


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

sc=StandardScaler()

X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

BN=BernoulliNB()

BN.fit(X_train,y_train)

y_pred=BN.predict(X_test)


accuracy=accuracy_score(y_test, y_pred)

from sklearn.naive_bayes import GaussianNB

gn=GaussianNB()
gn.fit(X_train,y_train)

gn_pred=gn.predict(X_test)
gn_accuracy=accuracy_score(y_test, gn_pred)

from sklearn.naive_bayes import MultinomialNB

gn=MultinomialNB()
gn.fit(X_train,y_train)
mn_pred=gn.predict(X_test)
mn_accuracy=accuracy_score(y_test, mn_pred)

