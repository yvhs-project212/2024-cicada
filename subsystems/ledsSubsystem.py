import phoenix5.led
import wpilib
import commands2
import logging
import phoenix6
import phoenix5

from constants import SW, ELEC

logger = logging.getLogger("Led's")

class ledSub(commands2.Subsystem):
    
    def  __init__(self):
        
        # Creates a PWM channel for robot communication to arduino
        self.ledValue = wpilib.PWM(ELEC.PWM_For_Leds)
        
        # Starts sending a pwm value to the arduino
        self.ledValue.setSpeed(0.01)
        
        # ctreLEDS = phoenix5.led
        # ctreLEDS.
        
        # Sets LEDs red
        
    def disabledPeriodic(self):
        self.ledValue.setSpeed(0.01)
    
    def ledMode1(self):
        self.ledValue.setSpeed(0.1)
        
        # Sets LED's green
    def ledMode2(self):
        self.ledValue.setSpeed(0.4)
        
        # Default Led Mode (Rainbow)
    def ledMode3(self):
        self.ledValue.setSpeed(0.5)
        
        # Sets LEDs red
    def ledMode4(self):
        self.ledValue.setSpeed(0.2)
        
        # Sets LEDs red
    def ledMode5(self):
        self.ledValue.setSpeed(0.3)