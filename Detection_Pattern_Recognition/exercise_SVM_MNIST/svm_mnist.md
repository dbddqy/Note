# Multi-class SVM for solving MNIST

Use one against the rest strategy, so 10 SVMs are trained. They are stored in class TenClassSVM:

```python
class TenClassSVM:
    def __init__(self, _alphas, _xs, _ys, _ws, _gamma, _kernel, _C):
        self.gamma = _gamma
        self.kernel = _kernel
        self.C = _C
        self.alphas = _alphas
        self.xs = _xs
        self.ys = _ys
        self.ws = _ws
    def predict(self, x, _label):
        alpha_use = self.alphas[_label]
        x_use = self.xs[_label]
        y_use = self.ys[_label]
        pred = self.ws[_label]
        for index in range(alpha_use.shape[0]):
            pred += (alpha_use[index][0] * y_use[index][0] * self.kernel(x_use[index], x, self.gamma))
        return pred
```

PCA for feature dimension reduction.

```python
# PCA
x_train_flattened = np.array(x_train.reshape([N, 28*28, 1]), dtype=np.float32)
R = np.einsum("ijk, ilk -> ijl", x_train_flattened, x_train_flattened).mean(axis=0)
e_vals, e_vecs = np.linalg.eig(R)
W = e_vecs[:, :50]
x_train_reduced = W.T.dot(x_train_flattened.reshape([N, 28*28]).T).T
```

The training process of a SVM:

```python
def trainSVM(x, y, _kernel, _gamma, _C):
    n = y.shape[0]
    P_Mat = get_P_Mat(x, y, kernel=_kernel, _gamma=_gamma)
    # optimizaton
    P = matrix(P_Mat)
    q = matrix(-np.ones([n, 1]))
    # 2*n inequality constraints
    G = matrix(np.vstack([-np.eye(n), np.eye(n)]))
    h = matrix(np.vstack([np.zeros([n, 1]), _C * np.ones([n, 1])]))
    # 1 equality constraint
    A = matrix(y.T)
    b = matrix(0.)
    sol = solvers.qp(P, q, G, h, A, b)
    alpha = np.array(sol['x'])
    # get SVs and SOs
    SV, SO = [], []
    for i in range(n):
        if alpha[i][0] < 0.001:
            continue
        if abs(alpha[i][0] - _C) > 0.001:
            SV.append(i)
        SO.append(i)
    # calculate b
    w0 = 0.
    for i in SV:
        w0 += y[i][0]
        for j in SO:
            w0 -= alpha[j][0] * y[j][0] * P_Mat[j][i]
    w0 /= len(SV)
    return alpha[SO], x[SO], y[SO], w0
```

Save the load models:

```python
# save model
model = TenClassSVM(alphas, xs, ys, ws, gamma, kernel, C)
f = open('model_1.pickle', 'wb')
pickle.dump(model, f)
f.close()

# load model
f = open('model_1.pickle', 'rb')
model = pickle.load(f)
f.close()
```

Make prediction:

```python
def predict(x, label, kernel, _gamma):
    global alphas, SOs, ws
    global x_train_reduced, y_train
    pred = ws[label]
    for index in range(alphas[label].shape[0]):
        pred += (alphas[label][index][0] * y_train[SOs[label][index]] * kernel(x_train_reduced[SOs[label][index]], x, _gamma))
    return pred
```

Final result tends to over-fitting (perhaps gamma value has to be further tuned):

> training error rate: 0.007500
> test error rate: 0.100000