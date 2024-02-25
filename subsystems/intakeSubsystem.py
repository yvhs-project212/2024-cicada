import wpilib
import commands2
import phoenix5
import rev

from constants import ELEC

class intakeSubsystem(commands2.Subsystem):
    
    def  __init__(self):
        
        # initialize falcon 500 on intake and inverts it if necessary
        # self.intakeMotor = phoenix5.WPI_TalonFX(9)
        
        self.intakeMotor = rev.CANSparkMax(ELEC.intake_motor, rev.CANSparkMax.MotorType.kBrushless)
        self.intakeMotor.setInverted(True)
        
    def intake(self):
        self.intakeMotor.set(0.35)
        
    def outake(self):
        self.intakeMotor.set(-0.6)
        
    def stopintake(self):
        self.intakeMotor.set(0)