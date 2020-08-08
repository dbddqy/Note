# Logistic Regression

Generate training and testing date set:

```python
def generate_data(n, p=0.8):
    # p: percentage of data for training
    x1 = np.random.multivariate_normal([4., 3.], [[4., 0.], [0., 1.]], n)
    plt.scatter(x1.T[0], x1.T[1], color="red")
    x2 = np.random.multivariate_normal([6., 0.], [[1.5, 0.5], [0.5, 1.5]], n)
    plt.scatter(x2.T[0], x2.T[1], color="blue")
    # combine data
    x = np.vstack((x1, x2))
    y = np.asarray([[1., 0.]] * n + [[0., 1.]] * n)
    # shuffle data
    shuffle_idx = np.arange(0, n*2)
    np.random.shuffle(shuffle_idx)
    x_shuffled = x[shuffle_idx]
    y_shuffled = y[shuffle_idx]
    # split data into training and testing
    _x_train = x_shuffled[0:int(n * p)*2]
    _y_train = y_shuffled[0:int(n * p)*2]
    _x_test = x_shuffled[int(n * p)*2:n*2]
    _y_test = y_shuffled[int(n * p)*2:n*2]
    return _x_train, _y_train, _x_test, _y_test
```

Model of logistic regression:

```python
def model(_x, _theta):
    return 1. / (1. + exp(-_x[0] * _theta[0] - _x[1] * _theta[1] - _theta[2]))
```

Calculating the gradient vector:

```python
def gradient(_x, _y, _theta, _model):
    grad = np.array([0., 0., 0.])
    for i in range(len(_x)):
        grad[0] += (-(1. - _model(_x[i], _theta)) * _y[i][0] + _model(_x[i], _theta) * _y[i][1]) * _x[i][0]
        grad[1] += (-(1. - _model(_x[i], _theta)) * _y[i][0] + _model(_x[i], _theta) * _y[i][1]) * _x[i][1]
        grad[2] += (-(1. - _model(_x[i], _theta)) * _y[i][0] + _model(_x[i], _theta) * _y[i][1])
    return grad
```

Result:

> step: 0, theta: 0.951656 1.001376 -0.007945
> training error rate: 0.506250, testing error rate: 0.450000
> step: 100, theta: -0.314369 1.131259 -0.194332
> training error rate: 0.043750, testing error rate: 0.175000
> step: 200, theta: -0.361768 1.302411 -0.186887
> training error rate: 0.043750, testing error rate: 0.150000
> step: 300, theta: -0.395465 1.433055 -0.181936
> training error rate: 0.043750, testing error rate: 0.150000
> step: 400, theta: -0.422276 1.538629 -0.178686
> training error rate: 0.043750, testing error rate: 0.150000
> step: 500, theta: -0.444488 1.627198 -0.176557
> training error rate: 0.050000, testing error rate: 0.150000
> step: 600, theta: -0.463398 1.703425 -0.175217
> training error rate: 0.050000, testing error rate: 0.150000
> step: 700, theta: -0.479820 1.770257 -0.174460
> training error rate: 0.050000, testing error rate: 0.150000
> step: 800, theta: -0.494296 1.829684 -0.174151
> training error rate: 0.050000, testing error rate: 0.150000
> step: 900, theta: -0.507206 1.883114 -0.174194
> training error rate: 0.050000, testing error rate: 0.150000

![](result.png)