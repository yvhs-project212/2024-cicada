import math
import wpilib
import commands2
import wpimath.kinematics
import wpimath.geometry
import wpimath.controller
import wpimath.trajectory
import rev
from constants import ELEC, SW, PHYS, MECH

class SwerveModule(commands2.Subsystem):
    def __init__(
        self, 
        driveMotorID: int, 
        turnMotorID: int, 
        driveMotorReversed: bool,
        turnMotorReversed: bool,
        turnMotorAbsoluteEncoderID: int,
        absoluteEncoderOffset: float,
        absoluteEncoderReversed: bool
        ) -> None:
        super().__init__()

        #Initiate motors
        self.driveMotor = rev.CANSparkMax(driveMotorID, rev.CANSparkMax.MotorType.kBrushless)
        self.turnMotor = rev.CANSparkMax(turnMotorID, rev.CANSparkMax.MotorType.kBrushless)

        #Initiate sensors
        self.turnMotorAbsoluteEncoder = wpilib.DutyCycleEncoder(turnMotorAbsoluteEncoderID)
        self.turningPIDController = wpimath.controller.ProfiledPIDController(
            SW.swerve_drive_turning_PID_controller_kP,
            SW.swerve_drive_turning_PID_controller_kI,
            SW.swerve_drive_turning_PID_controller_kD,
            wpimath.trajectory.TrapezoidProfile.Constraints()                        
        )

        self.driveIncrementalEncoder = self.driveMotor.getEncoder()
        self.turnIncrementalEncoder = self.turnMotor.getEncoder()

        self.driveIncrementalEncoder.setPositionConversionFactor(MECH.swerve_drive_driving_encoder_rotation2meter)
        self.driveIncrementalEncoder.setVelocityConversionFactor(MECH.swerve_drive_driving_encoder_rotation2meter_per_sec)
        self.turnIncrementalEncoder.setPositionConversionFactor(MECH.swerve_drive_turning_encoder_rotation2radian)
        self.turnIncrementalEncoder.setVelocityConversionFactor(MECH.swerve_drive_turning_encoder_rotation2radian_per_sec)
