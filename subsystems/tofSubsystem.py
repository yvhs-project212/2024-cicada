import wpilib
import rev
import commands2

import board
import time
import busio
import adafruit_vl6180x

# import digitalio
# import adafruit_vl53l4cd
# import adafruit_vl53l0x


class tofSUB(commands2.Subsystem):
    
    def  __init__(self):
        # Create I2C bus.
        i2c = busio.I2C(board.SCL, board.SDA)
        
        # Create sensor instance.
        sensor = adafruit_vl6180x.VL6180X(i2c)
        
        
        # Method 1 of using tof sensors with the I2C Port
        self.port = wpilib.I2C.Port.kOnboard
        self.device_Adress = 4
        
        self.device = wpilib.I2C(self.port, self.device_Adress)
        self.device.Port(0)