import wpilib
import commands2
import commands2.cmd

from subsystems.intakeSubsystem import intakeSubsystem
from subsystems.shooterSubsystem import shooterSubsystem

class outtakeCommand(commands2.Command):
    
    def __init__(self, intakeSubsystem: intakeSubsystem, shooterSubsystem: shooterSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
        self.shooterSub = shooterSubsystem
        
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian")
        logger.info("outtake")

    def execute(self):
        self.shooterSub.inwardsShooter()
        self.intakeSub.outake()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.shooterSub.stopShooter()
        self.intakeSub.stopintake()
        
class stopBothIntakeAndShooter(commands2.Command):
    def __init__(self, intakeSubsystem: intakeSubsystem, shooterSubsystem: shooterSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
        self.shooterSub = shooterSubsystem
        
    def initialize(self):
        import logging
        logger = logging.getLogger("fabian")
        logger.info("stopOuttake")

    def execute(self):
        self.shooterSub.stopShooter()
        self.intakeSub.stopintake()

    def isFinished(self):
        return False

    def end(self, interrupted: bool):
        self.shooterSub.stopShooter()
        self.intakeSub.stopintake()
        

        