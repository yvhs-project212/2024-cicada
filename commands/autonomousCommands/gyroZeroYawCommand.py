from subsystems.swerveSubsystem import swerveSubsystem
import commands2

class gyroZeroYawCommand(commands2.Command):
    def __init__(self, swerveSub: swerveSubsystem):
        self.swerveSub = swerveSub
        self.addRequirements(swerveSub)
        super().__init__()
        
    def isFinished(self) -> bool:
        return True
    
    def end(self, interrupted: bool):
        self.swerveSub.zeroGyroYaw()