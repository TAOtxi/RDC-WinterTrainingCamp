from sklearn.linear_model import Ridge
from sklearn import datasets
import numpy as np

class Grad:
    coef_ = []
    intercept_ = 0

    # 定义损失函数
    @staticmethod
    def loss_func(theta, X, Y):
        diff = np.dot(X, theta) - Y
        return (np.dot(diff.T, diff) + np.dot(theta.T, theta)) / 2

    # 梯度下降函数
    def grad_des(self, X, Y, alpha, beta):
        X = np.concatenate((np.ones((len(X), 1)), X), axis=1)
        theta = np.ones((len(X[0]), 1))
        temp_lose = Grad.loss_func(theta, X, Y)
        theta = theta - alpha * (np.dot(X.T, np.dot(X, theta) - Y) + beta * theta)
        while abs(temp_lose - (temp_lose := Grad.loss_func(theta, X, Y))) > 1e-5:
            theta = theta - alpha * (np.dot(X.T, np.dot(X, theta) - Y) + beta * theta)
        self.coef_, self.intercept_ = theta.T[0][1:], theta[0][0]

diabetes = datasets.load_diabetes()
data = diabetes.data
m = len(data)
target = diabetes.target
Alpha = 0.004
Beta = 0.001
BGD = Grad()
BGD.grad_des(data, target.reshape(m, 1), Alpha, Beta)
print("自己的系数：", BGD.coef_)
print("自己的截距：", BGD.intercept_)
print('-'*20)
ridge = Ridge(alpha=0.001).fit(data, target)
print("Ridge拟合系数", ridge.coef_)
print("Ridge截距", ridge.intercept_)
'''
自己的系数： [  -9.5514136  -239.0903527   520.36336903  323.82862566 -712.32801231
  413.38364115   65.81154253  167.51374939  720.94439563   68.12210045]
自己的截距： 152.1331399702721
--------------------
Ridge拟合系数 [  -9.55141449 -239.09035369  520.36336678  323.82862653 -712.3282053
  413.38379428   65.81162885  167.51377403  720.94446754   68.12209974]
Ridge截距 152.13348416289648
'''