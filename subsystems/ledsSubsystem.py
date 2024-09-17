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
        
        # 
        self.robotDisabled = wpilib.DigitalOutput(9)
        
        # ctreLEDS = phoenix5.led
        # ctreLEDS.
        
        
    def disabledInit(self) -> None:
        self.robotDisabled.set(False)
        
    # def disabledPeriodic(self):
    #     self.ledMode2
        
    def periodic(self) -> None:
        self.robotDisabled.set(True)
    
        # Sets LEDs red
    def ledMode1(self):
        self.ledValue.setSpeed(0.1)
        self.robotDisabled.set(True)
        
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