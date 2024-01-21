#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import commands2.cmd
import wpimath.controller

from subsystems.emoji_ss import EmojiSubsystem

import constants


class RotateEmojisLeft(commands2.Command):
    def __init__(self, emoji_ss: EmojiSubsystem) -> None:
        super().__init__()
        self.emoji_ss = emoji_ss
        self.timer = wpilib.Timer()
        self.timer.start()

    def execute(self):
        self.emoji_ss.rotate_left()

    def isFinished(self):
        # stop the motor after 2 seconds
        return self.timer.get() >= 2.0

    def cancel(self):
        self.emoji_ss.stop()


class RotateEmojisRight(commands2.Command):
    def __init__(self, emoji_ss: EmojiSubsystem) -> None:
        super().__init__()
        self.emoji_ss = emoji_ss
        self.timer = wpilib.Timer()
        self.timer.start()

    def execute(self):
        self.emoji_ss.rotate_right()

    def isFinished(self):
        # stop the motor after 2 seconds
        return self.timer.get() >= 2.0

    def cancel(self):
        self.emoji_ss.stop()
