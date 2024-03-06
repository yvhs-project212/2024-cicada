import wpilib
import rev
import constants 
import commands2
import phoenix5
import playingwithfusion

class ArmSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        self.armmotor1 = rev.CANSparkMax(constants.ELEC.arm_motor1_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2 = rev.CANSparkMax(constants.ELEC.arm_motor2_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        # self.armmotor1 = rev.CANSparkMax(constants.ELEC.arm_motor1_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        # self.armmotor2 = rev.CANSparkMax(constants.ELEC.arm_motor2_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)
        self.armmotor2.setInverted(True)
        self.motorgroup = wpilib.MotorControllerGroup(self.armmotor1, self.armmotor2)
        
        self.tofSensor = playingwithfusion.TimeOfFlight(0) # Create a tofSensor Instance
        self.tofSensor.RangingMode(1) # Set the range to medium
        
        # Get both encoder values for the arm and later display them
        self.encoder1 = self.armmotor1.getEncoder()
        self.encoder2 = self.armmotor2.getEncoder()
        
        # Initialize PID controller for spark max
        self.pidArm1 = self.armmotor1.getPIDController()
        self.pidArm2 = self.armmotor2.getPIDController()
        
        # Set what type of sensor to use for PID
        # self.pidArm1.setFeedbackDevice()
        # self.pidArm2.setFeedbackDevice()
        
        # proportional speed constant
        self.kP = 0.0
        # integral speed constant
        self.kI = 0.0
        # derivative speed constant
        self.kD = 0.0
        # I Zone Constant
        self.kIz = 0.0
        # FeedForward Constant
        self.kFF = 0.0
        # Minimum and maximum output
        self.kMaxOutput = 1
        self.kMinOutput = -1
        
        # Set PID Constants for both motors
        self.pidArm1.setP(self.kP)
        self.pidArm2.setP(self.kP)
        self.pidArm1.setI(self.kI)
        self.pidArm2.setI(self.kI)
        self.pidArm1.setD(self.kD)
        self.pidArm2.setD(self.kD)
        self.pidArm1.setIZone(self.kIz)
        self.pidArm2.setIZone(self.kIz)
        self.pidArm1.setFF(self.kFF)
        self.pidArm2.setFF(self.kFF)
        self.pidArm1.setOutputRange(self.kMinOutput, self.kMaxOutput)
        self.pidArm2.setOutputRange(self.kMinOutput, self.kMaxOutput)
        
        # Display PID coefficients on SmartDashboard
        wpilib.SmartDashboard.putNumber("P Gain", self.kP)
        wpilib.SmartDashboard.putNumber("I Gain", self.kI)
        wpilib.SmartDashboard.putNumber("D Gain", self.kD)
        wpilib.SmartDashboard.putNumber("I Zone", self.kIz)
        wpilib.SmartDashboard.putNumber("Feed Forward", self.kFF)
        wpilib.SmartDashboard.putNumber("Max Output", self.kMaxOutput)
        wpilib.SmartDashboard.putNumber("Min Output", self.kMinOutput)
        wpilib.SmartDashboard.putNumber("Set Rotations", 0)
        
        
    def periodic(self) -> None:
        
        # Read PID coefficients from SmartDashboard
        p = wpilib.SmartDashboard.getNumber("P Gain", 0)
        i = wpilib.SmartDashboard.getNumber("I Gain", 0)
        d = wpilib.SmartDashboard.getNumber("D Gain", 0)
        iz = wpilib.SmartDashboard.getNumber("I Zone", 0)
        ff = wpilib.SmartDashboard.getNumber("Feed Forward", 0)
        max = wpilib.SmartDashboard.getNumber("Max Output", 0)
        min = wpilib.SmartDashboard.getNumber("Min Output", 0)
        rotations = wpilib.SmartDashboard.getNumber("Set Rotations", 0)
        
        # If PID coefficients on SmartDashboard have changed, write new values to controller
        if (p != self.kP): self.pidArm1.setP(p); self.pidArm2.setP(p); self.kP = p
        if (i != self.kI): self.pidArm1.setI(i); self.pidArm2.setI(i); self.kI = i
        if (d != self.kD): self.pidArm1.setD(d); self.pidArm2.setD(i); self.kD = d
        if (iz != self.kIz): self.pidArm1.setIZone(iz); self.pidArm2.setIZone(iz); self.kIz = iz
        if (i != self.kI): self.pidArm1.setFF(ff); self.pidArm2.setFF(ff); self.kFF = ff
        if ((max != self.kMaxOutput) and (min != self.kMinOutput)): 
            self.pidArm1.setOutputRange(min, max); self.pidArm2.setOutputRange(min, max); self.kMaxOutput = max; self.kMinOutput = min
            
        # Set desired arm position
        self.pidArm1.setReference(rotations, rev.CANSparkMax.ControlType.kPosition)
        self.pidArm2.setReference(rotations, rev.CANSparkMax.ControlType.kPosition)
        
        wpilib.SmartDashboard.putNumber("SetPoint", rotations)
        wpilib.SmartDashboard.putNumber("Motor 1 Position", self.encoder1.getPosition())
        wpilib.SmartDashboard.putNumber("Motor 2 position", self.encoder2.getPosition())
        wpilib.SmartDashboard.putNumber("tof Sensor Range in millimeters", self.tofSensor.getRange())
        
    def armwithjoystick(self, joystickInput):
        speed = (joystickInput * constants.SW.ArmSpeed)
        self.motorgroup.set(-speed)
        #self.armmotor1.set(speed)

    def arm_down(self, speed):
        self.motorgroup.set(speed)

    def arm_up(self, speed):
        self.motorgroup.set(-speed)

    def arm_stop(self):
        self.motorgroup.set(0)        
