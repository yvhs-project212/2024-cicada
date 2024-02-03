import wpilib
import rev
import commands2
import commands2.cmd

from subsystems.SintakeSubsystem import SintakeSubsystem
import constants

class IntakeCommand(commands2.Command):
    
    def __init__(self, intakeSubsystem: SintakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("Intakie")

        
    def execute(self):
        self.intakeSub.intake

    def isfinished(self):
        return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake


class StopIntake(commands2.Command):
    
    def __init__(self, intakeSubsystem: SintakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("stop Intakie")
        
    def execute(self):
        self.intakeSub.stopIntake

    def isfinished(self):
        return False
     
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake

class ReverseIntake(commands2.Command):
    
    def __init__(self, intakeSubsystem: SintakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("reverse intake")

    def execute(self):
        self.intakeSub.reverseIntake

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopIntake

class ShootCommand(commands2.Command):
    
    def __init__(self, intakeSubsystem: SintakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("Shootie")

    def execute(self):
        self.intakeSub.shoot

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopShooter

class ReverseShooter(commands2.Command):
    
    def __init__(self, intakeSubsystem: SintakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("reverse shooter")

    def execute(self):
        self.intakeSub.reverseShooter

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopShooter

class StopShoot(commands2.Command):
    
    def __init__(self, intakeSubsystem: SintakeSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("stop shooter")

    def execute(self):
        self.intakeSub.stopShooter

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopShooter