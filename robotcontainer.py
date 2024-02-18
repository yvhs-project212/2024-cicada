#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpimath.controller
import commands2
import commands2.cmd
import commands2.button

# Constants
import constants
from constants import OP, SW

# Subsystem Imports
import Subsystems.shooterSubsystem
import Subsystems.robotLEDsSubsystem
import Subsystems.intakeSubsystem
import Subsystems.photonVisionSubsystem

# Command Imports
from Commands.robotLEDsCommand import ledMode1, ledMode2, ledMode3
from Commands.shooterCommand import inwardsShooter, outwardsShooter, stopShooter
from Commands.intakeCommand import intake, outake, stopIntake
from Commands.aprilTagCommand import getAprilTags


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.  Since
    Command-based is a "declarative" paradigm, very little robot logic should
    actually be handled in the :class:`.Robot` periodic methods (other than
    the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The robot's subsystems
        self.shooter = Subsystems.shooterSubsystem.shooterSubsystem()
        self.led = Subsystems.robotLEDsSubsystem.robotLEDsSubsystem()
        self.intake = Subsystems.intakeSubsystem.intakeSubsystem()
        self.Vision = Subsystems.photonVisionSubsystem.visionSub()

        # The driver's controller
        self.stick = commands2.button.CommandXboxController(OP.operator_joystick_port)


        # Configure the button bindings
        self.configureButtonBindings()


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        self.stick.leftBumper().whileTrue(inwardsShooter(self.shooter))
        self.stick.leftBumper().whileFalse(stopShooter(self.shooter, self.led))
        
        self.stick.rightBumper().whileTrue(outwardsShooter(self.shooter, self.led))
        self.stick.rightBumper().whileFalse(stopShooter(self.shooter, self.led))
        
        self.stick.button(2).whileTrue(outake(self.intake))
        self.stick.button(2).whileFalse(stopIntake(self.intake, self.led))
        
        self.stick.button(3).whileTrue(intake(self.intake, self.led))
        self.stick.button(3).whileFalse(stopIntake(self.intake, self.led))
        
        # self.stick.button(1).whileTrue(ledMode1(self.led))
        # self.stick.button(1).whileFalse(ledMode3(self.led))
        
        # self.stick.button(4).whileTrue(ledMode2(self.led))
        # self.stick.button(4).whileFalse(ledMode3(self.led))
        

    def getAutonomousCommand(self):
        return None