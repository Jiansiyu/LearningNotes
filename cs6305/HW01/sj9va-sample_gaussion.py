'''
Topic CS 6316 Machine Learning Homework 01 (4)
Autor: Siyu Jian (sj9va)
github: https://github.com/Jiansiyu
'''
from numpy.random import multivariate_normal as mv_normal
from sklearn.datasets import make_spd_matrix
import matplotlib.pyplot as plt

mean = [0,0]
cov = make_spd_matrix(2)
print(cov)
N = 500 # Number of samples
x1, x2 = mv_normal(mean, cov, N).T
plt.plot(x1, x2, 'o')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.savefig("sj9va_hw1.jpg")
plt.show()
