# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:09:43 2020

@author: Gauri
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_Data.csv")
X = df.iloc[: , :1].values
Y = df.iloc[: , -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)

plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Training set(salary vs experience')
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()

plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Training set(salary vs experience')
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()