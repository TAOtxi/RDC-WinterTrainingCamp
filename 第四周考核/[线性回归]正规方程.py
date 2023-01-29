from sklearn.linear_model import LinearRegression
from sklearn import datasets
import numpy as np

class NorEqu:
    coef_ = []
    intercept_ = 0

    def func(self, X, Y):
        X = np.concatenate((np.ones((len(X), 1)), data), axis=1)
        theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), Y)
        self.coef_, self.intercept_ = theta.T[0][1:], theta[0][0]

diabetes = datasets.load_diabetes()
data = diabetes.data
target = diabetes.target
normal = NorEqu()
normal.func(data, target.reshape(len(data), 1))
print("自己的系数：", normal.coef_)
print("自己的截距：", normal.intercept_)
print('-'*20)
lr = LinearRegression()
lr.fit(data, target)
print("sklearn拟合系数", lr.coef_)
print("sklearn截距", lr.intercept_)
'''
>>>自己的系数： [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163
                476.74583782  101.04457032  177.06417623  751.27932109   67.62538639]
>>>自己的截距： 152.1334841628965
--------------------
>>>sklearn拟合系数 [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163
                    476.74583782  101.04457032  177.06417623  751.27932109   67.62538639]
>>>sklearn截距 152.1334841628965
'''