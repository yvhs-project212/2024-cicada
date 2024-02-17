"""
This file defines constants related to your robot.  These constants include:

 * Physical constants (exterior dimensions, wheel base)

 * Mechanical constants (gear reduction ratios)

 * Electrical constants (current limits, CAN bus IDs, roboRIO slot numbers)

 * Operation constants (desired max velocity, max turning speed)

 * Software constants (USB ID for driver joystick)
"""

import math
from collections import namedtuple
import rev

# Physical constants, e.g. wheel circumference, physical dimensions
phys_data = {
}
PHYS = namedtuple("Data", phys_data.keys())(**phys_data)

# Mechanical constants, e.g. gearing ratios, whether motors are inverted
mech_data = {
}
MECH = namedtuple("Data", mech_data.keys())(**mech_data)

# Electrical constants, e.g. current limits, CAN bus IDs, RoboRIO port numbers
elec_data = {
    "hang_motor_CAN_ID": 4,
    "lower_motor_CAN_ID": 3,
}
ELEC = namedtuple("Data", elec_data.keys())(**elec_data)

# Operation constants, e.g. preferred brake mode, which joystick to use
op_data = {
    "driver_joystick_port": 0,
    "operator_joystick_port": 1,
}
OP = namedtuple("Data", op_data.keys())(**op_data)

# Software constants, e.g. PID values, absolute encoder zero points
sw_data = {
}
SW = namedtuple("Data", sw_data.keys())(**sw_data)
