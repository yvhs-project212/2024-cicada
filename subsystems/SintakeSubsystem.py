import wpilib
import rev
import phoenix5
import commands2

from constants import ELEC, OP

class SintakeSubsystem(commands2.Subsystem) :

    def __init__(self) -> None:
        super().__init__()
        self.intake_motor1 = phoenix5.WPI_TalonFX((ELEC.motor1_CAN_ID))
        #self.intake_motor1 = rev.CANSparkMax(2,rev.CANSparkMax.MotorType.kBrushless)
        self.shooter_motor2 = rev.CANSparkMax(ELEC.motor2_CAN_ID,rev.CANSparkMax.MotorType.kBrushless)
        self.shooter_motor3 = rev.CANSparkMax(ELEC.motor3_CAN_ID,rev.CANSparkMax.MotorType.kBrushless)
        self.shooter_motor2.setInverted(True)
        self.shootergroup = wpilib.MotorControllerGroup(self.shooter_motor2,self.shooter_motor3)
        self.CommandXboxController = wpilib.XboxController(OP.operator_joystick_port)

    def shoot(self) :
        self.shootergroup.set(-0.5)
        
    def reverseShooter(self) :

        self.shootergroup.set(0.5)

    def stopShooter(self) :
        
        self.shootergroup.set(0)

    def intake(self) :
        self.intake_motor1.set(-0.5)
    
    def reverseIntake(self) :
        
        self.intake_motor1.set(0.5)

    def stopIntake(self) :

        self.intake_motor1.set(0)
