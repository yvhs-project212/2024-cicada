import WpiLib
import rev
import commands2
import commands2.cmd

from subsystems.intakeSubsystem import MotorCommands

import constants

class IntakeCommand(commands2.Command):
    
    def __init__(self, intakeSubsystem: MotorCommands) -> None:
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
        self.intakeSub.stopintake

class ShootCommand(commands2.command):
    
    def __init__(self, intakeSubsystem: MotorCommands) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("shootie")

    def execute(self):
        self.intakeSub.shoot

    def isfinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopshooter

class StopShoot(commands2.command):
    
    def __init__(self, intakeSubsystem: MotorCommands) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("stop shootie")

    def execute(self):
        self.intakeSub.stopshooter

    def isfinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopshooter

class stopintake(commands2.Command):
    
    def __init__(self, intakeSubsystem: MotorCommands) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem

    def intialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("stop Intakie")

        
    def execute(self):
        self.intakeSub.stopintake

    def isfinished(self):
        return False
     
    def end(self, interrupted: bool):
        self.intakeSub.stopintake

class reverseShooter(commands2.command):
    
    def __init__(self, intakeSubsystem: MotorCommands) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("reverse shooter")

    def execute(self):
        self.intakeSub.reverseShooter

    def isfinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopshooter

class reverseintake(commands2.command):
    
    def __init__(self, intakeSubsystem: MotorCommands) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("reverse intake")

    def execute(self):
        self.intakeSub.reverseintake

    def isfinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.intakeSub.stopintake