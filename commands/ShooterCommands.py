import wpilib
import rev
import commands2
import commands2.cmd

from subsystems.ShooterSubsystem import ShooterSubsystem
import constants

class ShootCommand(commands2.Command):
    
    def __init__(self, ShooterSubsystem: ShooterSubsystem) -> None:
        super().__init__()
        self.ShooterSub = ShooterSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("Shootie")

    def execute(self):
        self.ShooterSub.shoot()

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.ShooterSub.stopShooter()

class ReverseShooter(commands2.Command):
    
    def __init__(self, ShooterSubsystem: ShooterSubsystem) -> None:
        super().__init__()
        self.ShooterSub = ShooterSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("reverse shooter")

    def execute(self):
        self.ShooterSub.reverseShooter()

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.ShooterSub.stopShooter()

class StopShoot(commands2.Command):
    
    def __init__(self, ShooterSubsystem: ShooterSubsystem) -> None:
        super().__init__()
        self.ShooterSub = ShooterSubsystem
    
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian campooos hernandez")
        logger.info("stop shooter")

    def execute(self):
        self.ShooterSub.stopShooter()

    def isFinished(self):
       return False
    
    def end(self, interrupted: bool):
        self.ShooterSub.stopShooter()