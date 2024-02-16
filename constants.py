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
from swervepy import u

# Physical constants, e.g. wheel circumference, physical dimensions
phys_data = {
    "track_width": 0,
    "wheel_base": 0,
    "wheel_circumference": 4 * math.pi * u.inch
}
PHYS = namedtuple("Data", phys_data.keys())(**phys_data)

# Mechanical constants, e.g. gearing ratios, whether motors are inverted
mech_data = {
    "swerve_module_driving_gearing_ratio": 6.75,   # SDS Mk4i L2
    "swerve_module_turning_gearing_ratio": 150 / 7,  # SDS Mk4i

    "driving_motor_inverted": False,
    "turning_motor_inverted": True,
}
MECH = namedtuple("Data", mech_data.keys())(**mech_data)

# Electrical constants, e.g. current limits, CAN bus IDs, RoboRIO port numbers
elec_data = {
    "drive_continuous_current_limit": 40,
    "turn_continuous_current_limit": 30,
    "drive_peak_current_limit": 60,
    "turn_peak_current_limit": 40,

    "open_loop_ramp_rate": 1.0,
    "closed_loop_ramp_rate": 0.7,

    "RF_turn_CAN_ID": 11,
    "RF_drive_CAN_ID": 12,
    "RF_encoder_DIO": 0,
    "RB_turn_CAN_ID": 13,
    "RB_drive_CAN_ID": 14,
    "RB_encoder_DIO": 1,
    "LB_turn_CAN_ID": 15,
    "LB_drive_CAN_ID": 16,
    "LB_encoder_DIO": 2,
    "LF_turn_CAN_ID": 17,
    "LF_drive_CAN_ID": 18,
    "LF_encoder_DIO": 3,
}
ELEC = namedtuple("Data", elec_data.keys())(**elec_data)

# Operation constants, e.g. preferred brake mode, which joystick to use
op_data = {
    #Max Possible Speed
    "max_possible_speed": 4.5 * (u.m / u.s),
    "max_possible_angular_velocity": 11.5 * (u.rad / u.s),

    #Actual speed setting
    "speed_limit": 1.0 * (u.m / u.s),
    "angular_velocity_limit": 1.5 * (u.rad / u.s),

    "driving_neutral": rev.CANSparkMax.IdleMode.kBrake,
    "turning_neutral": rev.CANSparkMax.IdleMode.kBrake,

    "driver_joystick_port": 0,
    "operator_joystick_port": 1,

    "left_joystick_X_axis": 0,
    "left_joystick_Y_axis": 1,
    "right_joystick_X_axis": 4,
    "right_joystick_Y_axis": 5,
}
OP = namedtuple("Data", op_data.keys())(**op_data)

# Software constants, e.g. PID values, absolute encoder zero points
sw_data = {

    "lf_faceforward_position":  -89,
    "rf_faceforward_position":  185,
    "lb_faceforward_position":  135,
    "rb_faceforward_position":   45,

    "field_relative": True,
    "open_loop": True,
    
    # Constants for PID control of the driving AND turning motors
    # (kP must be non-zero, or azimuth motors won't engage.)
    #"kP": 0.3,   # representative value for Falcon500 motors
    "driving_kP": 0.01,   # representative value for NEO motors
    "driving_kI": 0,
    "driving_kD": 0,
    "turning_kP": 0.01,   # representative value for NEO motors
    "turning_kI": 0,
    "turning_kD": 0,

    # Constants for feed-forward of driving motors
    "driving_kS": 0,
    "driving_kV": 0,
    "driving_kA": 0,
}
SW = namedtuple("Data", sw_data.keys())(**sw_data)
