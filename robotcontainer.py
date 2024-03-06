import math
import logging

logger = logging.getLogger("project212_robot")
import wpilib
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
from pathplannerlib.path import PathPlannerPath, PathConstraints, GoalEndState

from swervepy import u, SwerveDrive, TrajectoryFollowerParameters
from swervepy.impl import CoaxialSwerveModule

from constants import PHYS, MECH, ELEC, OP, SW
import subsystems.swerveComponents as SwerveComponents
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
import subsystems.drivetrainSubsystem

# Command Imports
from commands.shooterCommand import inwardsShooter, outwardsShooter, stopShooter
from commands.intakeCommand import intake, outake, stopIntake, IntakeLimitCommand
from commands.OuttakeCommand import outtakeCommand, stopBothIntakeAndShooter
import commands.armCommand
import commands.hangCommand
import commands.drivetrainCommand


class RobotContainer:
    """
    This example robot container should serve as a demonstration for how to
    implement swervepy on your robot.  You should not need to edit much of the
    code in this module to get a test working.  Instead, edit the values and
    class choices in constants.py.
    """

    def __init__(self):
        
        # Determine what the current reading of the 4 encoders should be, given
	    # that SW.XX_enc_zeropos says where the wheels face front
	    #
        """
        lf_enc_pos = self.lf_enc.absolute_position_degrees - SW.lf_enc_zeropos
        rf_enc_pos = self.rf_enc.absolute_position_degrees - SW.rf_enc_zeropos
        lb_enc_pos = self.lb_enc.absolute_position_degrees - SW.lb_enc_zeropos
        rb_enc_pos = self.rb_enc.absolute_position_degrees - SW.rb_enc_zeropos
        """
        
        
        
        
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
        
        self.drivetrain = subsystems.drivetrainSubsystem.drivetrainSubsystem(self.DriverController)
        self.swerve = subsystems.drivetrainSubsystem.drivetrainSubsystem.swerve

        # Configure the button bindings
        
        
        
        

        # Set the swerve subsystem's default command to teleoperate using
        # the controller joysticks
        #

    

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
        
        #self.drivetrain.setDefaultCommand(commands.drivetr dainCommand.drivetrainCommand(self.drivetrain))
        self.drivetrain.setDefaultCommand(subsystems.drivetrainSubsystem.drivetrainSubsystem.swerve)
        

    def getAutonomousCommand(self):
        return None