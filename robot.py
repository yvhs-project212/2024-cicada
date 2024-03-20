
#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import logging
log = logging.Logger('P212-robot')
import typing

import wpilib
import commands2
#import commands2.cmd

from wpilib.cameraserver import CameraServer

import robotcontainer


class Robot(commands2.TimedCommandRobot):
    """
    Command v2 robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you
    """

    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should be
        used for any initialization code.
        """
        self.autonomousCommand: typing.Optional[commands2.Command] = None

        # Instantiate our RobotContainer.  This will perform all our button
        # bindings, and put our autonomous chooser on the dashboard.
        self.container = robotcontainer.RobotContainer()
        self.container.swerve.reset_modules()         
        """
        Uses the CameraServer class to automatically capture video from a USB webcam and send it to the
        FRC dashboard without doing any vision processing. This is the easiest way to get camera images
        to the dashboard. Just add this to the robotInit() method in your program.
        """
        CameraServer().launch()

        log.info('robot initialized')

    def autonomousInit(self) -> None:
        """
        This method runs the autonomous command selected by your
        RobotContainer class.
        """
        self.autonomousCommand = self.container.get_autonomous_command()
        #self.autonomousCommand = self.container.getAutonomousCommand()

        # schedule the autonomous command (example)
        if self.autonomousCommand is not None:
            self.autonomousCommand.schedule()
        else:
            log.warning("no auto command?")

    def teleopInit(self) -> None:
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self) -> None:
        """This function is called periodically during operator control"""

    def testInit(self) -> None:
        # Cancels all running commands at the start of test mode
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(Robot)
