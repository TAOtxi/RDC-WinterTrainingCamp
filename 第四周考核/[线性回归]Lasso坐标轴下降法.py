from sklearn import datasets
from sklearn.linear_model import Lasso
import numpy as np
import copy

class AxisDecs:
    coef_ = []
    intercept_ = 0
    @staticmethod
    def loss_func(X, Y, theta, alpha):
        diff = np.dot(X, theta) - Y
        return np.dot(diff.T, diff) / 2 + alpha * np.sum(abs(theta))

    def fit(self, X, Y, alpha):
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        theta = np.ones((X.shape[1], 1))
        loss = AxisDecs.loss_func(X, Y, theta, alpha)
        while True:
            for i in range(0, X.shape[1]):
                minus = -(np.sum((np.dot(X, theta) - Y - X[:, i].reshape(-1, 1) * theta[i][0]) * X[:, i].reshape(-1, 1)) - alpha * X.shape[0]) / np.dot(X[:, i].T, X[:, i])
                plus = -(np.sum((np.dot(X, theta) - Y - X[:, i].reshape(-1, 1) * theta[i][0]) * X[:, i].reshape(-1, 1)) + alpha * X.shape[0]) / np.dot(X[:, i].T, X[:, i])
                theta_minus = copy.deepcopy(theta)
                theta_plus = copy.deepcopy(theta)
                theta_minus[i][0] = minus
                theta_plus[i][0] = plus
                if minus < 0 < plus:
                    theta[i][0] = minus if np.dot(X, theta_minus) < np.dot(X, theta_plus) else plus
                elif minus >= 0 >= plus:
                    theta[i][0] = 0
                elif minus >= 0 and plus >= 0:
                    theta[i][0] = plus
                elif minus <= 0 and plus <= 0:
                    theta[i][0] = minus
            if abs(loss - (loss := AxisDecs.loss_func(X, Y, theta, alpha))) < 1e-5:
                break
        self.coef_, self.intercept_ = theta.T[0][1:], theta[0][0]
diabetes = datasets.load_diabetes()
data = diabetes.data
target = diabetes.target
ad = AxisDecs()
Alpha = 0.001
ad.fit(data, target.reshape(-1, 1), Alpha)
print("自己的系数：", ad.coef_)
print("自己的截距：", ad.intercept_)
ls = Lasso(alpha=Alpha)
ls.fit(data, target)
print('-'*20)
print("Lasso拟合系数", ls.coef_)
print("Lasso截距", ls.intercept_)
'''
自己的系数： [  -8.99999752 -238.9022237   520.25646338  323.43204208 -720.76349827
  421.80601444   66.96278294  164.51470634  725.52932473   67.47495893]
自己的截距： 152.13248416289647
--------------------
Lasso拟合系数 [  -8.99844942 -238.89973958  520.26136185  323.42948431 -720.25173382
  421.40514083   66.734168    164.44887295  725.34044      67.4755376 ]
Lasso截距 152.13348416289648
'''