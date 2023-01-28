from sklearn import datasets
import numpy as np

# 定义损失函数
def loss_func(theta, X, Y):
    diff = np.dot(X, theta) - Y
    return np.sum((1/(2*m))*np.dot(diff.T, diff))

# 梯度下降函数
def grad_des(theta, X, Y, alpha):
    temp_lose = loss_func(theta, X, Y)
    temp_theta = theta.copy()
    theta = theta - alpha * np.sum(np.dot(X, temp_theta) - Y, axis=0) * temp_theta / m
    while abs(temp_lose - (temp_lose := loss_func(theta, X, Y))) > 1e-5:
        temp_theta = theta.copy()
        theta = theta - alpha * np.sum(np.dot(X, temp_theta) - Y, axis=0) * temp_theta / m
    return theta

diabetes = datasets.load_diabetes()
m = int(len(diabetes.data) * 0.7)
data = diabetes.data[:m]
data = np.concatenate((np.ones((len(data), 1)), data), axis=1)
target = diabetes.target[:m]
Alpha = 0.01
Theta = np.ones((len(data[0]), 1))
Theta = grad_des(Theta, data, target.reshape(m, 1), Alpha)
print(Theta)
