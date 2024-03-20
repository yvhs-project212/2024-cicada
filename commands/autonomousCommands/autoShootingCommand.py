from subsystems.intakeSubsystem import intakeSubsystem
from subsystems.shooterSubsystem import shooterSubsystem
import wpilib
import commands2

class shootingCommand(commands2.Command):
    
    def __init__(self, intakeSub: intakeSubsystem, shooterSub: shooterSubsystem) -> None:
        self.intakeSub = intakeSub
        self.shooterSub = shooterSub
        self.timer = wpilib.Timer()
        
    def initialize(self):
        self.timer.reset()
        self.timer.start()
        
    def execute(self):
        self.shooterSub.outwardsShooter()
        if self.timer.get() > 0.5:
            self.intakeSub.intake()
            
    def isFinished(self) -> bool:
        if self.timer.get() > 1.5:
            return True
        else:
            return False
        
    def end(self, interrupted: bool):
        self.intakeSub.stopintake()
        self.shooterSub.stopShooter()
        