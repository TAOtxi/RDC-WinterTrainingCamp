from sklearn.linear_model import Ridge
from sklearn import datasets
import numpy as np

class NorEqu:
    coef_ = []
    intercept_ = 0

    def func(self, X, Y, alpha):
        X = np.concatenate((np.ones((len(X), 1)), data), axis=1)
        theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + alpha * np.eye(len(X[0]))), X.T), Y)
        self.coef_, self.intercept_ = theta.T[0][1:], theta[0][0]

diabetes = datasets.load_diabetes()
data = diabetes.data
target = diabetes.target
Alpha = 0.001
normal = NorEqu()
normal.func(data, target.reshape(len(data), 1), Alpha)
print("自己的系数：", normal.coef_)
print("自己的截距：", normal.intercept_)
print('-'*20)
ridge = Ridge(alpha=Alpha).fit(data, target)
print("Ridge拟合系数", ridge.coef_)
print("Ridge截距", ridge.intercept_)
'''
自己的系数： [  -9.55141449 -239.09035369  520.36336678  323.82862653 -712.3282053
  413.38379428   65.81162885  167.51377403  720.94446754   68.12209974]
自己的截距： 152.13313997027214
--------------------
Ridge拟合系数 [  -9.55141449 -239.09035369  520.36336678  323.82862653 -712.3282053
  413.38379428   65.81162885  167.51377403  720.94446754   68.12209974]
Ridge截距 152.13348416289648
'''