from constants import PHYS, MECH, OP, ELEC, SW
from swervepy.impl import (
    AbsoluteDutyCycleEncoder,
    CoaxialSwerveModule,
    NEOCoaxialDriveComponent,
    NEOCoaxialAzimuthComponent,
)
from swervepy.impl.sensor import NavXGyro

drive_component_class = NEOCoaxialDriveComponent
azimuth_component_class = NEOCoaxialAzimuthComponent
gyro_component_class = NavXGyro
absolute_encoder_class = AbsoluteDutyCycleEncoder

drive_param_values = {
    "wheel_circumference": PHYS.wheel_circumference,
    "gear_ratio": MECH.swerve_module_driving_gearing_ratio,
    "max_speed": OP.max_possible_speed,
    "open_loop_ramp_rate": ELEC.open_loop_ramp_rate,
    "closed_loop_ramp_rate": ELEC.closed_loop_ramp_rate,
    "continuous_current_limit": ELEC.drive_continuous_current_limit,
    "peak_current_limit": ELEC.drive_peak_current_limit,
    "neutral_mode": OP.driving_neutral,
    "invert_motor": MECH.driving_motor_inverted,
    "kP": SW.driving_kP,
    "kI": SW.driving_kI,
    "kD": SW.driving_kD,
    "kS": SW.driving_kS,
    "kV": SW.driving_kV,
    "kA": SW.driving_kA,
}

azimuth_param_values = {
    "gear_ratio": MECH.swerve_module_turning_gearing_ratio,
    "max_angular_velocity": OP.max_angular_velocity,
    "ramp_rate": 0,
    "continuous_current_limit": ELEC.turn_continuous_current_limit,
    "peak_current_limit": ELEC.turn_peak_current_limit,
    "neutral_mode": OP.turning_neutral,
    "kP": SW.turning_kP,
    "kI": SW.turning_kI,
    "kD": SW.turning_kD,
    "invert_motor": MECH.turning_motor_inverted,
}

gyro_param_values = {
    "invert": False
}

drive_component_params_class = drive_component_class.Parameters
azimuth_component_params_class = azimuth_component_class.Parameters

drive_params = drive_component_params_class(**drive_param_values)
azimuth_params = azimuth_component_params_class(**azimuth_param_values)
