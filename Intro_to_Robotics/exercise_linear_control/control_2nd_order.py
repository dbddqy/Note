import numpy as np
import random
from matplotlib import pyplot as plt


class System:
    def __init__(self, x0, v0, m=1., b=2., k=1., control=False):
        self.m = m
        self.b = b
        self.k = k
        self.x = x0
        self.v = v0
        self.control = control
        self.a = (self.f() - self.b*self.v - self.k*self.x) / self.m

    def f(self):
        if self.control:
            kp = 16.
            kv = 2*np.sqrt(kp)
            f_prime = -kp*self.x-kv*self.v
            f = f_prime*self.m + self.b*self.v+self.k*self.x
            return f
        else:
            return 0.

    def update(self, dt=0.1):
        self.v += (self.a * dt)
        self.x += (self.v * dt)
        self.a = (self.f() - self.b*self.v - self.k*self.x) / self.m + np.random.normal(0.0, 0.00)


if __name__ == "__main__":
    s = System(2., 0., b=4., control=True)
    x_data, v_data, a_data, time = [], [], [], []
    for i in range(1000):
        x_data.append(s.x)
        v_data.append(s.v)
        a_data.append(s.a)
        time.append(i*0.01)
        s.update(0.01)

    plt.plot(time, x_data)
    plt.plot(time, v_data)
    plt.plot(time, a_data)
    plt.legend(["x", "v", "a"])
    plt.show()
