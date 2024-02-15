import navx
import commands2
import wpilib

class GyroSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.NavXGyro = navx.AHRS(wpilib.SPI.Port.kMXP)

    def resetYaw(self) -> None:
        self.NavXGyro.zeroYaw()

    