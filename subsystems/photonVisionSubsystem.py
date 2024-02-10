import wpilib
import commands2

from photonlibpy import estimatedRobotPose
from photonlibpy import multiTargetPNPResult
from photonlibpy import photonCamera
from photonlibpy import photonPipelineResult
from photonlibpy import packet
from photonlibpy import photonPoseEstimator
from photonlibpy import photonTrackedTarget


class visionSub(commands2.Subsystem):
    
    # Dosen't initialize anything 
    def  __init__(self):
        
        # Start camera server 
        self.camera = photonCamera.PhotonCamera("limelight") 
        self.camResult = self.camera.getLatestResult()
        # self.targets = photonPipelineResult.PhotonPipelineResult.getTargets()
        self.target = photonTrackedTarget.PhotonTrackedTarget
        
        # self.aprilTag = photonTrackedTarget.PhotonTrackedTarget.fiducialId
        self.aprilTagID = float(photonTrackedTarget.PhotonTrackedTarget.fiducialId)
        
        # initiate smartDashboard
        self.smartDashboard = wpilib.SmartDashboard 
        
        self.smartDashboard.putNumber("April Tag ID", self.aprilTagID)
        # self.smartDashboard.putNumberArray("X, Y, and Z Values for AprilTag", self.target.getBestCameraToTarget)
        # self.smartDashboard.putNumber("X, Y, and Z Values for AprilTag", self.target.getBestCameraToTarget)