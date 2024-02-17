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

from constants import OP, SW
# Subsystem
import subsystems.intakesubsystem
# Commands
from commands.intakecommands import intake, outtake, stop

import phoenix5


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
        self.intake = subsystems.intakesubsystem.intake_ss()

        # The driver's controller
        self.stick = commands2.button.CommandXboxController(OP.driver_joystick_port)

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
        self.stick.leftBumper().whileTrue(intake(self.intake))
        self.stick.leftBumper().whileFalse(stop(self.intake))

        self.stick.rightBumper().whileTrue(outtake(self.intake))
        self.stick.rightBumper().whileFalse(stop(self.intake))


    def getAutonomousCommand(self):
        return None