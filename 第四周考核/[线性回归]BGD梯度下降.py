from sklearn.linear_model import Ridge
from sklearn import datasets
import numpy as np

class Grad:
    coef_ = []
    intercept_ = 0

    # 定义损失函数
    @staticmethod
    def loss_func(theta, X, Y, beta):
        diff = np.dot(X, theta) - Y
        return (np.dot(diff.T, diff) + beta * np.dot(theta.T, theta)) / 2

    # 梯度下降函数
    def grad_des(self, X, Y, alpha, beta):
        X = np.concatenate((np.ones((len(X), 1)), X), axis=1)
        theta = np.ones((len(X[0]), 1))
        temp_lose = Grad.loss_func(theta, X, Y, beta)
        theta = theta - alpha * (np.dot(X.T, np.dot(X, theta) - Y) + beta * theta)
        while abs(temp_lose - (temp_lose := Grad.loss_func(theta, X, Y, beta))) > 1e-5:
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
ridge = Ridge(alpha=Beta).fit(data, target)
print("Ridge拟合系数", ridge.coef_)
print("Ridge截距", ridge.intercept_)
'''
自己的系数： [  -9.53434987 -239.07120975  520.40650094  323.81178145 -708.61637146
  410.43850641   64.15152428  167.04000065  719.56141013   68.13575371]
自己的截距： 152.1331399702721
--------------------
Ridge拟合系数 [  -9.55141449 -239.09035369  520.36336678  323.82862653 -712.3282053
  413.38379428   65.81162885  167.51377403  720.94446754   68.12209974]
Ridge截距 152.13348416289648
'''