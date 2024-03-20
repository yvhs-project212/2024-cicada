import wpilib
import commands2
import commands2.cmd

from subsystems.intakeSubsystem import intakeSubsystem

class intake(commands2.Command):
    
    def __init__(self, intakeSubsystem: intakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("IntakeRunning")

    def execute(self):
        self.intakeSub.intake()

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
    
    def __init__(self, intakeSubsystem: intakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def initialize(self):
        import logging
        logger = logging.getLogger("jhony")
        logger.info("IntakeStopped")

    def execute(self):
        self.intakeSub.stopintake()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.intakeSub.stopintake()
        
class IntakeLimitCommand(commands2.Command):
    
    def __init__(self, intakeSubsystem: intakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("Intakie")

        
    def execute(self):
        self.intakeSub.intake()

    def isFinished(self):
        if self.intakeSub.limit_switch_get_none() == False:
            return True
        else:
            return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopintake()