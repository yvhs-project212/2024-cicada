import wpilib
import rev
import constants 
import commands2

class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.armmotor1 = rev.CANSparkMax(constants.ELEC.arm_motor1_CAN_ID, rev.CANSparkMax.MotorType.kBrushed)
        self.armmotor2 = rev.CANSparkMax(constants.ELEC.arm_motor2_CAN_ID, rev.CANSparkMax.MotorType.kBrushed)
        self.armmotor2.setInverted(True)
        self.motorgroup = wpilib.MotorControllerGroup(self.armmotor1, self.armmotor2)

    def armwithjoystick(self, speed):
        self.motorgroup.set(speed * 0.3)

    def arm_down(self, speed):
        self.motorgroup.set(speed * 0.3)

    def arm_up(self, speed):
        self.motorgroup.set(-speed * 0.3)

    def arm_stop(self):
        self.motorgroup.set(0)        
