import navx
import commands2
import wpilib
from wpimath.geometry import Rotation2d

class GyroSubsystem(commands2.Subsystem):
    def __init__(self, invert: bool = False) -> None:
        super().__init__()
        self.NavXGyro = navx.AHRS.create_spi()
        self.invert = invert
        wpilib.SmartDashboard.putData("NavX", self)

    def resetYaw(self) -> None:
        self.NavXGyro.zeroYaw()

    def heading(self) -> Rotation2d:
        yaw = self.NavXGyro.getYaw()
        if self.invert:
            yaw = 360 - self.NavXGyro.getYaw()
        return Rotation2d.fromDegrees(yaw)

    