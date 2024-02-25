import wpilib
import rev
import constants 
import commands2
import phoenix5

class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        # self.armmotor1 = phoenix5.WPI_TalonSRX(constants.ELEC.arm_motor1_CAN_ID)
        # self.armmotor2 = phoenix5.WPI_TalonSRX(constants.ELEC.arm_motor2_CAN_ID)
        self.armmotor1 = rev.CANSparkMax(constants.ELEC.arm_motor1_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2 = rev.CANSparkMax(constants.ELEC.arm_motor2_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        
        self.armmotor2.setInverted(True)
        self.motorgroup = wpilib.MotorControllerGroup(self.armmotor1, self.armmotor2)

    def armwithjoystick(self, joystickInput):
        speed = (joystickInput * 0.5)
        self.motorgroup.set(speed)
        #self.armmotor1.set(speed)

    def arm_down(self, speed):
        self.motorgroup.set(speed)

    def arm_up(self, speed):
        self.motorgroup.set(-speed)

    def arm_stop(self):
        self.motorgroup.set(0)        
