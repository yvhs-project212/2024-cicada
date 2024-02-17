import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from subsystems import hangSubsystem

import constants

import logging
logger = logging.getLogger("aniyah")


class Hang(commands2.Command):
    def __init__(self, hang_ss: hangSubsystem) -> None:
        super().__init__()
        self.hangSub = hang_ss

    def initialize(self):
        logger.info("running Hang command")

    def execute(self):
        self.hangSub.hang()

    def isFinished(self):
        # command does not finish it needs to be cancelled
        return False

    def end(self, interrupted: bool):
        self.hangSub.stop()
        


class Lower(commands2.Command):
    def __init__(self, hang_ss: hangSubsystem) -> None:
        super().__init__()
        self.hangSub = hang_ss

    def initialize(self):
        logger.info(" Running Lower Hang command")

    def execute(self):
        self.hangSub.lower()

    def isFinished(self):
        # The command needs to be cancelled in order to stop
        return False

    def end(self, interrupted: bool):
        self.hangSub.stop()


class StopHang(commands2.Command):
    def __init__(self, hang_ss: hangSubsystem) -> None:
        super().__init__()
        self.hangSub = hang_ss

    def initialize(self):
        logger.info("running StopMotor command")
               
    def execute(self):
        self.hangSub.stop()


    def isFinished(self):
        # The command needs to be cancelled in order to stop
        return False

    def end(self, interrupted: bool):
        self.hangSub.stop()