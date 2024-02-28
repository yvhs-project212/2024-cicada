import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from subsystems.photonVisionSubsystem import visionSub

import constants

import logging
logger = logging.getLogger("aniyah")


class VisionCommand(commands2.Command):
    def __init__(self, visionSubsystem: visionSub) -> None:
        super().__init__()
        self.vision_sub = visionSubsystem

    def initialize(self):
        logger.info("running Hang command")

    def execute(self):
        self.vision_sub.teleopPeriodic()

    def isFinished(self):
        # command does not finish it needs to be cancelled
        return False

    def end(self, interrupted: bool):
        self.vision_sub.teleopPeriodic()