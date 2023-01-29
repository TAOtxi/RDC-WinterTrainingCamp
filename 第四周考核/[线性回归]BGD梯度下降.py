from sklearn.linear_model import LinearRegression
from sklearn import datasets
import numpy as np

# 定义损失函数
def loss_func(theta, X, Y):
    diff = np.dot(X, theta) - Y
    return np.dot(diff.T, diff) / 2

# 梯度下降函数
def grad_des(theta, X, Y, alpha):
    temp_lose = loss_func(theta, X, Y)
    temp_theta = theta.copy()
    theta = theta - alpha * np.dot(X.T, np.dot(X, temp_theta) - Y)
    while abs(temp_lose - (temp_lose := loss_func(theta, X, Y))) > 1e-5:
        temp_theta = theta.copy()
        theta = theta - alpha * np.dot(X.T, np.dot(X, temp_theta) - Y)
    return theta

diabetes = datasets.load_diabetes()
data = diabetes.data
m = len(data)
data_ = np.concatenate((np.ones((len(data), 1)), data), axis=1)
target = diabetes.target
Alpha = 1.9 / m
Theta = np.ones((len(data_[0]), 1))
Theta = grad_des(Theta, data_, target.reshape(m, 1), Alpha)
print("自己的系数：", Theta.T[0][1:])
print("自己的截距：", Theta[0][0])
print('-'*20)
lr = LinearRegression()
lr.fit(data, target)
print("sklearn拟合系数", lr.coef_)
print("sklearn截距", lr.intercept_)
'''
>>>自己的系数： [  -9.99381385 -239.79846532  519.88625585  324.37228024 -788.18534877
                473.57283614   99.2561154   176.55377325  749.78933312   67.64009601]
>>>自己的截距： 152.13348416289645
--------------------
>>>sklearn拟合系数 [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163
                    476.74583782  101.04457032  177.06417623  751.27932109   67.62538639]
>>>sklearn截距  152.1334841628965
'''