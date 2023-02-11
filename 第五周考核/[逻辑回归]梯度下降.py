from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np


class LogiReg:

    def __init__(self, tol=1e-4, C=1.0):
        self.C = 1/C
        self.tol = tol
        self.intercept_ = 0
        self.coef_ = []

    def sigmoid(self, X, theta):
        z = np.dot(X, theta)
        return 1 / (1 + np.exp(-z))

    def loss_func(self, X, Y, theta):
        Hx = self.sigmoid(X, theta)
        return -(np.dot(Y.T, np.log(Hx)) + np.dot((1 - Y).T, np.log(1 - Hx))) + self.C * np.dot(theta.T, theta) / 2, Hx

    def fit(self, X, Y, alpha):
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        Y = Y.reshape(-1, 1)
        theta = np.ones((X.shape[1], 1))
        new_loss, Hx = self.loss_func(X, Y, theta)
        while True:
            old_loss = new_loss
            gradient = np.dot(X.T, Hx - Y)
            theta[1:] = theta[1:] - alpha * gradient[1:] - self.C * theta[1:]
            theta[0] = theta[0] - alpha * gradient[0]
            new_loss, Hx = self.loss_func(X, Y, theta)
            if np.abs(old_loss - new_loss) <= self.tol:
                break
        self.coef_, self.intercept_ = theta.T[0][1:], theta[0][0]


data, target = load_breast_cancer(return_X_y=True)
MinMax = MinMaxScaler()
data = MinMax.fit_transform(data)
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3)
Alpha = 0.01
Logi = LogiReg(C=100)
Logi.fit(X_train, y_train, Alpha)
print("自己的系数：", Logi.coef_)
print("自己的截距：", Logi.intercept_)
lg = LogisticRegression(C=1, max_iter=10000)
lg.fit(X_train, y_train)
print("sklearn系数：", lg.coef_)
print("sklearn的截距：", lg.intercept_)
'''
自己的系数： [-1.68996565 -1.54461771 -1.65833756 -1.41862139 -0.6785336  -0.28703816
 -1.20781793 -1.86815073 -0.44774915  0.79217682 -1.15347494 -0.17694112
 -0.93070171 -0.74083066  0.05984187  0.49851498  0.21579325 -0.27566912
  0.32938211  0.42502471 -2.12586484 -2.26676343 -1.97683912 -1.53871128
 -1.46535716 -0.7718679  -1.24470468 -2.43519816 -1.10214263 -0.42421869]
自己的截距： 8.304687331323855
sklearn系数： [[-1.69250262 -1.54575053 -1.66055816 -1.41955616 -0.68047076 -0.28617921
  -1.20644206 -1.86636789 -0.44904646  0.79066093 -1.15282176 -0.17733811
  -0.93018832 -0.74029397  0.058992    0.49832546  0.21504262 -0.27683136
   0.32919078  0.42459568 -2.1269972  -2.26769602 -1.97773967 -1.53867832
  -1.46643419 -0.77149793 -1.24497291 -2.43512743 -1.10265907 -0.42463936]]
sklearn的截距： [8.30976597]

'''
