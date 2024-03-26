import wpilib
import commands2
import logging

from constants import SW, ELEC

logger = logging.getLogger("Led's")

class ledSub(commands2.Subsystem):
    
    def  __init__(self):
        
        # Creates a PWM channel for robot communication to arduino
        self.ledValue = wpilib.PWM(ELEC.PWM_For_Leds)
        self.intakeLimitSwitch = wpilib.DigitalInput(ELEC.intake_limit_switch)
        
        # Starts sending a pwm value to the arduino
        self.ledValue.setSpeed(0.0001)
        
        # Sets LEDs green
    def ledMode1(self):
        self.ledValue.setSpeed(0.1)
        
        # Sets LED's red
    def ledMode2(self):
        self.ledValue.setSpeed(0.3)
        
        # Default Led Mode (Rainbow)
    def ledMode3(self):
        self.ledValue.setSpeed(0.5)
        
    def ledWithBeamBreak(self):
        if (self.intakeLimitSwitch):
            ledSub.ledMode1
        else:
            ledSub.ledMode2