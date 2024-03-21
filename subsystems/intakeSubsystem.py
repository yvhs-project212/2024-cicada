import wpilib
import commands2
import phoenix5
import rev

from constants import ELEC, SW

class intakeSubsystem(commands2.Subsystem):
    
    def  __init__(self):
        
        self.intakeMotor = rev.CANSparkMax(ELEC.intake_motor, rev.CANSparkMax.MotorType.kBrushless)
        self.intakeMotor.setInverted(True)
        self.limitSwitch = wpilib.DigitalInput(ELEC.intake_limit_switch)
        
    def intake(self):
        self.intakeMotor.set(SW.IntakeSpeed)
        
    def outake(self):
        self.intakeMotor.set(SW.OutakeSpeed)
        
    def stopintake(self):
        self.intakeMotor.set(0)
        
    def limit_switch_get_none(self) -> bool:
        if self.limitSwitch.get():
            return True
        else:
            return False
        
    def intakeWithLimitSwitch(self):
        if self.limit_switch_get_none() == False:
            self.intakeMotor.set(SW.IntakeSpeed)
        elif self.limit_switch_get_none() == True:
            self.stopintake()
        
    def periodic(self) -> None:
        wpilib.SmartDashboard.putBoolean("LimitSwitchGetNone", self.limit_switch_get_none())
        wpilib.SmartDashboard.putBoolean("LimitSwitch", self.limitSwitch.get())