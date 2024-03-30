import wpilib
import commands2
import commands2.cmd

from subsystems.ledsSubsystem import ledSub

class ledMode1(commands2.Command):
    
    def __init__(self, robotLEDsSubsystem: ledSub) -> None:
        super().__init__()
        self.robotLED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("LED'S")
        logger.info("Mode 1")

    def execute(self):
        self.robotLED.ledMode1()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.robotLED.ledMode3()
        
class ledMode2(commands2.Command):
    
    def __init__(self, robotLEDsSubsystem: ledSub) -> None:
        super().__init__()
        self.robotLED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("LED'S")
        logger.info("Mode 2")

    def execute(self):
        self.robotLED.ledMode2()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.robotLED.ledMode3()
        
class ledMode3(commands2.Command):
    
    def __init__(self, robotLEDsSubsystem: ledSub) -> None:
        super().__init__()
        self.robotLED = robotLEDsSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("LED'S")
        logger.info("Mode 3")

    def execute(self):
        self.robotLED.ledMode3()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.robotLED.ledMode3()