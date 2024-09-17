import wpilib
import rev
import wpilib.counter
import constants 
import commands2


import wpimath.controller
import wpimath.trajectory
import math
from wpilib import XboxController
from wpimath.units import metersToFeet, metersToInches

class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        
        self.armmotor1 = rev.CANSparkMax(constants.ELEC.arm_motor1_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2 = rev.CANSparkMax(constants.ELEC.arm_motor2_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2.setInverted(True)
        self.armLimitSwitch = wpilib.DigitalInput(constants.ELEC.arm_limit_switch)
        self.motorgroup = wpilib.MotorControllerGroup(self.armmotor1, self.armmotor2)
        
        # Get both encoder values for the arm
        self.encoder1 = self.armmotor1.getEncoder()
        self.encoder2 = self.armmotor2.getEncoder()
        
        self.armPID = wpimath.controller.PIDController(constants.SW.Arm_kP, constants.SW.Arm_kI, constants.SW.Arm_kD)
        self.armPID.setTolerance(1)
        
        self.joystick_override = False
        self.controller = XboxController(constants.op_data.operator_controller)
        
    def periodic(self) -> None:
        self.avgArmPos = (self.encoder1.getPosition() + self.encoder2.getPosition())/2
        wpilib.SmartDashboard.putBoolean("Arm LimitSwitch", self.armLimitSwitch.get())
        wpilib.SmartDashboard.putNumberArray("ArmPositions", [self.encoder1.getPosition(), self.encoder2.getPosition(), self.avgArmPos])
        wpilib.SmartDashboard.putNumber("Arm speeds", self.motorgroup.get())
        
        #  PID values to appear on SmartDashboard
        wpilib.SmartDashboard.putBoolean("Arm PID at setpoint", self.armPID.atSetpoint())
        wpilib.SmartDashboard.putNumber("Current PID setpoint", self.armPID.getSetpoint())
        wpilib.SmartDashboard.putNumberArray("PID position Error and Tolerance", [self.armPID.getPositionError(), self.armPID.getPositionTolerance()])
        
        if self.armLimitSwitch.get() == False:
            self.encoder1.setPosition(0)
            self.encoder2.setPosition(0)
        
    def armwithjoystick(self, joystickInput):
        if joystickInput <= 0.15 and joystickInput >= -0.15:
            calculatedInput = 0
        else:
            calculatedInput = joystickInput
            
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
        self.motorgroup.set(speed)

    def arm_up(self, speed):
        self.motorgroup.set(-speed)
        
    def arm_stop(self):
        self.motorgroup.set(0)
        
    def armToAmp(self):
        # Sets the desired enocder tick for the arm to be positioned at
        self.armPID.setSetpoint(-115.0)
        
        # self.motorgroup.set(self.armPID.calculate(self.avgArmPos, -115.0))

    def armToFloor(self):
        # Sets the desired enocder tick for the arm to be positioned at
        self.armPID.setSetpoint(0.0)
        
        # self.motorgroup.set(self.armPID.calculate(self.avgArmPos, 0.0))
        
    def armWithAprilTag(self, aprilTagDistance):
        if (aprilTagDistance is None):
            change = False
        else:
            change = True
            if change is True:
                distance = metersToInches(float(aprilTagDistance))
                if distance > 110:
                    self.setpoint = distance / 2.6
                elif distance > 90:
                    self.setpoint = distance / 3
                else:
                    self.setpoint = distance / 3.9
        # Sets the desired enocder tick for the arm to be positioned at
        self.armPID.setSetpoint(self.setpoint)
        
        # self.motorgroup.set(self.armPID.calculate(self.avgArmPos, -self.setpoint))
        
    def MainArmCommand(self, joystickInput):
        if self.controller.getYButton():
            self.armToAmp()
        elif self.controller.getAButton():
            self.armToFloor()
        elif self.controller.getXButton():
            self.armWithAprilTag()
            
        if abs(joystickInput) > 0.1:  # Threshold to ignore minor movements
            self.joystick_override = True
            self.motorgroup.set(joystickInput)
        else:
            self.joystick_override = False
            
        if not self.joystick_override:
            self.runPIDControl()
            
    def runPIDControl(self):
        # Get the current position of the arm from the encoder
        current_position = self.avgArmPos

        # Calculate output from PID controller
        pid_output = self.armPID.calculate(current_position)

        # Send the output to the motor
        self.motorgroup.set(pid_output)