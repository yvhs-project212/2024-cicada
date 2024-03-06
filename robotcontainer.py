import math
import logging

logger = logging.getLogger("project212_robot")
import wpilib
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
from pathplannerlib.path import PathPlannerPath, PathConstraints, GoalEndState

from swervepy import u, SwerveDrive, TrajectoryFollowerParameters
from swervepy.impl import CoaxialSwerveModule

from constants import PHYS, MECH, ELEC, OP, SW
import components
import commands2
#import commands2.cmd
import commands2.button

# Constants
import constants
from constants import OP, SW

# Subsystem Imports
import subsystems.shooterSubsystem
import subsystems.intakeSubsystem
import subsystems.armSubsystem
import subsystems.hangSubsystem
import subsystems.photonVisionSubsystem
import subsystems.armSubsystem
import subsystems.hangSubsystem

# Command Imports
from commands.shooterCommand import inwardsShooter, outwardsShooter, stopShooter
from commands.intakeCommand import intake, outake, stopIntake, IntakeLimitCommand
from commands.OuttakeCommand import outtakeCommand, stopBothIntakeAndShooter
from commands.intakeCommand import intake, outake, stopIntake
from commands.visionCommand import takeSnapShot, togglePipeline, doNothing
import commands.armCommand
import commands.hangCommand

import commands.autonomousCommands.driveForwardCommand


