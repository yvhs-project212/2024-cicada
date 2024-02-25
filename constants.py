"""
This file defines constants related to your robot.  These constants include:

 * Physical constants (exterior dimensions, wheelbase)

 * Mechanical constants (gear reduction ratios)

 * Electrical constants (current limits, CAN bus IDs, roboRIO slot numbers)

 * Operation constants (desired max velocity, max turning speed)

 * Software constants (USB ID for driver joystick)
"""

import math
from collections import namedtuple
import rev
import phoenix5

# Physical constants
phys_data = {
}
PHYS = namedtuple("Data", phys_data.keys())(**phys_data)

# Mechanical constants
mech_data = {
}
MECH = namedtuple("Data", mech_data.keys())(**mech_data)

# Electrical constants
elec_data = {
    "shooter_Motor1": 5,
    "shooter_Motor2": 6,
    "intake_motor": 7,    
    "arm_motor1_CAN_ID": 8,
    "arm_motor2_CAN_ID": 9,    
    "hang_motor_CAN_ID": 10,
    "lower_motor_CAN_ID": 19,
}
ELEC = namedtuple("Data", elec_data.keys())(**elec_data)

JOYSTICK_AXES = {
}

# Operation constants
op_data = {
}
OP = namedtuple("Data", op_data.keys())(**op_data)

# Software constants
sw_data = {
}
SW = namedtuple("Data", sw_data.keys())(**sw_data)
