#!/usr/bin/env python3

import odrive
from odrive.enums import *
import time

import numpy as np
import matplotlib.pyplot as plt

from math import pi, sin, cos

length = 0.2  # [m]
mass = 0.016  # [kg]
g = 9.8128  # [m/s^2]
ki = 0.01095249  # [Nm/A]
offset = 1146

M = mass * length * length / 3.
K = - mass * g * length / 2.

T = 1  # [s]
omega = 2 * pi / T
interval = 1000  # 100 control loops / s
q_max = 20.0 * pi / 180

# trajectory
# q = q_max * sin(omega * t)
q_0, q_1, q_2 = [], [], []
for i in range(T*interval):
    t = i / interval
    q_0.append(q_max * sin(omega * t))
    q_1.append(q_max * omega * cos(omega * t))
    q_2.append(q_max * omega * omega * -sin(omega * t))
# q_0 = np.array(q_0)
# q_2 = np.array(q_2)
# plt.plot(q_0 * K / ki)
# # plt.plot(q_1)
# plt.plot(q_2 * M / ki)
# plt.show()



kp = 900.
kv = 2*np.sqrt(kp)

# torque = M * (q_2[0] + kv * (q_1[0]-0) + kp * (q_0[0]-0.5)) + K * 0.5
# print(torque/ki)

odrv = odrive.find_any(serial_number="2083359F524B") # 24V_taobao axis_3 axis_4
axis = odrv.axis1

key = input("press any key to start calibration..")

axis.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while axis.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

axis.controller.config.vel_limit_tolerance = 0
axis.controller.config.control_mode = 3
axis.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
axis.controller.pos_setpoint = offset

key = input("please install the link")

axis.requested_state = AXIS_STATE_IDLE
axis.controller.config.control_mode = 1
axis.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

key = input("please confirm link installed")

while (True):
    for i in range(T*interval):
        qd_0 = (axis.encoder.pos_estimate - offset) / 2000.0 * pi
        qd_1 = axis.encoder.vel_estimate / 2000.0 * pi
        torque = M * (q_2[i] + kv * (q_1[i]-qd_1) + kp * (q_0[i]-qd_0)) + K * qd_0
        axis.controller.current_setpoint = torque / ki
        time.sleep(1./interval - 0.00086)


