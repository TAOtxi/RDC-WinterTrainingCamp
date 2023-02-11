from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np


class LogiReg:

    def __init__(self, tol=1e-4, C=1.0):
        self.C = 1/C
        self.tol = tol

    theta = None
    intercept_ = None
    coef_ = None

    def sigmoid(self, X):
        z = np.dot(X, self.theta)
        return 1 / (1 + np.exp(-z))

    def loss_func(self, X, Y):
        Hx = self.sigmoid(X)
        return -np.dot(Y.T, np.log(Hx)) - np.dot((1 - Y).T, np.log(1 - Hx)) + self.C * np.dot(self.theta.T, self.theta) / 2, Hx

    def fit(self, X, Y, alpha):
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        self.theta = np.ones((X.shape[1], 1))
        Y = Y.reshape(-1, 1)
        new_loss, Hx = self.loss_func(X, Y)
        while True:
            old_loss = new_loss
            gradient = np.dot(X.T, Hx - Y)
            self.theta[1:] = self.theta[1:] - alpha * gradient[1:] - self.C * self.theta[1:]
            self.theta[0] = self.theta[0] - alpha * gradient[0]
            new_loss, Hx = self.loss_func(X, Y)
            if np.abs(old_loss - new_loss) <= self.tol:
                break
        self.coef_, self.intercept_ = self.theta.T[0][1:], self.theta[0][0]

    def predict(self, X):
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        Y_pred = np.apply_along_axis(lambda x: 1 if x >= 0.5 else 0, 1, self.sigmoid(X))
        return Y_pred

    def score(self, X, Y_true):
        Y_pred = self.predict(X)
        diff = (Y_pred == Y_true)
        return np.sum(diff) / len(diff)

data, target = load_breast_cancer(return_X_y=True)
MinMax = MinMaxScaler()
data = MinMax.fit_transform(data)
X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size=0.3)
Alpha = 0.01
Logi = LogiReg(C=100)
Logi.fit(X_train, Y_train, Alpha)
print("自己的系数：", Logi.coef_)
print("自己的截距：", Logi.intercept_)
print("评估准确率:", Logi.score(X_test, Y_test))
lg = LogisticRegression(C=1, max_iter=10000)
lg.fit(X_train, Y_train)
print("sklearn系数：", lg.coef_)
print("sklearn的截距：", lg.intercept_)
print("评估准确率:", lg.score(X_test, Y_test))
'''
自己的系数： [-1.74216547 -1.45592752 -1.71985209 -1.46844326 -0.34819727 -0.43786109
 -1.35586399 -1.69831644 -0.56529711  0.95687098 -1.00833893  0.05485187
 -0.82952932 -0.68894818  0.25749566  0.41728213  0.15388719 -0.08579424
  0.23744769  0.57960888 -2.18971552 -2.05212648 -2.05022997 -1.57687565
 -1.28946803 -1.00516487 -1.58669787 -2.42184275 -1.34983532 -0.42377244]
自己的截距： 8.18716819577715
评估准确率: 0.9649122807017544
sklearn系数： [[-1.74447218 -1.45719508 -1.72188362 -1.46933177 -0.35018515 -0.43732911
  -1.35450667 -1.69694636 -0.56664822  0.95545988 -1.00783421  0.05421728
  -0.82920433 -0.68859486  0.25663281  0.41688505  0.15342338 -0.08687163
   0.23693729  0.57936631 -2.1908173  -2.05314502 -2.05118284 -1.57700361
  -1.29061547 -1.0049657  -1.58655538 -2.42209892 -1.35038734 -0.42397905]]
sklearn的截距： [8.19261556]
评估准确率: 0.9649122807017544
'''
