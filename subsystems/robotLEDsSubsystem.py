import wpilib
import commands2


class robotLEDsSubsystem(commands2.Subsystem):
    
    def  __init__(self):
        
        # Creates a PWM channel for robot LED's
        self.ledValue = wpilib.PWM(1)
        
    def ledMode1(self):
        self.ledValue.setSpeed(0.5)
        
    def ledMode2(self):
        self.ledValue.setSpeed(0.3)
        
    def ledMode3(self):
        self.ledValue.setSpeed(0.1)