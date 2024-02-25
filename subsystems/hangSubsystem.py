import wpilib
import commands2
import rev
from constants import ELEC
'''import phoenix5'''




class HangSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.hangMotor1 = rev.CANSparkMax(ELEC.hang_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.hangMotor2 = rev.CANSparkMax(ELEC.lower_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushed)

        '''self.hangMotor1 = phoenix5.TalonSRX(ELEC.hang_motor_CAN_ID)
        self.hangMotor2 = phoenix5.VictorSPX(ELEC.lower_motor_CAN_ID)'''

        self.hangMotorGroup = wpilib.MotorControllerGroup(self.hangMotor1)
        

        
    def hang(self):
        self.hangMotorGroup.set(-0.4)

    
    def lower(self):
        self.hangMotorGroup.set(0.4)

    
    def stop(self):
        self.hangMotorGroup.set(0)
