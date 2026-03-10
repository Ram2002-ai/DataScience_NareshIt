import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("E:\data\data_set\emp_sal.csv")
X=df.iloc[:,1:2].values
y=df.iloc[:,2].values


from sklearn.svm import SVR
from sklearn.metrics import r2_score
svr_reg=SVR(kernel='poly',gamma='scale',degree=5,coef0=3,epsilon=2)
svr_reg.fit(X,y)

svr_pred=svr_reg.predict([[6.5]])


from sklearn.neighbors import KNeighborsRegressor
knn=KNeighborsRegressor(n_neighbors=4,weights='distance',algorithm='ball_tree')
knn.fit(X,y)

knn_pred=knn.predict([[6.5]])

knn_score=knn.