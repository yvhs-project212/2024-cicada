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

# Subsystems
import subsystems.IntakeSubsystem
import subsystems.ShooterSubsystem


# Commands
from commands.IntakeCommands import IntakeCommand,StopIntake,ReverseIntake
from commands.ShooterCommands import StopShoot,ReverseShooter,ShootCommand

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
        self.Shootes = subsystems.ShooterSubsystem.ShooterSubsystem()
        self.intakes = subsystems.IntakeSubsystem.IntakeSubsystem()

        # The driver's controller
        self.stick = commands2.button.CommandXboxController(OP.operator_joystick_port)

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

        self.stick.a().whileTrue(IntakeCommand(self.intakes))
        self.stick.a().whileFalse(StopIntake(self.intakes))

        self.stick.y().whileTrue(ReverseIntake(self.intakes))
        self.stick.y().whileFalse(StopIntake(self.intakes))

        self.stick.rightBumper().whileTrue(ShootCommand(self.Shootes))
        self.stick.rightBumper().whileFalse(StopShoot(self.Shootes)) 
        
        self.stick.leftBumper().whileTrue(ReverseShooter(self.Shootes))
        self.stick.leftBumper().whileFalse(StopShoot(self.Shootes))

        
  
    def getAutonomousCommand(self):
        return None