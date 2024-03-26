import wpilib
import rev
import constants 
import commands2
import phoenix5
import playingwithfusion
from constants import SW, ELEC

class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        #super().__init__()
        
        self.beamBreak = wpilib.DigitalInput(8)
        
        self.armmotor1 = rev.CANSparkMax(ELEC.arm_motor1_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2 = rev.CANSparkMax(ELEC.arm_motor2_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2.setInverted(True)
        self.armLimitSwitch = wpilib.DigitalInput(constants.ELEC.arm_limit_switch)
        self.motorgroup = wpilib.MotorControllerGroup(self.armmotor1, self.armmotor2)
        
        # self.tofSensor = playingwithfusion.TimeOfFlight(0) # Create a tofSensor Instance
        # self.tofSensor.RangingMode(1) # Set the range to medium
        
        # Get both encoder values for the arm and later display them
        self.encoder1 = self.armmotor1.getEncoder()
        self.encoder2 = self.armmotor2.getEncoder()
        
        # Set the position of encoders to 0 and how often to check for position change
        self.encoder1.setPosition(0)
        self.encoder2.setPosition(0)
        self.encoder1.setMeasurementPeriod(8)
        self.encoder2.setMeasurementPeriod(8)
        
        # Initialize PID controller for spark max
        self.pidArm1 = self.armmotor1.getPIDController()
        self.pidArm2 = self.armmotor2.getPIDController()
        
        # Set what type of sensor to use for PID if not using neo hallsensor
        # self.pidArm1.setFeedbackDevice()
        # self.pidArm2.setFeedbackDevice()
        
        self.rotations = 0
        
        # Set PID Constants for both motors
        self.pidArm1.setP(SW.Arm_kP)
        self.pidArm2.setP(SW.Arm_kP)
        self.pidArm1.setI(SW.Arm_kI)
        self.pidArm2.setI(SW.Arm_kI)
        self.pidArm1.setD(SW.Arm_kD)
        self.pidArm2.setD(SW.Arm_kD)
        # self.pidArm1.setIZone(SW.Arm_kIz)
        # self.pidArm2.setIZone(SW.Arm_kIz)
        # self.pidArm1.setFF(SW.Arm_kFF)
        # self.pidArm2.setFF(SW.Arm_kFF)
        self.pidArm1.setOutputRange(SW.Arm_kMaxOutput, SW.Arm_kMinOutput)
        self.pidArm2.setOutputRange(SW.Arm_kMaxOutput, SW.Arm_kMinOutput)
        
        # Display PID coefficients on SmartDashboard
        wpilib.SmartDashboard.putNumber("P Gain", SW.Arm_kP)
        wpilib.SmartDashboard.putNumber("I Gain", SW.Arm_kI)
        wpilib.SmartDashboard.putNumber("D Gain", SW.Arm_kD)
        wpilib.SmartDashboard.putNumber("I Zone", SW.Arm_kIz)
        wpilib.SmartDashboard.putNumber("Feed Forward", SW.Arm_kFF)
        wpilib.SmartDashboard.putNumber("Max Output", SW.Arm_kMaxOutput)
        wpilib.SmartDashboard.putNumber("Min Output", SW.Arm_kMinOutput)
        wpilib.SmartDashboard.putNumber("Arm Set-Point", self.rotations)
        
        
    def periodic(self) -> None:
        
        wpilib.SmartDashboard.putNumber("Arm Set-Point", self.rotations)
        wpilib.SmartDashboard.putNumber("Motor 1 Position", self.encoder1.getPosition())
        wpilib.SmartDashboard.putNumber("Motor 2 position", self.encoder2.getPosition())
        wpilib.SmartDashboard.putBoolean("BeamBreak", self.beamBreak.get())
        # wpilib.SmartDashboard.putNumber("tof Sensor Range in millimeters", self.tofSensor.getRange())
        
        # if (wpilib.XboxController.getXButtonPressed):
        #     self.rotations = 60
        #     self.pidArm1.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        #     self.pidArm2.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
            
        # elif (wpilib.XboxController.getYButtonPressed):
        #     self.rotations = 0
        #     self.pidArm1.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        #     self.pidArm2.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        # else:
        #     self.motorgroup.set(0)
        #     # self.pidArm1.set
        #     # self.pidArm1.setReference(self.encoder1.getPosition, rev.CANSparkMax.ControlType.kPosition)
        #     # self.pidArm2.setReference(self.encoder2.getPosition, rev.CANSparkMax.ControlType.kPosition)
        # self.pidArm1.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        # self.pidArm2.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
            
        
        
    def armwithjoystick(self, joystickInput):
        if joystickInput <= 0.15 and joystickInput >= -0.15:
            calculatedInput = 0
        else:
            calculatedInput = joystickInput
            
        if self.armLimitSwitch.get():
            speed = (calculatedInput * constants.SW.ArmSpeed)
            # self.encoder1.setPosition(0)
            # self.encoder2.setPosition(0)
        else: 
            if calculatedInput > 0:
                speed = 0
            else:
                speed = (calculatedInput * constants.SW.ArmSpeed)
            
        #speed = (calculatedInput * constants.SW.ArmSpeed)
        self.motorgroup.set(speed)

    def arm_down(self, speed):
        self.motorgroup.set(speed)

    def arm_up(self, speed):
        self.motorgroup.set(-speed)
            
    def armToGround(self):  # Set desired arm position
        self.rotations = 0
        self.pidArm1.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        self.pidArm2.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        
    def armToAmp(self):
        self.rotations = -60  # VALUE NOT TESTED
        self.pidArm1.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        self.pidArm2.setReference(self.rotations, rev.CANSparkMax.ControlType.kPosition)
        
    def arm_stop(self):
        self.motorgroup.set(0)
