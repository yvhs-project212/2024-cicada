import math
import logging

logger = logging.getLogger("project212_robot")
import wpilib
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
from pathplannerlib.path import PathPlannerPath, PathConstraints, GoalEndState

from swervepy import u, SwerveDrive, TrajectoryFollowerParameters
from swervepy.impl import CoaxialSwerveModule

from constants import PHYS, MECH, ELEC, OP, SW
import subsystems.swerveComponents as swerveComponents
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
import subsystems.swerveSubsystem
import subsystems.ledsSubsystem

# Command Imports
from commands.shooterCommand import inwardsShooter, outwardsShooter, stopShooter
from commands.intakeCommand import intake, outake, stopIntake, IntakeLimitCommand
from commands.OuttakeCommand import outtakeCommand, stopBothIntakeAndShooter
from commands.intakeCommand import intake, outake, stopIntake
from commands.visionCommand import takeSnapShot, togglePipeline #doNothing
from commands.armCommand import armToGround, armToAmp, armStop
from commands.ledCommand import ledMode1, ledMode2, ledMode3
import commands.armCommand
import commands.hangCommand

#Auto Command Imports
import commands.autonomousCommands.driveForwardCommand
import commands.autonomousCommands.autoShootingCommand
import commands.autonomousCommands.autoDropArmCommand


class RobotContainer:
    """
    This example robot container should serve as a demonstration for how to
    implement swervepy on your robot.  You should not need to edit much of the
    code in this module to get a test working.  Instead, edit the values and
    class choices in constants.py.
    """

    def __init__(self):

        # The robot's subsystems
        self.shooter = subsystems.shooterSubsystem.shooterSubsystem()
        self.intake = subsystems.intakeSubsystem.intakeSubsystem()
        self.arm = subsystems.armSubsystem.ArmSubsystem()        
        self.hang = subsystems.hangSubsystem.HangSubsystem()
        self.Vision = subsystems.photonVisionSubsystem.visionSub()
        self.drivetrain = subsystems.swerveSubsystem.swerveSubsystem()
        self.leds = subsystems.ledsSubsystem.ledSub()
        self.swerve = self.drivetrain.getSwerve()

        # The driver's controller
        self.DriverController = commands2.button.CommandXboxController(OP.driver_controller)
        self.OperatorController = commands2.button.CommandXboxController(OP.operator_controller)  
        
        #Autos
        self.dropArmAndScore = commands2.SequentialCommandGroup(commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm), 
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter))
        
        self.autoChooser = wpilib.SendableChooser()
        self.autoChooser.setDefaultOption("DriveForward", commands.autonomousCommands.driveForwardCommand.getAutoCommand(self.swerve, 5.0))
        self.autoChooser.addOption("ScoreOneNote", self.dropArmAndScore)
        self.autoChooser.addOption("autoDropArm", commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm))
        
        wpilib.SmartDashboard.putData(self.autoChooser)
        
        self.configureButtonBindings()


    def get_autonomous_command(self):
        return self.autoChooser.getSelected()

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        # self.DriverController.button(1).whileTrue()
        
        self.OperatorController.button(1).whileTrue(IntakeLimitCommand(self.intake))
        
        self.OperatorController.leftBumper().whileTrue(intake(self.intake))
        self.OperatorController.leftBumper().whileFalse(stopIntake(self.intake))
        
        self.OperatorController.rightBumper().whileTrue(outwardsShooter(self.shooter))
        self.OperatorController.rightBumper().whileFalse(stopShooter(self.shooter))
        
        self.OperatorController.button(2).whileTrue(outake(self.intake))
        self.OperatorController.button(2).whileFalse(stopIntake(self.intake))
        
        # self.OperatorController.button(4).toggleOnTrue(armToAmp(self.arm))
        # self.OperatorController.button(4).toggleOnFalse(armStop(self.arm))
        self.OperatorController.button(4).whileTrue(ledMode2(self.leds))
        
        # self.OperatorController.button(3).toggleOnTrue(armToGround(self.arm))
        # self.OperatorController.button(3).toggleOnFalse(armStop(self.arm))
        self.OperatorController.button(3).whileTrue(ledMode1(self.leds))
        
        self.OperatorController.button(7).whileTrue(togglePipeline(self.Vision))
        # self.OperatorController.button(7).whileFalse(doNothing(self.Vision))
        
        self.OperatorController.button(8).toggleOnTrue(takeSnapShot(self.Vision))
        # self.OperatorController.button(8).whileFalse(doNothing(self.Vision))
        
        self.arm.setDefaultCommand(commands.armCommand.ArmWithJoystick(self.arm))
        
        self.hang.setDefaultCommand(commands.hangCommand.HangCommand(self.hang))
        
        self.swerve.setDefaultCommand(self.drivetrain.getSwerveTeleopCommand(self.swerve))