import math
import logging

logger = logging.getLogger("project212_robot")

from constants import PHYS, MECH, ELEC, OP, SW
import commands2
import commands2.cmd
import commands2.button

# Constants
import constants
from constants import OP, SW

# Subsystem Imports
import Subsystems.shooterSubsystem
import Subsystems.intakeSubsystem
import Subsystems.armSubsystem
import Subsystems.hangSubsystem

# Command Imports
from Commands.shooterCommand import inwardsShooter, outwardsShooter, stopShooter
from Commands.intakeCommand import intake, outake, stopIntake
import Commands.armCommand
from Commands.hangCommand import Hang, Lower, StopHang


class RobotContainer:
    """
    This example robot container should serve as a demonstration for how to
    implement swervepy on your robot.  You should not need to edit much of the
    code in this module to get a test working.  Instead, edit the values and
    class choices in constants.py.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The robot's subsystems
        self.shooter = Subsystems.shooterSubsystem.shooterSubsystem()
        self.intake = Subsystems.intakeSubsystem.intakeSubsystem()
        self.arm = Subsystems.armSubsystem.ArmSubsystem()        
        self.hang = Subsystems.hangSubsystem.HangSubsystem()

        # The driver's controller
        self.stick = commands2.button.CommandXboxController(0)
        self.stick = commands2.button.CommandXboxController(1)

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
        self.stick.leftBumper().whileFalse(stopShooter(self.shooter))
        
        self.stick.rightBumper().whileTrue(outwardsShooter(self.shooter))
        self.stick.rightBumper().whileFalse(stopShooter(self.shooter))
        
        self.stick.button(2).whileTrue(outake(self.intake))
        self.stick.button(2).whileFalse(stopIntake(self.intake))
        
        self.stick.button(3).whileTrue(intake(self.intake))
        self.stick.button(3).whileFalse(stopIntake(self.intake))
        
        self.arm.setDefaultCommand(Commands.armCommand.ArmWithJoystick(self.arm))
        
        self.stick.leftTrigger().whileTrue(Lower(self.hang))
        self.stick.leftTrigger().whileFalse(StopHang(self.hang))
    
        self.stick.rightTrigger().whileTrue(Hang(self.hang))
        self.stick.rightTrigger().whileFalse(StopHang(self.hang))

    def getAutonomousCommand(self):
        return None