import wpilib
import commands2

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
        
        # Start camera server 
        self.camera = photonCamera.PhotonCamera("limelight") 
        self.camResult = self.camera.getLatestResult()
        # self.targets = photonPipelineResult.PhotonPipelineResult.getTargets()
        self.target = photonTrackedTarget.PhotonTrackedTarget
        
        
        
        # initiate smartDashboard
        self.smartDashboard = wpilib.SmartDashboard
        
        # self.smartDashboard.putNumberArray("X, Y, and Z Values for AprilTag", self.target.getBestCameraToTarget)
        # self.smartDashboard.putNumber("X, Y, and Z Values for AprilTag", self.target.getBestCameraToTarget)
        
        
        
    def pereodic(self):
        
        self.aprilTag = photonTrackedTarget.PhotonTrackedTarget.getFiducialId
        self.apriltagID = 0
        
        if self.aprilTag == 1:
            self.apriltagID = 1
        elif self.aprilTag == 2:
            self.apriltagID = 2
        elif self.aprilTag == 3:
            self.apriltagID = 3
        elif self.aprilTag == 4:
            self.apriltagID = 4
        elif self.aprilTag == 5:
            self.apriltagID = 5 
        elif self.aprilTag == 6:
            self.apriltagID = 6
        elif self.aprilTag == 7:
            self.apriltagID = 7
        elif self.aprilTag == 8:
            self.apriltagID = 8
        elif self.aprilTag == 9:
            self.apriltagID = 9
        elif self.aprilTag == 10:
            self.apriltagID = 10
        elif self.aprilTag == 11:
            self.apriltagID = 11
        elif self.aprilTag == 12:
            self.apriltagID = 12
        elif self.aprilTag == 13:
            self.apriltagID = 13
        
        
        self.smartDashboard.putNumber("April Tag ID", self.apriltagID)
        
    def nothing(self):
        self.apriltagID = 0