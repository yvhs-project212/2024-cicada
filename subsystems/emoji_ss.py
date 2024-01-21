#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import rev
from constants import ELEC


class EmojiSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        """Creates a new EmojiSubsystem"""
        super().__init__()
        self.motor = rev.CANSparkMax(
            ELEC.emoji_motor_CAN_ID, rev.CANSparkMax.MotorType.kBrushless)

    def rotate_left(self):
        self.motor.set(-0.3)

    def rotate_right(self):
        self.motor.set(0.3)

    def stop(self):
        self.motor.set(0)
