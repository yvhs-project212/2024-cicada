#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpimath.controller
import commands2
import commands2.cmd
import commands2.button

# Constants
import constants
from constants import OP, SW

# Subsystem Imports
import subsystems.shooterSubsystem
import subsystems.intakeSubsystem
import subsystems.photonVisionSubsystem
import subsystems.armSubsystem
import subsystems.hangSubsystem

# Command Imports
from commands.shooterCommand import inwardsShooter, outwardsShooter, stopShooter
from commands.intakeCommand import intake, outake, stopIntake
import commands.armCommand
import commands.hangCommand

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.  Since
    Command-based is a "declarative" paradigm, very little robot logic should
    actually be handled in the :class:`.Robot` periodic methods (other than
    the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The robot's subsystems
        self.shooter = subsystems.shooterSubsystem.shooterSubsystem()
        self.intake = subsystems.intakeSubsystem.intakeSubsystem()      
        self.hang = subsystems.hangSubsystem.HangSubsystem()        
        self.arm = subsystems.armSubsystem.ArmSubsystem()
        self.Vision = subsystems.photonVisionSubsystem.visionSub()

        # The driver's controller
        self.OperatorController = commands2.button.CommandXboxController(OP.operator_joystick_port)

        # Configure the button bindings
        self.configureButtonBindings()


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        self.OperatorController.leftBumper().whileTrue(inwardsShooter(self.shooter))
        self.OperatorController.leftBumper().whileFalse(stopShooter(self.shooter))
        
        self.OperatorController.rightBumper().whileTrue(outwardsShooter(self.shooter))
        self.OperatorController.rightBumper().whileFalse(stopShooter(self.shooter))
        
        self.OperatorController.button(2).whileTrue(outake(self.intake))
        self.OperatorController.button(2).whileFalse(stopIntake(self.intake))
        
        self.OperatorController.button(3).whileTrue(intake(self.intake))
        self.OperatorController.button(3).whileFalse(stopIntake(self.intake))
        
        self.arm.setDefaultCommand(commands.armCommand.ArmWithJoystick(self.arm))
        
        self.hang.setDefaultCommand(commands.hangCommand.HangCommand(self.hang))

    def getAutonomousCommand(self):
        return None