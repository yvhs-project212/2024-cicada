import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from subsystems.hangSubsystem import HangSubsystem

import constants

import logging
logger = logging.getLogger("aniyah")


class HangCommand(commands2.Command):
    def __init__(self, hang_ss: HangSubsystem) -> None:
        super().__init__()
        self.hangSub = hang_ss
        self.addRequirements(hang_ss)
        self.opController = wpilib.XboxController(constants.OP.operator_joystick_port).getPOV

    def initialize(self):
        logger.info("running Hang command")

    def execute(self):
        self.hangSub.dPadControll(self.opController())

    def isFinished(self):
        # command does not finish it needs to be cancelled
        return False

    def end(self, interrupted: bool):
        self.hangSub.stop()