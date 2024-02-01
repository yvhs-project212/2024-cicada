import wpilib
import rev
import phoenix5
import commands2

from constants import ELEC

class MotorCommands(commands2.subsystem) :

    def __init__(self) -> None:
        super().__init__()
        self.intake_motor1 = phoenix5.WPI_TalonFX((ELEC.motor1_CAN_ID))
        self.shooter_motor2 = rev.CANSparkMax(ELEC.motor2_CAN_ID,rev.CANSparkMax.MotorType.kBrushless)
        self.shooter_motor3 = rev.CANSparkMax(ELEC.motor3_CAN_ID,rev.CANSparkMax.MotorType.kBrushless)
        self.shooter_motor2.setInverted(True)
        self.shootergroup = wpilib.MotorControllerGroup(self.shooter_motor2,self.shooter_motor3)
        

    def intake(self) :
        self.intake_motor1.set(-0.5)
    
    def shoot(self) :
        self.shootergroup.set(0.5)

    def reverseShooter(self) :
        self.shootergroup.set(-0.5)
    
    def reverseintake(self) :
        self.intake_motor1.set(0.5)

    def stopintake(self) :
        self.intake_motor1.set(0)

    def stopshooter(self) :
        self.shootergroup.set(0)