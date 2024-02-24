import wpilib
import rev
import phoenix5
import commands2

from constants import ELEC, OP

class IntakeSubsystem(commands2.Subsystem) :

    def __init__(self) -> None:
        super().__init__()

        self.intake_motor1 = phoenix5.WPI_TalonFX(ELEC.motor1_CAN_ID, 'rio')
        #self.intake_motor1 = rev.CANSparkMax(ELEC.motor1_CAN_ID,rev.CANSparkMax.MotorType.kBrushless)
        self.limit_switch = wpilib.DigitalInput(2)

    def intake(self):
        self.intake_motor1.set(-0.5)
    
    def reverseIntake(self):
        self.intake_motor1.set(0.5)

    def stopIntake(self):
        self.intake_motor1.set(0)
    
    def limit_switch_Get(self) -> bool:
        if self.limit_switch.get():
            return True
        else:
            return False
        