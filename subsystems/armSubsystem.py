import wpilib
import rev
import wpilib.counter
import constants 
import commands2


import wpimath.controller
import wpimath.trajectory
import math
from subsystems.ledsSubsystem import ledSub

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
        
        
        # Set the position of encoders to 0
        self.encoder1.setPosition(0)
        self.encoder2.setPosition(0)
        
        self.armPID = wpimath.controller.PIDController(constants.SW.Arm_kP, constants.SW.Arm_kI, constants.SW.Arm_kD)
        self.armPID.setTolerance(2)
        
        self.pidUse1 = False
        self.pidUse2 = False
        # self.armPID.setIntegratorRange(-1.0, 1.0)
        # self.armPID.setSetpoint(3)
        # self.armPID.enableContinuousInput(-1, 1)
        # self.armPID.setIZone(1)
        
        # self.speed = 0
        
        self.controller = wpilib.XboxController(1)
        
    def periodic(self) -> None:
        self.avgArmPos = (self.encoder1.getPosition() + self.encoder2.getPosition())/2
        wpilib.SmartDashboard.putBoolean("BeamBreak", self.armLimitSwitch.get())
        wpilib.SmartDashboard.putBoolean("Arm PID at setpoint", self.armPID.atSetpoint())
        wpilib.SmartDashboard.putNumberArray("ArmPositions", [self.encoder1.getPosition(), self.encoder2.getPosition(), self.avgArmPos])
        
        wpilib.SmartDashboard.putNumber("PID Position error", self.armPID.getPositionError())
        wpilib.SmartDashboard.putNumber("PID Position error", self.armPID.getVelocityError())
        
        wpilib.SmartDashboard.putNumber("Arm speeds", self.motorgroup.get())
        wpilib.SmartDashboard.putNumber("motor 1 speeds", self.armmotor1.get())
        wpilib.SmartDashboard.putNumber("motor 2 speeds", self.armmotor2.get())
        
        # wpilib.SmartDashboard.putNumber("ArmSpeeds", self.speed)
        # wpilib.SmartDashboard.putNumber("tof Sensor Range in millimeters", self.tofSensor.getRange())
        
        
    def armwithjoystick(self, joystickInput):
        if joystickInput <= 0.15 and joystickInput >= -0.15:
            calculatedInput = 0
        else:
            calculatedInput = joystickInput
            
        # if (self.pidUse1 and self.pidUse2 == False):
        #     self.armPID.reset
            
        if self.armLimitSwitch.get():
            speed = (calculatedInput * constants.SW.ArmSpeed)
        else: 
            self.encoder1.setPosition(0)
            self.encoder2.setPosition(0)
            if calculatedInput > 0:
                speed = 0
            else:
                speed = (calculatedInput * constants.SW.ArmSpeed)
            
        self.motorgroup.set(speed)

    def arm_down(self, speed):
        # self.armPID = wpimath.controller.PIDController(0.02, 0, 0)
        self.motorgroup.set(speed)

    def arm_up(self, speed):
        # self.armPID = wpimath.controller.PIDController(0.02, 0, 0)
        self.motorgroup.set(-speed)
        
    def arm_stop(self):
        self.motorgroup.set(0)
        
    def armToAmp(self):
        # self.speed = (self.armPID.calculate(self.avgArmPos, -60.0))
        self.pidUse1 = True
        self.motorgroup.set(self.armPID.calculate(self.avgArmPos, -60.0))

    def armToFloor(self):
        # self.speed = (self.armPID.calculate(self.avgArmPos, 0.0))
        self.pidUse2 = True
        self.motorgroup.set(self.armPID.calculate(self.avgArmPos, 0.0))
        
    def resetPID (self):
        self.pidUse1 = False
        self.pidUse2 = False
        # self.armPID.reset()
        # self.armPID.setPID(0, 0, 0)
        self.motorgroup.set(0)
        self.armPID.disableContinuousInput()