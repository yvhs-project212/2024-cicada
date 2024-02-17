import math
import wpilib
import rev
import DrivetrainParameters
import commands2
from swervepy import u, SwerveDrive, TrajectoryFollowerParameters
from swervepy.impl import CoaxialSwerveModule
from constants import PHYS, MECH, ELEC, OP, SW
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
from pathplannerlib.path import PathPlannerPath, PathConstraints, GoalEndState

class DrivetrainSubsystem (commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        swerve_gyro = DrivetrainParameters.gyro_component_class(**DrivetrainParameters.gyro_param_values)
        self.gyro = swerve_gyro.navx

        self.lf_enc = DrivetrainParameters.absolute_encoder_class(
            ELEC.LF_encoder_DIO, SW.lf_faceforward_position)
        self.lb_enc = DrivetrainParameters.absolute_encoder_class(
            ELEC.LB_encoder_DIO, SW.lb_faceforward_position)
        self.rf_enc = DrivetrainParameters.absolute_encoder_class(
            ELEC.RF_encoder_DIO, SW.rf_faceforward_position)
        self.rb_enc = DrivetrainParameters.absolute_encoder_class(
            ELEC.RB_encoder_DIO, SW.rb_faceforward_position)
        
        lf_enc_pos = self.lf_enc.absolute_position_degrees - SW.lf_faceforward_position
        rf_enc_pos = self.rf_enc.absolute_position_degrees - SW.rf_faceforward_position
        lb_enc_pos = self.lb_enc.absolute_position_degrees - SW.lb_faceforward_position
        rb_enc_pos = self.rb_enc.absolute_position_degrees - SW.rb_faceforward_position

        modules = (
            #Left Front
            CoaxialSwerveModule(
                drive=DrivetrainParameters.drive_component_class(
                    id_=ELEC.LF_drive_CAN_ID,
                    parameters=DrivetrainParameters.drive_params),
                azimuth=DrivetrainParameters.azimuth_component_class(
                    id_=ELEC.LF_turn_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(lf_enc_pos),
                    parameters=DrivetrainParameters.azimuth_params,
                    absolute_encoder=self.lf_enc),
                placement=Translation2d(*DrivetrainParameters.module_locations['LF']),
            ),
            #Right Front
            CoaxialSwerveModule(
                drive=DrivetrainParameters.drive_component_class(
                    id_=ELEC.RF_drive_CAN_ID,
                    parameters=DrivetrainParameters.drive_params),
                azimuth=DrivetrainParameters.azimuth_component_class(
                    id_=ELEC.RF_turn_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(rf_enc_pos),
                    parameters=DrivetrainParameters.azimuth_params,
                    absolute_encoder=self.rf_enc),
                placement=Translation2d(*DrivetrainParameters.module_locations['RF']),
            ),
            #Left Back
            CoaxialSwerveModule(
                drive=DrivetrainParameters.drive_component_class(
                    id_=ELEC.LB_drive_CAN_ID,
                    parameters=DrivetrainParameters.drive_params),
                azimuth=DrivetrainParameters.azimuth_component_class(
                    id_=ELEC.LB_turn_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(lb_enc_pos),
                    parameters=DrivetrainParameters.azimuth_params,
                    absolute_encoder=self.lb_enc),
                placement=Translation2d(*DrivetrainParameters.module_locations['LB']),
            ),
            #Right Back
             CoaxialSwerveModule(
                drive=DrivetrainParameters.drive_component_class(
                    id_=ELEC.RB_drive_CAN_ID,
                    parameters=DrivetrainParameters.drive_params),
                azimuth=DrivetrainParameters.azimuth_component_class(
                    id_=ELEC.RB_turn_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(rb_enc_pos),
                    parameters=DrivetrainParameters.azimuth_params,
                    absolute_encoder=self.rb_enc),
                placement=Translation2d(*DrivetrainParameters.module_locations['RB']),
            )
            
        )