class RobotContainer:
    """
    This example robot container should serve as a demonstration for how to
    implement swervepy on your robot.  You should not need to edit much of the
    code in this module to get a test working.  Instead, edit the values and
    class choices in constants.py.
    """

    def __init__(self):
        navx_adapter = components.gyro_component_class(**components.gyro_param_values)
        self.gyro = navx_adapter.navx
        self.gyro.zeroYaw()


        # The Azimuth component included the absolute encoder because it needs
        # to be able to reset to absolute position.
        #
        self.lf_enc = components.absolute_encoder_class(ELEC.LF_encoder_DIO, SW.lf_enc_zeropos)
        self.lb_enc = components.absolute_encoder_class(ELEC.LB_encoder_DIO, SW.lb_enc_zeropos)
        self.rb_enc = components.absolute_encoder_class(ELEC.RB_encoder_DIO, SW.rb_enc_zeropos)
        self.rf_enc = components.absolute_encoder_class(ELEC.RF_encoder_DIO, SW.rf_enc_zeropos)

        # Determine what the current reading of the 4 encoders should be, given
	    # that SW.XX_enc_zeropos says where the wheels face front
	    #
        """
        lf_enc_pos = self.lf_enc.absolute_position_degrees - SW.lf_enc_zeropos
        rf_enc_pos = self.rf_enc.absolute_position_degrees - SW.rf_enc_zeropos
        lb_enc_pos = self.lb_enc.absolute_position_degrees - SW.lb_enc_zeropos
        rb_enc_pos = self.rb_enc.absolute_position_degrees - SW.rb_enc_zeropos
        """
        lf_enc_pos = self.lf_enc.absolute_position_degrees
        rf_enc_pos = self.rf_enc.absolute_position_degrees
        lb_enc_pos = self.lb_enc.absolute_position_degrees
        rb_enc_pos = self.rb_enc.absolute_position_degrees
        logger.info(f"Encoder positions: LF={lf_enc_pos}, RF={rf_enc_pos}, RB={rb_enc_pos}, LB={lb_enc_pos}")
        
        
        
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The robot's subsystems
        self.shooter = subsystems.shooterSubsystem.shooterSubsystem()
        self.intake = subsystems.intakeSubsystem.intakeSubsystem()
        self.arm = subsystems.armSubsystem.ArmSubsystem()        
        self.hang = subsystems.hangSubsystem.HangSubsystem()
        self.Vision = subsystems.photonVisionSubsystem.visionSub()

        # The driver's controller
        self.DriverController = commands2.button.CommandXboxController(OP.driver_controller)
        self.OperatorController = commands2.button.CommandXboxController(OP.operator_controller)

        # Configure the button bindings
        self.configureButtonBindings()
        
        
        
        modules = (
            # Left Front module
            CoaxialSwerveModule(
                drive=components.drive_component_class(
                    id_=ELEC.LF_drive_CAN_ID,
                    parameters=components.drive_params,
                ),
                azimuth=components.azimuth_component_class(
                    id_=ELEC.LF_steer_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(lf_enc_pos),
                    parameters=components.azimuth_params,
                    absolute_encoder=self.lf_enc,
                ),
                placement=Translation2d(*components.module_locations["LF"]),
            ),
            # Right Front module
            CoaxialSwerveModule(
                drive=components.drive_component_class(
                    id_=ELEC.RF_drive_CAN_ID,
                    parameters=components.drive_params,
                ),
                azimuth=components.azimuth_component_class(
                    id_=ELEC.RF_steer_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(rf_enc_pos),
                    parameters=components.azimuth_params,
                    absolute_encoder=self.rf_enc,
                ),
                placement=Translation2d(*components.module_locations["RF"]),
            ),
            # Left Back module
            CoaxialSwerveModule(
                drive=components.drive_component_class(
                    id_=ELEC.LB_drive_CAN_ID,
                    parameters=components.drive_params,
                ),
                azimuth=components.azimuth_component_class(
                    id_=ELEC.LB_steer_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(lb_enc_pos),
                    parameters=components.azimuth_params,
                    absolute_encoder=self.lb_enc,
                ),
                placement=Translation2d(*components.module_locations["LB"]),
            ),
            # Right Back module
            CoaxialSwerveModule(
                drive=components.drive_component_class(
                    id_=ELEC.RB_drive_CAN_ID,
                    parameters=components.drive_params,
                ),
                azimuth=components.azimuth_component_class(
                    id_=ELEC.RB_steer_CAN_ID,
                    azimuth_offset=Rotation2d.fromDegrees(rb_enc_pos),
                    parameters=components.azimuth_params,
                    absolute_encoder=self.rb_enc,
                ),
                placement=Translation2d(*components.module_locations["RB"]),
            ),
        )

        self.speed_limit_ratio = 1.0
        if OP.speed_limit:
            if OP.speed_limit > OP.max_speed:
                wpilib.reportWarning("Speed limit is greater than max_speed and won't be used")
            else:
                self.speed_limit_ratio = OP.speed_limit / OP.max_speed

        self.angular_velocity_limit_ratio = 1.0
        if OP.angular_velocity_limit:
            if OP.angular_velocity_limit > OP.max_angular_velocity:
                wpilib.reportWarning("Angular velocity limit is greater than max_angular_velocity and won't be used")
            else:
                self.angular_velocity_limit_ratio = (
                    OP.angular_velocity_limit / OP.max_angular_velocity)

        # Define a swerve drive subsystem by passing in a list of SwerveModules
        # and some options
        #
        self.swerve = SwerveDrive(modules, navx_adapter, OP.max_speed, OP.max_angular_velocity)

        # Set the swerve subsystem's default command to teleoperate using
        # the controller joysticks
        #
        self.swerve.setDefaultCommand(
            self.swerve.teleop_command(
                translation=self.get_translation_input,
                strafe=self.get_strafe_input,
                rotation=self.get_rotation_input,
                field_relative=SW.field_relative,
                drive_open_loop=SW.drive_open_loop,
            )
        )

    def log_data(self):
        for pos in ("LF", "RF", "LB", "RB"):
            encoder = getattr(self, f"{pos.lower()}_enc")
            wpilib.SmartDashboard.putNumber(f"{pos} absolute encoder", encoder.absolute_position_degrees)
            wpilib.SmartDashboard.putNumber(f"{pos} absolute encoder", encoder.absolute_position_degrees)

    @staticmethod
    def deadband(value, band):
        return value if abs(value) > band else 0

    def process_joystick_input(self, val, deadband=0.1, exponent=1, limit_ratio=1.0, invert=False):
        """
        Given a raw joystick reading, return the processed value after adjusting
        for real-world UX considerations:
          * apply a deadband to ignore jitter around zero
          * apply an exponent for greater low-velocity control
        """
        deadbanded_input = self.deadband(val, deadband)
        input_sign = +1 if val > 0 else -1  # this works for val=0 also
        invert_sign = -1 if invert else +1
        # abs required for fractional exponents
        scaled_input = limit_ratio * abs(deadbanded_input) ** exponent
        return invert_sign * input_sign * scaled_input

    def get_translation_input(self, invert=True):
        raw_stick_val = self.DriverController.getRawAxis(OP.translation_joystick_axis)
        return self.process_joystick_input(raw_stick_val, invert=invert,
                                           limit_ratio=self.speed_limit_ratio)

    def get_strafe_input(self, invert=True):
        raw_stick_val = self.DriverController.getRawAxis(OP.strafe_joystick_axis)
        return self.process_joystick_input(raw_stick_val, invert=invert,
                                           limit_ratio=self.speed_limit_ratio)

    def get_rotation_input(self, invert=True):
        raw_stick_val = self.DriverController.getRawAxis(OP.rotation_joystick_axis)
        return self.process_joystick_input(
            raw_stick_val, invert=invert, limit_ratio=self.angular_velocity_limit_ratio)

    def get_autonomous_command(self):
        follower_params = TrajectoryFollowerParameters(
            max_drive_velocity=4.5 * (u.m / u.s),
            theta_kP=1,
            xy_kP=1,
        )

        bezier_points = PathPlannerPath.bezierFromPoses(
            [
                Pose2d(1.0, 1.0, Rotation2d.fromDegrees(0)),
                Pose2d(3.0, 1.0, Rotation2d.fromDegrees(0)),
                Pose2d(5.0, 3.0, Rotation2d.fromDegrees(90)),
            ]
        )
        path = PathPlannerPath(
            bezier_points,
            PathConstraints(3.0, 3.0, 2 * math.pi, 4 * math.pi),
            GoalEndState(0.0, Rotation2d.fromDegrees(-90)),  # Zero velocity and facing 90 degrees clockwise
        )

        first_path = True  # reset robot pose to initial pose in trajectory
        open_loop = True  # don't use built-in motor feedback for velocity
        return self.swerve.follow_trajectory_command(path, follower_params, first_path, open_loop)



    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        self.OperatorController.button(1).whileTrue(IntakeLimitCommand(self.intake))
        #self.OperatorController.button(1).whileFalse(stopIntake(self.intake))
        
        self.OperatorController.leftBumper().whileTrue(intake(self.intake))
        self.OperatorController.leftBumper().whileFalse(stopIntake(self.intake))
        
        self.OperatorController.rightBumper().whileTrue(outwardsShooter(self.shooter))
        self.OperatorController.rightBumper().whileFalse(stopShooter(self.shooter))
        
        self.OperatorController.button(2).whileTrue(outtakeCommand(self.intake, self.shooter))
        self.OperatorController.button(2).whileFalse(stopBothIntakeAndShooter(self.intake, self.shooter))
        
        self.arm.setDefaultCommand(commands.armCommand.ArmWithJoystick(self.arm))
        
        self.hang.setDefaultCommand(commands.hangCommand.HangCommand(self.hang))
        

    def getAutonomousCommand(self):
        return commands.autonomousCommands.driveForwardCommand(self.swerve)