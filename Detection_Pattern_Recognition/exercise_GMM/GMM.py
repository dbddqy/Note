# 文件功能：实现 GMM 算法

import numpy as np
# from numpy import *
import pylab
import random, math

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy.stats import multivariate_normal
plt.style.use('seaborn')


class GMM(object):
    def __init__(self, n_clusters, tolerance=1e-5, max_iter=50):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tolenrance_ = tolerance
        self.gamma = None # probability of n-th point belongs to k-th group [N, K]
        self.mu = None # mean [K, dim(data)]
        self.sigma = None # covariance matrix [K, dim(data), dim(data)]
        self.pi = None # weight [K, ]
    # 屏蔽开始

    # 更新W
    def update_gamma(self, data):
        for k in range(self.n_clusters):
            self.gamma[:, k] = self.pi[k] * multivariate_normal.pdf(data, mean=self.mu[k], cov=self.sigma[k])
        temp = np.sum(self.gamma, axis=1, keepdims=True)
        self.gamma = self.gamma / temp

    # 更新pi
    def update_pi(self, N):
        for i in range(self.n_clusters):
            self.pi[i] = np.sum(self.gamma[:, i]) / N

    # 更新Mu
    def update_mu(self, data):
        self.mu = self.gamma.T.dot(data) / (self.pi.reshape([self.n_clusters, 1]) * data.shape[0])

    # 更新Var
    def update_sigma(self, data):
        for i in range(self.n_clusters):
            temp_sigma = np.zeros([data.shape[1], data.shape[1]])
            for n in range(data.shape[0]):
                temp_sigma += self.gamma[n, i] * (data[n:n+1, :]-self.mu[i:i+1, :]).T.dot(data[n:n+1, :]-self.mu[i:i+1, :])
            self.sigma[i] = temp_sigma / (self.pi[i] * data.shape[0])

    # 屏蔽结束
    
    def fit(self, data):
        # 作业3
        # 屏蔽开始
        # init
        N = data.shape[0]
        self.gamma = np.ones([N, self.n_clusters]) / self.n_clusters
        self.mu = data[0:self.n_clusters, :]
        self.sigma = np.zeros([self.n_clusters, data.shape[1], data.shape[1]])
        for i in range(self.n_clusters):
            self.sigma[i] = np.identity(data.shape[1])
        self.pi = np.ones([self.n_clusters, ]) / self.n_clusters
        # optimize
        for _ in range(self.max_iter):
            self.update_gamma(data)
            self.update_pi(N)
            mu_old = self.mu
            self.update_mu(data)
            self.update_sigma(data)
            if np.linalg.norm(mu_old-self.mu) < self.tolenrance_:
                break
        # 屏蔽结束
    
    def predict(self, data):
        # 屏蔽开始
        result = []
        for n in range(data.shape[0]):
            max_index = 0
            max_likelihood = self.pi[max_index] * multivariate_normal.pdf(data[n], mean=self.mu[max_index],
                                                                          cov=self.sigma[max_index])
            for k in range (1, self.n_clusters):
                if max_likelihood < self.pi[k] * multivariate_normal.pdf(data[n], mean=self.mu[k], cov=self.sigma[k]):
                    max_index = k
                    max_likelihood = self.pi[max_index] * multivariate_normal.pdf(data[n], mean=self.mu[max_index],
                                                                              cov=self.sigma[max_index])
            result.append(max_index)
        return result
        # 屏蔽结束

# 生成仿真数据
def generate_X(true_Mu, true_Var):
    # 第一簇的数据
    num1, mu1, var1 = 400, true_Mu[0], true_Var[0]
    X1 = np.random.multivariate_normal(mu1, np.diag(var1), num1)
    # 第二簇的数据
    num2, mu2, var2 = 600, true_Mu[1], true_Var[1]
    X2 = np.random.multivariate_normal(mu2, np.diag(var2), num2)
    # 第三簇的数据
    num3, mu3, var3 = 1000, true_Mu[2], true_Var[2]
    X3 = np.random.multivariate_normal(mu3, np.diag(var3), num3)
    # 合并在一起
    X = np.vstack((X1, X2, X3))
    # 显示数据
    plt.figure(figsize=(10, 8))
    plt.axis([-10, 15, -5, 15])
    plt.scatter(X1[:, 0], X1[:, 1], s=5)
    plt.scatter(X2[:, 0], X2[:, 1], s=5)
    plt.scatter(X3[:, 0], X3[:, 1], s=5)
    plt.show()
    return X

if __name__ == '__main__':
    # 生成数据
    true_Mu = [[0.5, 0.5], [5.5, 2.5], [1, 7]]
    true_Var = [[1, 3], [2, 2], [6, 2]]
    X = generate_X(true_Mu, true_Var)

    gmm = GMM(n_clusters=3)
    gmm.fit(X)
    cat = gmm.predict(X)
    print(cat)

    color_list = ["blue", "green", "red"]
    colors = [color_list[cat_index] for cat_index in cat]
    plt.figure(figsize=(10, 8))
    plt.axis([-10, 15, -5, 15])
    plt.scatter(X[:, 0], X[:, 1], c=colors, s=5)
    plt.show()

    

