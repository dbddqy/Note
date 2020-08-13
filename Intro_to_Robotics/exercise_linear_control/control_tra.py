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
        self.goal = np.zeros([3, ])
        self.a = (self.f() - self.b*self.v - self.k*self.x) / self.m

    def set_goal(self, goal):
        self.goal = goal

    def f(self):
        if self.control:
            kp = 16.
            kv = 2*np.sqrt(kp)
            f_prime = kp*(self.goal[0]-self.x)+kv*(self.goal[1]-self.v)+self.goal[2]
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
    x_data, v_data, a_data = [], [], []
    time = np.arange(0., 10., 10./1000)

    # # step
    # goal = np.array([[0., 0., 0.],
    #                  [4., 0., 0.],
    #                  [2., 0., 0.]])
    # for i in range(1000):
    #     if i < 300:
    #         s.set_goal(goal[0])
    #     elif 300 < i < 700:
    #         s.set_goal(goal[1])
    #     else:
    #         s.set_goal(goal[2])
    #     x_data.append(s.x)
    #     v_data.append(s.v)
    #     a_data.append(s.a)
    #     s.update(0.01)

    # cubic polynomial y = 0.05 * (x^3-15*x^2+63*x)
    goal = np.zeros([1000, 3])
    for i in range(goal.shape[0]):
        x = 0.01 * i
        goal[i] = np.array([0.05*(x*x*x-15*x*x+63*x),
                            0.05*(3*x*x-30*x+63),
                            0.05*(6*x-30)])

    for i in range(1000):
        s.set_goal(goal[i])
        x_data.append(s.x)
        v_data.append(s.v)
        a_data.append(s.a)
        s.update(0.01)

    plt.plot(time, x_data)
    plt.plot(time, v_data)
    plt.plot(time, np.array(a_data)*0.1)
    plt.legend(["x", "v", "0.1*a"])
    plt.show()
