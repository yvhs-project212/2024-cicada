import wpilib
import commands2
import commands2.cmd

from Subsystems.intakeSubsystem import intakeSubsystem
from Subsystems.robotLEDsSubsystem import robotLEDsSubsystem

class intake(commands2.Command):
    
    def __init__(self, intakeSubsystem: intakeSubsystem, robotLEDsSubsystem: robotLEDsSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
        self.LED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("IntakeRunning")

    def execute(self):
        self.intakeSub.intake()
        self.LED.ledMode2()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.intakeSub.stopintake()
        
class outake(commands2.Command):
    
    def __init__(self, intakeSubsystem: intakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("OutakeRunning")

    def execute(self):
        self.intakeSub.outake()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.intakeSub.stopintake()
        
class stopIntake(commands2.Command):
    
    def __init__(self, intakeSubsystem: intakeSubsystem, robotLEDsSubsystem: robotLEDsSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
        self.LED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("IntakeStopped")

    def execute(self):
        self.intakeSub.stopintake()
        self.LED.ledMode3()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.intakeSub.stopintake()