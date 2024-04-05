import wpilib
import commands2
import logging

from constants import SW, ELEC

logger = logging.getLogger("Led's")

class ledSub(commands2.Subsystem):
    
    def  __init__(self):
        
        # Creates a PWM channel for robot communication to arduino
        self.ledValue = wpilib.PWM(ELEC.PWM_For_Leds)
        
        # Starts sending a pwm value to the arduino
        self.ledValue.setSpeed(0.01)
        
        # Sets LEDs red
    def ledMode1(self):
        self.ledValue.setSpeed(0.2)
        
        # Sets LED's green
    def ledMode2(self):
        self.ledValue.setSpeed(0.4)
        
        # Default Led Mode (Rainbow)
    def ledMode3(self):
        self.ledValue.setSpeed(0.5)