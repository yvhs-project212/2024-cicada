import wpilib
import commands2
import commands2.cmd
from Subsystems.photonVisionSubsystem import visionSub

class getAprilTags(commands2.Command):
    
    def __init__(self, visionSubsystem: visionSub) -> None:
        super().__init__()
        self.visionSub = visionSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("aprilTagsRunning")

    def execute(self):
        self.visionSub.getApriltags()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.visionSub.nothing()