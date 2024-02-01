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
import subsystems.intakeSubsystem


# Commands
from commands.intakeComs import IntakeCommand, ShootCommand,StopShoot,stopintake,reverseShooter,reverseintake

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
        self.intakes = subsystems.intakeSubsystem.MotorCommands() 


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

        self.stick.button(1).whileTrue(IntakeCommand(self.intakes))
        self.stick.button(1).whileFalse(stopintake(self.intakes))

        self.stick.rightBumper().whileTrue(ShootCommand(self.intakes))
        self.stick.rightBumper().whileFalse(StopShoot(self.intakes))
        
        self.stick.leftBumper().whileTrue(reverseShooter(self.intakes))
        self.stick.leftBumper().whileFalse(StopShoot(self.intakes))

        self.stick.button(4).whileTrue(reverseintake(self.intakes))
        self.stick.button(4).whileFalse(stopintake(self.intakes))



    def getAutonomousCommand(self):
        return None