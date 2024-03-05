from subsystems.drivetrainSubsystem import drivetrainSubsystem
import commands2
import logging
logger = logging.getLogger("leqili")

from swervepy.subsystem import SwerveDrive
from constants import SW

class drivetrainCommand(commands2.Command):
    def __init__(self, drivetrainSubsystem: drivetrainSubsystem) -> None:
        super().__init__()
        self.drivetrainSub = drivetrainSubsystem
        self.addRequirements(drivetrainSubsystem)
        
    def initialize(self):
        logger.info("drivetrain initiated")

        
    def execute(self):
        self.drivetrainSub.swerveDrive()
        
    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted: bool):
        logger.info("drivetrain stopped")