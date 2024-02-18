import wpilib
import commands2

from wpimath.geometry import Pose3d, Transform3d, Translation3d, Rotation3d
from wpimath import geometry
import math 

from photonlibpy import estimatedRobotPose
from photonlibpy import multiTargetPNPResult
from photonlibpy import photonCamera
from photonlibpy import photonPipelineResult
from photonlibpy import packet
from photonlibpy import photonPoseEstimator
from photonlibpy import photonTrackedTarget

from constants import OP


class visionSub(commands2.Subsystem):
    
    # Dosen't initialize anything 
    def  __init__(self):
        
        # Tells photonVision the name of the camera being used
        self.camera = photonCamera.PhotonCamera("limelight") 
        self.camResult = self.camera.getLatestResult()
        self.target = photonTrackedTarget.PhotonTrackedTarget
        # self.targets = photonPipelineResult.PhotonPipelineResult.getTargets()
        
        
        
        
        # # Returns the april tag id that is beeing seen
        # # aprilTagFromLimelight = self.target.getFiducialId()
        # # Returns the X, Y, and Z Values from the April Tag in meters
        # aprilTagDistance = self.target.getBestCameraToTarget()
            
        # wpilib.SmartDashboard.putNumber("April Tag ID", self.apriltagID)
        
        # self.xyzValuesForAprilTags = Transform3d(aprilTagDistance, Rotation3d(0, 0, 0))
        # # self.apriltagID = 0
        
        # # if aprilTagFromLimelight in range (0, 16):
        # #     self.apriltagID = aprilTagFromLimelight
        
        # wpilib.SmartDashboard.putNumber("April Tag X Value in meters", self.xyzValuesForAprilTags.X())
        # wpilib.SmartDashboard.putNumber("April Tag Y Value in meters", self.xyzValuesForAprilTags.Y())
        # wpilib.SmartDashboard.putNumber("April Tag Z Value in meters", self.xyzValuesForAprilTags.Z())
        
        
    def teleopPeriodic(self):
        
        # Returns the april tag id that is beeing seen
        aprilTagFromLimelight = self.target.getFiducialId()
            
        wpilib.SmartDashboard.putNumber("April Tag ID", self.apriltagID)
        
        
        
        # Returns the X, Y, and Z Values from the April Tag in meters
        aprilTagDistance = self.target.getBestCameraToTarget()
        
        self.xyzValuesForAprilTags = Transform3d(aprilTagDistance, Rotation3d(0, 0, 0))
        self.apriltagID = 0
        
        if aprilTagFromLimelight in range (0, 16):
            self.apriltagID = aprilTagFromLimelight
            
        wpilib.SmartDashboard.putNumber("April Tag X Value in meters", self.xyzValuesForAprilTags.X())
        wpilib.SmartDashboard.putNumber("April Tag Y Value in meters", self.xyzValuesForAprilTags.Y())
        wpilib.SmartDashboard.putNumber("April Tag Z Value in meters", self.xyzValuesForAprilTags.Z())