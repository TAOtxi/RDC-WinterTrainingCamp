from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
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
            gradient = np.dot(X.T, (Hx - Y)) + self.C * theta
            theta = theta - alpha * gradient
            new_loss, Hx = self.loss_func(X, Y, theta)
            if np.abs(old_loss - new_loss) < self.tol:
                break
        self.coef_, self.intercept_ = theta.T[0][1:], theta[0][0]


data, target = load_breast_cancer(return_X_y=True)
MinMax = MinMaxScaler()
data = MinMax.fit_transform(data)
Alpha = 0.08
Logi = LogiReg(C=1000)
Logi.fit(data, target, Alpha)
print("自己的系数：", Logi.coef_)
print("自己的截距：", Logi.intercept_)
lg = LogisticRegression(C=1000, max_iter=10000)
lg.fit(data, target)
print("sklearn系数：", lg.coef_)
print("sklearn的截距：", lg.intercept_)
'''
自己的系数： [  5.92558021   0.54299262   5.86943542  -0.69255307  -2.01973081
  15.80942231  -8.58706681 -14.55350294   3.48866207   0.22401657
 -26.73851114   5.89512604 -12.82059101 -17.58909549  -5.3846213
   6.12742599   6.21098646  -4.5698809    3.57774081  11.64347318
 -17.85642678 -16.59878288 -11.02334938 -18.7494114   -4.18976916
   1.78280396  -7.85527731  -7.45383861 -12.30683538  -8.68464202]
自己的截距： 27.121661540979773
sklearn系数： [[ 10.64713386   0.53368336   9.34884602   2.57646577  -4.79190463
   22.51835097 -13.36678792 -15.50968242   2.47997528  -2.13443468
  -27.68460401   6.94440344  -1.28740596 -23.37537453  -6.20132794
   -1.45577365  17.37335643 -14.62667779   4.55735868  28.66638553
  -24.27665668 -17.31834974 -14.03364935 -28.21649484  -1.83884119
    3.54700919  -9.00028957  -3.19415196 -11.61879133 -16.12910528]]
sklearn的截距： [28.23862808]
'''
