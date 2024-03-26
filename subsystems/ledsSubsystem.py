import wpilib
import commands2
import logging

logger = logging.getLogger("Led's")

class ledSub(commands2.Subsystem):
    
    def  __init__(self):
        
        # Creates a PWM channel for robot communication to arduino
        self.ledValue = wpilib.PWM(1)
        
        # Starts sending a pwm value to the arduino
        self.ledValue.setSpeed(0.0001)
        
    def ledMode1(self):
        self.ledValue.setSpeed(0.1)
        
    def ledMode2(self):
        self.ledValue.setSpeed(0.3)
        
    def ledMode3(self): #Default Led Mode
        self.ledValue.setSpeed(0.5)