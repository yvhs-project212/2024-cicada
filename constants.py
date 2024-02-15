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
    "swerve_module_wheel_diameter_in_inch": 4,
    "swerve_module_wheel_diameter_in_meter": 0.1016
}
PHYS = namedtuple("Data", phys_data.keys())(**phys_data)

# Mechanical constants, e.g. gearing ratios, whether motors are inverted
mech_data = {
    "swerve_module_driving_gearing_ratio": 6.75,  # SDS Mk4i L2
    "swerve_module_turning_gearing_ratio": 150 / 7,  # SDS Mk4i
}
MECH = namedtuple("Data", mech_data.keys())(**mech_data)

# Electrical constants, e.g. current limits, CAN bus IDs, RoboRIO port numbers
elec_data = {

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
    "swerve_drive_turning_PID_controller_kP": 1,
    "swerve_drive_turning_PID_controller_kI": 0,
    "swerve_drive_turning_PID_controller_kD": 0,
    "swerve_drive_driving_encoder_rotation2meter": 
    MECH.swerve_module_driving_gearing_ratio * math.pi * PHYS.swerve_module_wheel_diameter_in_meter,
    "swerve_drive_turning_encoder_rotation2radian": 
    MECH.swerve_module_turning_gearing_ratio * 2 * math.pi,
    "swerve_drive_driving_encoder_rotation2meter_per_sec":
    (MECH.swerve_module_driving_gearing_ratio * math.pi * PHYS.swerve_module_wheel_diameter_in_meter)/60,
    "swerve_drive_turning_encoder_rotation2radian_per_sec": 
    (MECH.swerve_module_turning_gearing_ratio * 2 * math.pi)/60

}
SW = namedtuple("Data", sw_data.keys())(**sw_data)
