import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from subsystems.photonVisionSubsystem import visionSub

import constants

import logging
logger = logging.getLogger("Jhony")
        
class takeSnapShot(commands2.Command):
    def __init__(self, visionSubsystem: visionSub) -> None:
        super().__init__()
        self.vision_sub = visionSubsystem

    def initialize(self):
        logger.info("Capturing Image")

    def execute(self):
        self.vision_sub.captureImage()

    def isFinished(self):
        # command does not finish it needs to be cancelled
        return False

    def end(self, interrupted: bool):
        self.vision_sub.nothingCommand()
        
class togglePipeline(commands2.Command):
    def __init__(self, visionSubsystem: visionSub) -> None:
        super().__init__()
        self.vision_sub = visionSubsystem

    def initialize(self):
        logger.info("Changing Pipeline")

    def execute(self):
        self.vision_sub.togglePipeLine(1)

    def isFinished(self):
        # command does not finish it needs to be cancelled
        return False

    def end(self, interrupted: bool):
        self.vision_sub.nothingCommand()
        
class doNothing(commands2.Command):
    def __init__(self, visionSubsystem: visionSub) -> None:
        super().__init__()
        self.vision_sub = visionSubsystem

    def initialize(self):
        logger.info("Changing Pipeline")

    def execute(self):
        self.vision_sub.nothingCommand

    def isFinished(self):
        # command does not finish it needs to be cancelled
        return False

    def end(self, interrupted: bool):
        self.vision_sub.nothingCommand()