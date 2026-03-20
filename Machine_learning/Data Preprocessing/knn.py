# KNN CLASSIFICATION

# distance metrix 1. Ecludian distance 2. manhatian distaince

# imbalance data : two class 1. majority class 2. minority class

"""
 how to handle imbalanced 
 
 
 99%             1%
 
 undersample     oversample
 70 %            30%
 75%             25%
 80%             20%

then take average of all 

- SMOTHE for imbalance data

synthetic minority oversampling technique


outlier impact impact knn model

logistic & naive bayes -- does not impact outlier because of probability



  
 

"""


import pandas as pd
import numpy as np

df1=pd.read_csv("E:\data\data_set\Future prediction1.csv")

X=df1.iloc[:,[2,3]].values
y=df1.iloc[:,-1].values




from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier()

knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)


from sklearn.metrics import accuracy_score,confusion_matrix

accuracy=accuracy_score(y_test, y_pred)
































