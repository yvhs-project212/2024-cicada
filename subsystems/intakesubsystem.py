import wpilib
import rev
import commands2
from constants import ELEC
import phoenix5

class intake_ss(commands2.Subsystem):
        def __init__(self) -> bool:
            super().__init__()
            self.motor = rev.CANSparkMax(rev.CANSparkMax.MotorType.kBrushless)
            #self.motor = phoenix5.WPI_TalonSRX(ELEC.intake_CAN_ID)
            self.limitswitch = wpilib.DigitalInput(7)

        def intake(self):
            self.motor.set(0.3)

        def outtake(self):
             self.motor.set(-0.3)

        def stop(self):
             if self.limit_switch == 0:
                self.motor.set(0)
            
        def limit_switch(self) -> bool:
         if self.limitswitch():
             return False
         else:
             return True



    