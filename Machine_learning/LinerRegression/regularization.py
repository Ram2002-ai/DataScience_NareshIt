import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score


df=pd.read_csv(r"E:\data\data_set\car-mpg.csv")

df = df.

df['origin']=df['origin'].replace({1:'america',2:'europe',3:'asia'})

df=pd.get_dummies(df,columns=['origin'],dtype=int)

df=df.replace('?',np.nan)

df=df.apply(pd.to_numeric,errors='ignore')
df=df.apply(lambda x:x.fillna(x.median()) if x.dtype !='object' else x)


X = df.drop(['mpg'],axis=1) # 
y = df[['mpg']]

#Scaling the data
X_s = preprocessing.scale(X)
X_s = pd.DataFrame(X_s, columns = X.columns)

y_s = preprocessing.scale(y)
y_s = pd.DataFrame(y_s,columns = y.columns)

X_train, X_test, y_train, y_test = train_test_split(X_s, y_s, test_size=0.20, random_state=0)



reg=LinearRegression()
reg.fit(X_train,y_train)
reg_coef=reg.coef_




ridge=Ridge(alpha=0.4)
ridge.fit(X_train,y_train)
ridge_coef=ridge.coef_

Lasso=Lasso()
Lasso.fit(X_train,y_train)

lasso_coef=Lasso.coef_






























