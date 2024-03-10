import wpilib
from wpimath.geometry import Translation2d, Rotation2d, Pose2d
from pathplannerlib.path import PathPlannerPath, PathConstraints, GoalEndState

from swervepy import u, SwerveDrive, TrajectoryFollowerParameters
import commands2
import math

import swervepy

class driveForwardCommand(commands2.Command):
    def __init__(self, swerveDrive: SwerveDrive):
        self.swerve = swerveDrive
        self.follower_params = TrajectoryFollowerParameters(
            max_drive_velocity=0.5 * (u.m / u.s),
            theta_kP=1,
            xy_kP=1,
        )

        bezier_points = PathPlannerPath.bezierFromPoses([
            Pose2d(1.0, 1.0, Rotation2d.fromDegrees(0)),
            Pose2d(3.0, 1.0, Rotation2d.fromDegrees(0)),
            #Pose2d(5.0, 3.0, Rotation2d.fromDegrees(90)),
        ])
        self.path = PathPlannerPath(
            bezier_points,
            PathConstraints(3.0, 3.0, 2 * math.pi, 4 * math.pi),
            GoalEndState(0.0, Rotation2d.fromDegrees(-90)),     # Zero velocity and facing 90 degrees clockwise
        )
        self.first_path = True  # reset robot pose to initial pose in trajectory
        self.open_loop = True
        
    def execute(self):
        self.swerve(self.path, self.follower_params, self.first_path, self.open_loop)