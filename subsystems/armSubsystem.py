import wpilib
import rev
import constants 
import commands2
import phoenix5


import wpimath.controller
import wpimath.trajectory
import math

class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        
        self.armmotor1 = rev.CANSparkMax(constants.ELEC.arm_motor1_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2 = rev.CANSparkMax(constants.ELEC.arm_motor2_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2.setInverted(True)
        self.armLimitSwitch = wpilib.DigitalInput(constants.ELEC.arm_limit_switch)
        self.motorgroup = wpilib.MotorControllerGroup(self.armmotor1, self.armmotor2)
        
        # self.tofSensor = playingwithfusion.TimeOfFlight(0) # Create a tofSensor Instance
        # self.tofSensor.RangingMode(1) # Set the range to medium
        
        # Get both encoder values for the arm
        self.encoder1 = self.armmotor1.getEncoder()
        self.encoder2 = self.armmotor2.getEncoder()
        self.avgArmPos = (self.encoder1.getPosition() + self.encoder2.getPosition())/2
        
        # Set the position of encoders to 0
        self.encoder1.setPosition(0)
        self.encoder2.setPosition(0)
        
        # self.pid = wpimath.controller.ArmFeedforward(0.01, 1, 8, 3)
        # self.pid.calculate(25, 3, 1)
        self.armPID = wpimath.controller.PIDController(0.05, 0, 0)
        self.armPID.setTolerance(3, 0.05)
        self.armPos = self.armPID.setSetpoint(0)
        self.armPID.setIntegratorRange(-1, 1)
        # self.armPID.calculate()
        # self.armPID.enableContinuousInput(-1, 1)
        # self.armPID.setIZone(1)
        
    def periodic(self) -> None:
        wpilib.SmartDashboard.putBoolean("BeamBreak", self.armLimitSwitch.get())
        wpilib.SmartDashboard.putNumberArray("ArmPositions", [self.encoder1.getPosition(), self.encoder2.getPosition(), self.avgArmPos])
        # wpilib.SmartDashboard.putNumber("tof Sensor Range in millimeters", self.tofSensor.getRange())
        
    def armwithjoystick(self, joystickInput):
        if joystickInput <= 0.15 and joystickInput >= -0.15:
            calculatedInput = 0
        else:
            calculatedInput = joystickInput
            
        if self.armLimitSwitch.get():
            speed = (calculatedInput * constants.SW.ArmSpeed)
        else: 
            if calculatedInput > 0:
                speed = 0
                # self.encoder1.setPosition(0)
                # self.encoder2.setPosition(0)
            else:
                speed = (calculatedInput * constants.SW.ArmSpeed)
            
        self.motorgroup.set(speed)

    def arm_down(self, speed):
        self.motorgroup.set(speed)

    def arm_up(self, speed):
        self.motorgroup.set(-speed)
        
    def arm_stop(self):
        self.motorgroup.set(0)
