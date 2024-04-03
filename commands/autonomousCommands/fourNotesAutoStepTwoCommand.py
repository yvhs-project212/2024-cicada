import wpilib
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
from pathplannerlib.path import PathPlannerPath, PathConstraints, GoalEndState

from swervepy import u, SwerveDrive, TrajectoryFollowerParameters
import commands2
import math

import swervepy
def getAutoCommand(swerve: SwerveDrive):
    follower_params = TrajectoryFollowerParameters(
        max_drive_velocity=0.5 * (u.m / u.s),
        theta_kP=1,
        xy_kP=1,
    )

    path = PathPlannerPath.fromPathFile("4NotesStep2")
    
    first_path = False  # reset robot pose to initial pose in trajectory
    open_loop = True
    return swerve.follow_trajectory_command(path, follower_params, first_path, open_loop)