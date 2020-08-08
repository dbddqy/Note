# Soft margin SVM

Data generation:

```python
def generate_data(n, p=1.0):
    # p: percentage of data for training
    x1 = np.random.multivariate_normal([4., 3.], [[.4, 0.], [0., .1]], int(1.0*n))  # simple case
    plt.scatter(x1.T[0], x1.T[1], color="red")
    x2 = np.random.multivariate_normal([6., 0.], [[1.5, .5], [.5, 1.5]], int(1.0*n))
    plt.scatter(x2.T[0], x2.T[1], color="blue")
    # combine data
    x = np.vstack((x1, x2))
    y = np.asarray([[1.]] * n + [[-1.]] * n)
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

RBF kernel:

```python
def kernel_RBF(x1, x2, _gamma):
    return np.exp(-_gamma * np.sum((x1 - x2) * (x1 - x2)))
```

Get the matrix for quadratic programming (applying the kernel trick):

```python
def get_P_Mat(x, y, n, kernel, _gamma):
    _P = np.zeros([n, n], dtype=np.float)
    for i in range(n):
        for j in range(n):
            _P[i][j] = y[i][0] * y[j][0] * kernel(x[i].T, x[j].T, _gamma)
    return _P
```

Solve the quadratic programming with cvxopt:

```python
# optimizaton
P = matrix(P_Mat)
q = matrix(-np.ones([n*2, 1]))
# 2*n inequality constraints
G = matrix(np.vstack([-np.eye(n*2), np.eye(n*2)]))
h = matrix(np.vstack([np.zeros([n*2, 1]), C*np.ones([n*2, 1])]))
# 1 equality constraint
A = matrix(y_train.T)
b = matrix(0.)

sol = solvers.qp(P, q, G, h, A, b)
alpha = np.array(sol['x'])
```

Select indices of SVs (support vectors) and SOs (support vector and outliers):

```python
SV, SO = [], []
for i in range(n*2):
    if alpha[i][0] < 0.001:
        continue
    if abs(alpha[i][0]-C) > 0.001:
        SV.append(i)
    SO.append(i)
```

Calculate the offset w0:

```python
w0 = 0.
for i in SV:
	w0 += y_train[i][0]
	for j in SO:
		w0 -= alpha[j][0] * y_train[j][0] * P_Mat[j][i]
w0 /= len(SV)
```

Result:

![](soft_margin.png)

When gamma is set too large, it tends to overfitting.

![](soft_margin_overfitting_gamma=50.png)