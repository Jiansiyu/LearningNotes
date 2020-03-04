import random
import matplotlib.pyplot as plt
from numpy.random import normal
from numpy.random import beta as beta_sample
from numpy import linspace
from scipy.stats import beta,norm
from scipy.optimize import minimize, brentq
import operator
import math

# Number of training point
m=10000

# generate the sigma and the mu for the random generator
mu_1=2.0*math.pi/3.0
sigma_1=math.sqrt(0.5)

mu_2=0.0
sigma_2=1.0


# Draw examples and assign labels
x1 = list(normal(mu_1,sigma_1,m))
y1 = [1]*m
# print(sorted(x1))
x2 = list(normal(mu_2,sigma_2,m))
y2 = [-1]*m
# print(sorted(x2))

# Combine positive and negative examples
x = x1 + x2
y = y1 + y2

#plot the examples
plt.hist([x1,x2], bins=50, color=['r','b'],density=True)


# PDF plot of N(0,1) change to nomal distribution
ls1 = linspace(norm.ppf(0.00001, mu_1,sigma_1),norm.ppf(0.99999, mu_1, sigma_1), 100)
plt.plot(ls1, norm.pdf(ls1, mu_1, sigma_1), 'r-', lw=2, alpha=0.6, label=r"$\mu={0:.2f},\sigma={1:.2f}$".format(mu_1,sigma_1))

# PDF plot of N(2pi/3,sqrt(0.5))
ls2 = linspace(norm.ppf(0.00001, mu_2,sigma_2),norm.ppf(0.99999, mu_2, sigma_2), 100)
plt.plot(ls2, norm.pdf(ls2, mu_2, sigma_2), 'r-', lw=2, alpha=0.6, label=r"$\mu={0:.2f},\sigma={1:.2f}$".format(mu_2,sigma_2))

plt.xticks(size=14)
plt.yticks(size=14)
plt.legend(fontsize=14)
# plt.savefig("fig-mix-beta.png")
plt.savefig("fig-mix-norm-samples.png")
#plt.show()


def compute_empirical_risk(x, y, b):
    """
    x - input
    y - output
    b - dividing point
    """
    error_counts = 0.0
    for (idx,val) in enumerate(x):
        if (val <= b) and (y[idx] > 0):
            error_counts += 1
        elif (val > b) and (y[idx] < 0):
            error_counts += 1
            
    return error_counts/len(x)

def find_thresh(x, y, N=400):
    """
    x - input
    y - output
    N - number of hypotheses
    """
    emp_errs, true_errs = {}, {}
    sorted_x = sorted(x)
    for idx in range(1200):
        # if idx % 200 == 0:
        #     print(idx)
        b = (1.0*idx)/N
        # Empirical error
        emp_err = compute_empirical_risk(x, y, b)
        # True error of the same hypothesis
        #true_err = 0.5*beta.cdf(b,alpha_1,beta_1) + 0.5*(1 - beta.cdf(b,alpha_2,beta_2))
        true_err =0.5*norm.cdf(b,mu_1,sigma_1)+0.5*(1-norm.cdf(b,mu_2,sigma_2))
        emp_errs[b] = emp_err
        true_errs[b] = true_err
    sorted_emp_errs = sorted(emp_errs.items(), key=operator.itemgetter(1))
    sorted_true_errs = sorted(true_errs.items(), key=operator.itemgetter(1))
    b, emp_err = sorted_emp_errs[0]
    bast, true_err = sorted_true_errs[0]
    return b, emp_err, true_errs[b], bast, true_err

def find_bayes_thresh():
    #f = lambda x : beta.pdf(x,alpha_1,beta_1) - beta.pdf(x,alpha_2,beta_2)
    f = lambda x : norm.pdf(x,mu_1,sigma_1) - norm.pdf(x,mu_2,sigma_2)
    res = brentq(f, 0, 1)
    print(res)
    return res

def compute_bayes_error(b):
    #bayes = 0.5*beta.cdf(b,alpha_1,beta_1) + 0.5*(1 - beta.cdf(b,alpha_2,beta_2))
    bayes = 0.5*norm.cdf(b,mu_1,sigma_1) + 0.5*(1 - norm.cdf(b,mu_2,sigma_2))

# learning on the sampled data
hs, hs_emp_err, hs_true_err, hast, hast_true_err = find_thresh(x, y, N=400)
print("Boundary:{}".format(hs))
print("h_S = {}\n\tEmpirical error L_S(h_S) = {}\n\tTrue error L_D(h_S) = {}\nh^ast={}\n\tTrue_error L_D(h^ast) = {}".format(hs, hs_emp_err, hs_true_err,hast, hast_true_err))
