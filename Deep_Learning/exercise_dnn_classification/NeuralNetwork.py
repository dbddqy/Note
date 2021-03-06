from funcs import *


class NeuralNetwork:
    def __init__(self, dim_in):
        self.Ws = []
        self.Bs = []
        self.activations = []
        self.d_activations = []
        self.dims = [dim_in]

    def add_dense_layer(self, n, activation=relu, d_activation=d_relu):
        self.Ws.append(np.random.normal(0., 2./self.dims[-1], [n, self.dims[-1]]))
        self.Bs.append(np.zeros([n, 1]))
        self.activations.append(activation)
        self.d_activations.append(d_activation)
        self.dims.append(n)

    def model(self, x0):
        x_temp = x0
        x = [x_temp]
        for i in range(len(self.Ws)):
            x_temp = self.activations[i](self.Ws[i].dot(x_temp) + self.Bs[i])
            x.append(x_temp)
        return x

    def gradient(self, xs, ys, d_loss_f):
        grad_w, grad_b = [], []
        for i in range(len(self.Ws)):
            grad_w.append(np.zeros(self.Ws[i].shape))
            grad_b.append(np.zeros(self.Bs[i].shape))
        for i in range(len(xs)):
            x = self.model(xs[i:i+1].T)  # (x, 1)
            y = ys[i:i+1].T  # (x, 1)
            index = -1
            jacobi = d_loss_f(x[index], y).dot(self.d_activations[index](x[index]))  # (1, x)*(x, x)
            while True:
                # grad["w3"] += np.dot(_loss_to_a3.T, x2.T)
                # grad["b3"] += _loss_to_a3.T
                grad_w[index] += jacobi.T.dot(x[index-1].T)  # (x, 1)*(1, y)
                grad_b[index] += jacobi.T  # (x, 1)
                if index == -len(self.Ws):
                    break
                # _a3_to_x2 = _theta["w3"]
                # _x2_to_a2 = np.diag((x2 - x2 * x2).reshape([5, ]))
                jacobi = jacobi.dot(self.Ws[index]).dot(self.d_activations[index-1](x[index-1]))  # (1, x)*(x, y)*(y, y)
                index -= 1
        for i in range(len(self.Ws)):
            grad_w[i] /= len(xs)
            grad_b[i] /= len(xs)
        return grad_w, grad_b

