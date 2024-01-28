#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import commands2.cmd
import wpimath.controller

import subsystems.armSubsystem

from subsystems.armSubsystem import armSubsystem

import constants


class RotateArmLeft(commands2.Command):
    """
    This imaginary robot has an "emoji subsystem" that displays different
    emojis.  A motor is used to rotate the display left (showing the previous
    emoji) or right (showing the next emoji).  Running the motor for exactly
    2.0 seconds shifts the display by one emoji.
    """
    def __init__(self, armSubsystem: armSubsystem) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        super().__init__()
        self.armSub = armSubsystem

    def initialize(self):
        """
        Perform any setup to initialize the command.
        This method runs when the scheduler schedules the command.
        """

    def execute(self):
        """
        Performs the main bulk of the command.
        This method runs 50 times a second while the command is active.
        """
        self.armSub.armMoveLeft()

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """

    def end(self, interrupted: bool):
        """
        Perform any cleanup or final steps needed after the command finishes.
        If you need to do something different depending on whether the command
        completed normally or was interrupted (by another command), the
        :interrupted: parameter will be True if the command was interrupted.
        """
        self.armSub.armStop()


class RotateArmRight(commands2.Command):
    """
    This imaginary robot has an "emoji subsystem" that displays different
    emojis.  A motor is used to rotate the display left (showing the previous
    emoji) or right (showing the next emoji).  Running the motor for exactly
    2.0 seconds shifts the display by one emoji.
    """
    def __init__(self, armSubsystem: armSubsystem) -> None:
        """
        Constructor for the command object.  Assigns some instance variables.
        """
        super().__init__()
        self.armSub = armSubsystem

    def initialize(self):
        """
        Perform any setup to initialize the command.
        This method runs when the scheduler schedules the command.
        """

    def execute(self):
        """
        Performs the main bulk of the command.
        This method runs 50 times a second while the command is active.
        """
        self.armSub.armMoveRight()

    def isFinished(self):
        """
        Returns a boolean indicating whether the command has completed.
        """

    def end(self, interrupted: bool):
        """
        Perform any cleanup or final steps needed after the command finishes.
        If you need to do something different depending on whether the command
        completed normally or was interrupted (by another command), the
        :interrupted: parameter will be True if the command was interrupted.
        """
        self.armSub.armStop()