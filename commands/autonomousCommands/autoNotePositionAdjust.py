import wpilib
import commands2

from subsystems.intakeSubsystem import intakeSubsystem
from subsystems.shooterSubsystem import shooterSubsystem
from constants import SW

class autoNotePositionAdjust(commands2.Command):
    def __init__(self, intakeSubsystem: intakeSubsystem, shooterSubsystem: shooterSubsystem) -> None:
        super().__init__()
        self.intakeSub = intakeSubsystem
        self.shooterSub = shooterSubsystem
        self.timer = wpilib.Timer()
        
    def initialize(self):
        self.timer.reset()
        self.timer.start()

    def execute(self):
        if self.timer.get() > SW.AutoNotePositionAdjustStartTiming:
            self.shooterSub.inwardsShooter()
            self.intakeSub.outake()

    def isFinished(self):
        if self.timer.get() > SW.AutoNotePositionAdjustStartTiming + 1:
            return True
        else: 
            return False

    def end(self, interrupted: bool):
        self.shooterSub.stopShooter()
        self.intakeSub.stopintake()