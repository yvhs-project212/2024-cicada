import math
import logging

logger = logging.getLogger("project212_robot")
import wpilib
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
from pathplannerlib.path import PathPlannerPath, PathConstraints, GoalEndState
from pathplannerlib.auto import NamedCommands, AutoBuilder, PathPlannerAuto

from pathplannerlib.auto import AutoBuilder
from pathplannerlib.config import HolonomicPathFollowerConfig, ReplanningConfig, PIDConstants
from wpilib import DriverStation


from swervepy import u, SwerveDrive, TrajectoryFollowerParameters
from swervepy.impl import CoaxialSwerveModule

from constants import PHYS, MECH, ELEC, OP, SW
import subsystems.swerveComponents as swerveComponents
import commands2

import commands2.button


# Constants
import constants
from constants import OP, SW

# Subsystem Imports
import subsystems.shooterSubsystem
import subsystems.intakeSubsystem
import subsystems.armSubsystem
import subsystems.hangSubsystem
import subsystems.photonVisionSubsystem
import subsystems.armSubsystem
import subsystems.hangSubsystem
import subsystems.swerveSubsystem
import subsystems.ledsSubsystem

# Command Imports
from commands.shooterCommand import inwardsShooter, outwardsShooter, stopShooter
from commands.intakeCommand import intake, outake, stopIntake, IntakeLimitCommand
from commands.OuttakeCommand import outtakeCommand, stopBothIntakeAndShooter
from commands.intakeCommand import intake, outake, stopIntake
from commands.visionCommand import takeSnapShot, togglePipeline
from commands.armCommand import armStop, armToFloor, armToAmp, armWithAprilTag
from commands.ledCommand import ledMode1, ledMode2, ledMode3
import commands.armCommand
import commands.hangCommand


#Auto Command Imports
import commands.autonomousCommands.driveForwardCommand
import commands.autonomousCommands.autoShootingCommand
import commands.autonomousCommands.autoDropArmCommand
from commands.autonomousCommands import gyroZeroYawCommand, autoNotePositionAdjust, BlueTaxiAfterScoreFromRight, RedTaxiAfterScoreFromLeft, redBackToCommunityFromLeft
from commands.autonomousCommands import blueBackToCommunityFromRight
from commands.autonomousCommands import FourNotesAutoStepOneCommand, FourNotesAutoStepTwoCommand, FourNotesAutoStepThreeCommand, FourNotesAutoStepFourCommand, FourNotesAutoStepFiveCommand, FourNotesAutoStepSixCommand


