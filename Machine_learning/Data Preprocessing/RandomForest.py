import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("E:\data\data_set\Social_Network_Ads.csv")

X=df.iloc[:,[2,3]].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Tree baesd algorithm doesn't required feature scaling

from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier(n_estimators=500,max_depth=3)

rf.fit(X_train,y_train)

y_pred=rf.predict(X_test)

from sklearn.metrics import accuracy_score,confusion_matrix

ac=accuracy_score(y_test, y_pred)

cm=confusion_matrix(y_test, y_pred)

bias=rf.score(X_train,y_train)
variance=rf.score(X_test,y_test)


from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train

x1_range = np.linspace(X_set[:,0].min()-1, X_set[:,0].max()+1, 500)
x2_range = np.linspace(X_set[:,1].min()-1, X_set[:,1].max()+1, 500)

X1, X2 = np.meshgrid(x1_range, x2_range)

Z = rf.predict(np.array([X1.ravel(), X2.ravel()]).T)
Z = Z.reshape(X1.shape)

plt.contourf(X1, X2, Z, alpha=0.75, cmap=ListedColormap(('red', 'green')))

colors = ['red', 'green']
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0],
                X_set[y_set == j, 1],
                c=colors[i], label=j)

plt.title('Random Forest Classification (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

s

























