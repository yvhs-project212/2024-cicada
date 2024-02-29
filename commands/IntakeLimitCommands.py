import wpilib
import rev
import commands2
import commands2.cmd

from subsystems.IntakeSubsystem import IntakeSubsystem
import constants
 
class IntakeLimitCommand(commands2.Command):
    
    def __init__(self, intakeSubsystem: IntakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("Intakie")

        
    def execute(self):
        self.intakeSub.intake()

    def isFinished(self):
        return self.intakeSub.limit_switch_get_none()
    
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake()

class StopIntakeLimit(commands2.Command):
    
    def __init__(self, intakeSubsystem: IntakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("stop Intakie")
        
    def execute(self):
        self.intakeSub.stopIntake()

    def isFinished(self):
        return False
     
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake()

class ReverseIntakeLimit(commands2.Command):
    
    def __init__(self, intakeSubsystem: IntakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("reverse intake")

    def execute(self):
        self.intakeSub.reverseIntake()

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake()

