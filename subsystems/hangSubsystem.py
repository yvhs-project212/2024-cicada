import wpilib
import commands2
import rev
from constants import ELEC, SW
'''import phoenix5'''




class HangSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.hangMotor1 = rev.CANSparkMax(ELEC.hang_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.hangMotor2 = rev.CANSparkMax(ELEC.lower_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)

        '''self.hangMotor1 = phoenix5.TalonSRX(ELEC.hang_motor_CAN_ID)
        self.hangMotor2 = phoenix5.VictorSPX(ELEC.lower_motor_CAN_ID)'''

        self.hangMotorGroup = wpilib.MotorControllerGroup(self.hangMotor1, self.hangMotor2)
        self.Controller = wpilib.XboxController(0)
        
        
    def dPadControll(self, joystick):
        if (joystick == 0):
            self.hangMotorGroup.set(-0.4)
        elif(joystick == 45):
            self.hangMotor2.set(0.4)
        elif(joystick == 135):
            self.hangMotor2.set(-0.4)
        elif(joystick == 180):
            self.hangMotorGroup.set(0.4)
        elif (joystick == 225):
            self.hangMotor1.set(0.4)
        elif(joystick == 315):
            self.hangMotor1.set(-0.4)
        else:
            self.hangMotor2.set(0)
            self.hangMotor1.set(0)
            
    # def leftMotorUp(self):
    #     self.hangMotor1.set(SW.HangMotorUp)
        
    # def leftMotorDown(self):
    #     self.hangMotor1.set(SW.HangMotorDown)

    def stop(self):
        self.hangMotorGroup.set(0)