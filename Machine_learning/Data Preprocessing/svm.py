import pandas as pd
import numpy as np




df1=pd.read_csv("E:\data\data_set\Future prediction1.csv")

df1=df1.iloc[:,[2,3]].values

df2=df1.copy

X=df1[:,0]
y=df1[:,1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
sc.fit_transform(X_train)
