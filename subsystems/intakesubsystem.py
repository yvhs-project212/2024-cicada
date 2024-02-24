import wpilib
import rev
import commands2
from constants import ELEC
import phoenix5

class intake_ss(commands2.Subsystem):
        def __init__(self) -> None:
            super().__init__()
            self.motor = phoenix5.WPI_TalonSRX(ELEC.intake_CAN_ID)

        def intake(self):
            self.motor.set(0.3)

        def outtake(self):
             self.motor.set(-0.3)

        def stop(self):
             self.motor.set(0)
