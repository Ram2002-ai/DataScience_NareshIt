import numpy as np
import pandas as pd

df=pd.read_csv(r"E:\data\data_set\mlfirst1.csv")
df


X=df.iloc[:,-1].values
y=df.iloc[:,3].values

# missing value imputation
from sklearn.impute import SimpleImputer


imputer=SimpleImputer(strategy='median')

imputer=imputer.fit(X[1:3])
x[:,1:3]=imputer.transform(X[:,1:3])

from sklearn.preprocessing import LabelEncoder

labelEncoder_x=LabelEncoder()

# labelEncoder_x.fit_transform(X[:,0])

x[:,0]=labelEncoder_x.fit_transform(X[:,0])

labelEncoder_y=LabelEncoder()
y=labelEncoder_y.fit_transform(y)

from sklearn.model_selection import train_test_split

# X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.7,random_state=42)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)



# feature scalling
















