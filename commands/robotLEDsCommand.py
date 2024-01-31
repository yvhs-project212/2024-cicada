import wpilib
import commands2
import commands2.cmd

from Subsystems.robotLEDsSubsystem import robotLEDsSubsystem

class ledMode1(commands2.Command):
    
    def __init__(self, robotLEDsSubsystem: robotLEDsSubsystem) -> None:
        super().__init__()
        self.robotLED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("LEDMode1Running")

    def execute(self):
        self.robotLED.ledMode1()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.robotLED.ledMode3()
        
class ledMode2(commands2.Command):
    
    def __init__(self, robotLEDsSubsystem: robotLEDsSubsystem) -> None:
        super().__init__()
        self.robotLED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("LEDMode2Running")

    def execute(self):
        self.robotLED.ledMode2()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.robotLED.ledMode3()
        
class ledMode3(commands2.Command):
    
    def __init__(self, robotLEDsSubsystem: robotLEDsSubsystem) -> None:
        super().__init__()
        self.robotLED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("DefaultLEDModeRunning")

    def execute(self):
        self.robotLED.ledMode3()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.robotLED.ledMode3()