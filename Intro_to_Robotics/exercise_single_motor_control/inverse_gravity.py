#!/usr/bin/env python3

import odrive
from odrive.enums import *
import time

from math import pi, sin

length = 0.105  # [m]
weight = 0.016  # [kg]
g = 9.8128  # [m/s^2]
k = 0.01095249  # [Nm/A]
offset = 1146

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
    vel = axis.encoder.vel_estimate
    if vel > 0:
        vel_compensate = 0.37
    else:
        vel_compensate = -0.37
    pos = (axis.encoder.pos_estimate - offset) / 2000.0 * pi
    current = - 1.5 * sin(pos) * length * weight * g / k + vel_compensate
    axis.controller.current_setpoint = current
    print ("current: %f", current)