class RobotContainer:

    def __init__(self):

        # The robot's subsystems
        self.shooter = subsystems.shooterSubsystem.shooterSubsystem()
        self.intake = subsystems.intakeSubsystem.intakeSubsystem()
        self.arm = subsystems.armSubsystem.ArmSubsystem()        
        self.hang = subsystems.hangSubsystem.HangSubsystem()
        self.Vision = subsystems.photonVisionSubsystem.visionSub()
        self.drivetrain = subsystems.swerveSubsystem.swerveSubsystem()
        self.leds = subsystems.ledsSubsystem.ledSub()
        self.swerve = self.drivetrain.getSwerve()

        # The driver's controller
        self.DriverController = commands2.button.CommandXboxController(OP.driver_controller)
        self.OperatorController = commands2.button.CommandXboxController(OP.operator_controller)  
        
        #Autos
        self.dropArmAndScore = commands2.SequentialCommandGroup(commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm), 
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter))
    
        self.oneNote = commands2.SequentialCommandGroup(commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm), 
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter))
        
        self.oneNoteShootOnly = commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter)
        
        self.blueOneNoteAndTaxiFromRight = commands2.SequentialCommandGroup(gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain),
                                                                commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm), 
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                                   BlueTaxiAfterScoreFromRight.getAutoCommand(self.swerve),
                                                                   gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain))
        
        self.blueTwoNoteAndTaxiFromRight = commands2.SequentialCommandGroup(gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain),
                                                                commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm), 
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                                commands2.ParallelDeadlineGroup(BlueTaxiAfterScoreFromRight.getAutoCommand(self.swerve), intake(self.intake)),
                                                                commands2.ParallelDeadlineGroup(blueBackToCommunityFromRight.getAutoCommand(self.swerve), autoNotePositionAdjust.autoNotePositionAdjust(self.intake, self.shooter)),
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                                )

        
        self.redOneNoteAndTaxiFromLeft = commands2.SequentialCommandGroup(gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain),
                                                                commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm), 
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                                   RedTaxiAfterScoreFromLeft.getAutoCommand(self.swerve),
                                                                   gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain))
        
        self.redTwoNoteAndTaxiFromLeft = commands2.SequentialCommandGroup(gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain),
                                                                commands.autonomousCommands.autoDropArmCommand.autoDropArmCommand(self.arm), 
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                                commands2.ParallelDeadlineGroup(RedTaxiAfterScoreFromLeft.getAutoCommand(self.swerve), intake(self.intake)),
                                                                commands2.ParallelDeadlineGroup(redBackToCommunityFromLeft.getAutoCommand(self.swerve), autoNotePositionAdjust.autoNotePositionAdjust(self.intake, self.shooter)),
                                                                commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                                )
        
        self.FourNotesAuto = commands2.SequentialCommandGroup(gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain),
                                                              self.oneNote,
                                                              commands2.ParallelDeadlineGroup(FourNotesAutoStepOneCommand.getAutoCommand(self.swerve), intake(self.intake)),
                                                              commands2.ParallelDeadlineGroup(FourNotesAutoStepTwoCommand.getAutoCommand(self.swerve), autoNotePositionAdjust.autoNotePositionAdjust(self.intake, self.shooter)),
                                                              commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                              commands2.ParallelDeadlineGroup(FourNotesAutoStepThreeCommand.getAutoCommand(self.swerve), intake(self.intake)),
                                                              commands2.ParallelDeadlineGroup(FourNotesAutoStepFourCommand.getAutoCommand(self.swerve), autoNotePositionAdjust.autoNotePositionAdjust(self.intake, self.shooter)),
                                                              commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                              commands2.ParallelDeadlineGroup(FourNotesAutoStepFiveCommand.getAutoCommand(self.swerve), intake(self.intake)),
                                                              commands2.ParallelDeadlineGroup(FourNotesAutoStepSixCommand.getAutoCommand(self.swerve), autoNotePositionAdjust.autoNotePositionAdjust(self.intake, self.shooter)),
                                                              commands.autonomousCommands.autoShootingCommand.shootingCommand(self.intake, self.shooter),
                                                              )
        
        self.autoChooser = wpilib.SendableChooser()
        self.autoChooser.setDefaultOption("DriveForward", commands.autonomousCommands.driveForwardCommand.getAutoCommand(self.swerve, 5.0))
        self.autoChooser.addOption("ScoreOneNote", self.dropArmAndScore)
        self.autoChooser.addOption("FourNotesAuto", self.FourNotesAuto)
        self.autoChooser.addOption("BlueScoreAndTaxiFromRight", self.blueOneNoteAndTaxiFromRight)
        self.autoChooser.addOption("BlueScoreOneAndPickUpFromMidFromRight", self.blueTwoNoteAndTaxiFromRight)
        self.autoChooser.addOption("RedScoreAndTaxiFromLeft", self.redOneNoteAndTaxiFromLeft)
        self.autoChooser.addOption("RedScoreOneAndPickUpFromMidFromLeft", self.redTwoNoteAndTaxiFromLeft)
        self.autoChooser.addOption("shootOnly", self.oneNoteShootOnly)
        
        NamedCommands.registerCommand("driveForward", commands.autonomousCommands.driveForwardCommand)
        
        wpilib.SmartDashboard.putData(self.autoChooser)
        
        self.configureButtonBindings()

    def get_autonomous_command(self):
        return self.autoChooser.getSelected()
        #return PathPlannerAuto("New Auto")

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        
        # self.OperatorController.button(1).whileTrue(IntakeLimitCommand(self.intake, self.leds))
        self.OperatorController.button(1).whileTrue(armToAmp(self.arm))
        self.OperatorController.button(1).whileFalse(armStop(self.arm))
        
        self.OperatorController.leftBumper().whileTrue(intake(self.intake))
        self.OperatorController.leftBumper().whileFalse(stopIntake(self.intake))
        
        self.OperatorController.rightBumper().whileTrue(outwardsShooter(self.shooter))
        self.OperatorController.rightBumper().whileFalse(stopShooter(self.shooter))
        
        # self.OperatorController.button(4).onTrue(autoNotePositionAdjust.autoNotePositionAdjust(self.intake, self.shooter))
        
        # self.OperatorController.button(2).whileTrue(outake(self.intake))
        # self.OperatorController.button(2).whileFalse(stopIntake(self.intake))
        self.OperatorController.button(2).whileTrue(outtakeCommand(self.intake, self.shooter))
        self.OperatorController.button(2).whileFalse(stopBothIntakeAndShooter(self.intake, self.shooter))
            
        self.DriverController.leftBumper().onTrue(gyroZeroYawCommand.gyroZeroYawCommand(self.drivetrain))
        
        # # self.OperatorController.button(4).whileTrue(ledMode2(self.leds))
        self.OperatorController.button(4).whileTrue(armToFloor(self.arm))
        self.OperatorController.button(4).whileFalse(armStop(self.arm))
        
        # # self.OperatorController.button(3).whileTrue(ledMode1(self.leds))
        self.OperatorController.button(3).whileTrue(armWithAprilTag(self.arm, self.Vision))
        self.OperatorController.button(3).whileFalse(armStop(self.arm))
        
        self.OperatorController.button(7).whileTrue(togglePipeline(self.Vision))
        
        self.OperatorController.button(8).toggleOnTrue(takeSnapShot(self.Vision))
        
        # self.arm.setDefaultCommand(commands.armCommand.ArmWithJoystick(self.arm, self.leds))
        
        self.hang.setDefaultCommand(commands.hangCommand.HangCommand(self.hang))
        
        self.swerve.setDefaultCommand(self.drivetrain.getSwerveTeleopCommand(self.swerve))