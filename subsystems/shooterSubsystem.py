import wpilib
import rev
import commands2

from constants import ELEC

class shooterSubsystem(commands2.Subsystem):
    
    def  __init__(self):
        
        # initialize the 2 shooter motors and invert one motor
        self.shooterMotor1 = rev.CANSparkMax(ELEC.arm_motor_1, rev.CANSparkMax.MotorType.kBrushless)
        self.shooterMotor2 = rev.CANSparkMax(ELEC.arm_motor_2, rev.CANSparkMax.MotorType.kBrushless)
        self.shooterMotor1.setInverted(True)
        
        # create a controller instance and group the 2 shooter motors
        self.shooterMotorGroup = wpilib.MotorControllerGroup(self.shooterMotor1, self.shooterMotor2)
        self.controller = wpilib.XboxController(0)
        
        self.liveWindow = wpilib.SmartDashboard
        self.liveWindow.putNumber("ShooterMotorOPT", 0)
    
    def outwardsShooter(self):
        self.shooterMotorGroup.set(-0.8)
        
    def inwardsShooter(self):
        self.shooterMotorGroup.set(1)
        
    def stopShooter(self):
        self.shooterMotorGroup.set(0)