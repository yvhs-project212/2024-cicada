import commands2
from subsystems.armSubsystem import ArmSubsystem
import rev
from constants import SW
import wpilib

class autoDropArmCommand(commands2.Command):
    def __init__(self, armSub: ArmSubsystem) -> None:
        self.armSub = armSub
        self.timer = wpilib.Timer()
        
    def initialize(self):
        self.timer.reset()
        self.timer.start()
        coastMode = rev.CANSparkMax.IdleMode.kCoast
        self.armSub.armmotor1.setIdleMode(coastMode)
        self.armSub.armmotor2.setIdleMode(coastMode)
        
    def execute(self):
        self.armSub.arm_down(SW.StageOneAutoArmDownSpeed)
        if self.timer.get() >= SW.AutoArmDownStageTiming:
            self.armSub.arm_down(SW.StageTwoAutoArmDownSpeed)
        
        
    def isFinished(self) -> bool:
        if self.armSub.armLimitSwitch.get():
            return False
        else:
            return True
        
    def end(self, interrupted: bool):
        brakeMode = rev.CANSparkMax.IdleMode.kBrake
        self.armSub.armmotor1.setIdleMode(brakeMode)
        self.armSub.armmotor2.setIdleMode(brakeMode)
        self.armSub.arm_stop()