import wpilib
import rev
import commands2
import commands2.cmd

from subsystems.IntakeSubsystem import IntakeSubsystem
import constants
 
class IntakeCommand(commands2.Command):
    
    def __init__(self, intakeSubsystem: IntakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("Intakie")

        
    def execute(self):
        self.intakeSub.intake(self)

    def isfinished(self):
        return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake()


class StopIntake(commands2.Command):
    
    def __init__(self, intakeSubsystem: IntakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("stop Intakie")
        
    def execute(self):
        self.intakeSub.stopIntake()

    def isfinished(self):
        return False
     
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake()

class ReverseIntake(commands2.Command):
    
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
