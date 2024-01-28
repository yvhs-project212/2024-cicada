#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import commands2.cmd
import wpimath.controller

import Subsystems.armSubsystem

from Subsystems.armSubsystem import armSubsystem

import constants


class RotateArmLeft(commands2.Command):
    
    def __init__(self, armSubsystem: armSubsystem) -> None:
        super().__init__()
        self.armSub = armSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("armCommandRunning")

    def execute(self):
        self.armSub.armMoveLeft()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.armSub.armStop()


class RotateArmRight(commands2.Command):

    def __init__(self, armSubsystem: armSubsystem) -> None:
        super().__init__()
        self.armSub = armSubsystem

    def execute(self):
        """
        Performs the main bulk of the command.
        This method runs 50 times a second while the command is active.
        """
        self.armSub.armMoveRight()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.armSub.armStop()


class StopArm(commands2.Command):

    def __init__(self, armSubsystem: armSubsystem) -> None:
        super().__init__()
        self.armSub = armSubsystem
        
    def execute(self):
        self.armSub.armStop()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.armSub.armStop()