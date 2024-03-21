import wpilib
import commands2
import logging

logger = logging.getLogger("Led's")

class ledSub(commands2.Subsystem):
    
    def  __init__(self):
        
        # Creates a PWM channel for robot communication to arduino
        self.ledValue = wpilib.PWM(1)
        
    def ledMode1(self):
        self.ledValue.setSpeed(0.05)
        
    def ledMode2(self):
        self.ledValue.setSpeed(0.1)
        
    def ledMode3(self):
        self.ledValue.setSpeed(0.15)