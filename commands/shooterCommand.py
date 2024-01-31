#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import commands2.cmd

from Subsystems.shooterSubsystem import shooterSubsystem

class outwardsShooter(commands2.Command):
    
    def __init__(self, shooterSubsystem: shooterSubsystem) -> None:
        super().__init__()
        self.shooterSub = shooterSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("ShooterOutwards")

    def execute(self):
        self.shooterSub.outwardsShooter()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.shooterSub.stopShooter()


class inwardsShooter(commands2.Command):

    def __init__(self, shooterSubsystem: shooterSubsystem) -> None:
        super().__init__()
        self.shooterSub = shooterSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("ShooterInwards")

    def execute(self):
        self.shooterSub.inwardsShooter()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.shooterSub.stopShooter()


class stopShooter(commands2.Command):

    def __init__(self, shooterSubsystem: shooterSubsystem) -> None:
        super().__init__()
        self.shooterSub = shooterSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("ShooterStopped")
        
    def execute(self):
        self.shooterSub.stopShooter()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.shooterSub.stopShooter()