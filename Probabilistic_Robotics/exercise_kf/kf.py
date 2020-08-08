#!/usr/bin/env python3.5

import numpy as np
from matplotlib import pyplot as plt


# truth y = x ** 2
def generate_data(num=100):
    x0 = np.arange(0., 1., 1./num)
    y_true = x0 * x0
    y0 = y_true + np.random.normal(0., 0.1, num)
    return x0, y0, y_true


NUM = 100
x0, y0, y_true = generate_data(NUM)
plt.plot(x0, y0)
plt.plot(x0, y_true)

# assume the prediction model is y = x, so F = 1.
# the observation model is also y = x, so H = 1.
F = 1.
H = 1.
# prediction variance: Q, observation variance: R
Q = 0.001
R = 0.1
# initial value
mu_0 = 1.
sigma_0 = 1.  # very uncertain about the initial value

mu_filtered, sigma_filtered = [], []
mu_plus = mu_0
sigma_plus = sigma_0
for i in range(NUM):
    # update prediction
    mu_minus = F * mu_plus
    sigma_minus = F * F * sigma_plus + Q
    # update observation
    k = (H * sigma_minus) / (H * H * sigma_minus + R)
    mu_plus = mu_minus + k * (y0[i] - H * mu_minus)
    sigma_plus = (1. - k * H) * sigma_minus
    # append data
    mu_filtered.append(mu_plus)
    sigma_filtered.append(sigma_plus)

plt.plot(x0, mu_filtered)
plt.legend(["data", "ground truth", "result"])
plt.show()
