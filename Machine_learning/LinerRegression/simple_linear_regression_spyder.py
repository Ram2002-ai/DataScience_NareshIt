#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"E:\data\data_set\Salary_Data.csv")

x = dataset.iloc[:,:-1]
y = dataset.iloc[:, -1] 


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) 

y_pred = regressor.predict(x_test)

comparision = pd.DataFrame({'Actual': y_test, 'Prediction': y_pred})
print(comparision) 


plt.scatter(x_test, y_test, color = 'Red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary of employee based on experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show() 


# predict future 

m_coef = regressor.coef_
print(m_coef)

c_intercept = regressor.intercept_
print(c_intercept)

y_20 = m_coef * 20 + c_intercept
print(y_20)


bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance) 


from scipy.stats import variation

variation(dataset.values)

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])
dataset['Salary'].corr(dataset['Salary'])
dataset['YearsExperience'].corr(dataset['Salary'])
dataset['YearsExperience'].corr(dataset['YearsExperience'])


dataset.skew()

# standard error


import scipy.stats as stats
dataset.apply(stats.zscore)

# ssr
import numpy as np
y_mean=np.mean(y)
ssr=np.sum((y_pred-y_mean)**2)
print(ssr)

# sse
y=y[0:6]
sse=np.sum((y-y_pred)**2)
print(sse)


# sst
mean_total=np.mean(dataset.values)
sst=np.sum((dataset.values-mean_total)**2)
print(sst)

# r2
r_square=1-ssr/sst
print(r_square)

m_coef*2+c_intercept

# pickle
import pickle

filename='linear_regressor_model.pkl'
with open(filename,'wb') as file:
    pickle.dump(regressor,file) 
print('model has been pickeled and saved as linear_regressor_model.pkl',filename)
