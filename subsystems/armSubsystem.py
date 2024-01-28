import wpilib
import rev
import commands2
import photonlibpy

from constants import ELEC
from photonlibpy.photonCamera import PhotonCamera

class armSubsystem(commands2.Subsystem):
    
    def robotInit(self):
        self.motor1 = rev.CANSparkMax(ELEC.arm_motor_1, rev.CANSparkMax.MotorType.kBrushless)
        self.motor1.setInverted(True)
        self.motor2 = rev.CANSparkMax(ELEC.arm_motor_2, rev.CANSparkMax.MotorType.kBrushless)
        self.armMotors = wpilib.MotorControllerGroup(self.motor1, self.motor2)
        self.controller = wpilib.XboxController(0)
        
        # PhotonVision functions
        self.pipeline = PhotonCamera.setPipelineIndex(self, 1)
        
        # set pwm signal
        self.ledValue = wpilib.PWM
        self.ledValue.setPulseTime(self, 1000000)
        
    def teleopPeriodic(self):
        "nothing"
    
    def armMoveLeft(self):
        self.armMotors.set(0.2)
        
    def armMoveRight(self):
        self.armMotors.set(-0.2)
        
    def armStop(self):
        self.armMotors.set(0)
            
if __name__ == "__main__":
    wpilib.run(armSubsystem)