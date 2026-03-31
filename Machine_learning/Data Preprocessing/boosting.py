import numpy as np
import pandas as pd

df=pd.read_csv("E:\data\data_set\Churn_Modelling.csv")

print(df.isnull().sum())

X=df.iloc[:,3:-1].values
y=df.iloc[:,-1].values



from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X[:,2]=le.fit_transform(X[:,2])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')
X=np.array(ct.fit_transform(X))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


from xgboost import XGBClassifier
xg=XGBClassifier(random_state=0)

xg.fit(X_train,y_train)

y_pred=xg.predict(X_test)

from sklearn.metrics import accuracy_score

ac=accuracy_score(y_test, y_pred)

bias=xg.score(X_train, y_train)
variance=xg.score(X_test,y_test)


# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = xg, X = X_train, y = y_train, cv = 100)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
#print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


from lightgbm import LGBMClassifier

lgbm=LGBMClassifier()
lgbm.fit(X_train,y_train)

l_pred=lgbm.predict(X_test)

l_accuracy=accuracy_score(y_test, y_pred)



l_accuracies = cross_val_score(estimator = lgbm, X = X_train, y = y_train, cv = 100)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
#print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()

rf.fit(X_train,y_train)

r_pred=rf.predict(X_test)

r_accuracy=accuracy_score(y_test, y_pred)

param_grid=({
    
    'max_depth':[1,2,3,4,5,6,7,,8,9,10]
    
    
    })





