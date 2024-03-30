import wpilib
import rev
import commands2

from constants import ELEC, SW

class shooterSubsystem(commands2.Subsystem):
    
    def  __init__(self):
        
        # initialize the 2 shooter motors and invert one motor
        self.shooterMotor1 = rev.CANSparkMax(ELEC.shooter_Motor1, rev.CANSparkMax.MotorType.kBrushless)
        self.shooterMotor2 = rev.CANSparkMax(ELEC.shooter_Motor2, rev.CANSparkMax.MotorType.kBrushless)
        self.shooterMotor1.setInverted(True)
        
        # create a controller instance and group the 2 shooter motors
        self.shooterMotorGroup = wpilib.MotorControllerGroup(self.shooterMotor1, self.shooterMotor2)
        
        # Creates an encoder constant for both shooter motors
        motor1Encoder = self.shooterMotor1.getEncoder()
        motor2Encoder = self.shooterMotor2.getEncoder()
        
        # RPM for both shooter wheels
        self.shooter1RPM = motor1Encoder.getVelocity()
        self.shooter2RPM = motor2Encoder.getVelocity()
        
    def periodic(self) -> None:
        wpilib.SmartDashboard.putNumber("Motor 12 RPM", self.shooter1RPM)
        wpilib.SmartDashboard.putNumber("Motor 13 RPM", self.shooter2RPM)
    
    def outwardsShooter(self):
        # self.shooterMotor1.set(-0.6)
        # self.shooterMotor2.set(-0.4)
        self.shooterMotorGroup.set(SW.OutwardsShooterSpeed)
        
    def inwardsShooter(self):
        self.shooterMotorGroup.set(SW.InwardsShooterSpeed)
        
    def stopShooter(self):
        self.shooterMotorGroup.set(0)