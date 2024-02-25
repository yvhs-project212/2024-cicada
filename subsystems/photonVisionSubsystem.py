import wpilib
import commands2

from photonlibpy import estimatedRobotPose
from photonlibpy import multiTargetPNPResult
from photonlibpy.photonCamera import PhotonCamera
from photonlibpy.photonPipelineResult import PhotonPipelineResult
from photonlibpy import packet
from photonlibpy import photonPoseEstimator
from photonlibpy.photonTrackedTarget import PhotonTrackedTarget

from constants import OP


class visionSub(commands2.Subsystem):
    
    # Dosen't initialize anything 
    def  __init__(self):
        
        # Start camera server 
        self.camera = PhotonCamera("limelight")
        
        
        
    def teleopPeriodic(self):
        
        self.camResult = self.camera.getLatestResult()
        self.pipeline = self.camResult.getTargets()
        
        self.fidicial_ids= [ i.getFiducialId() for i in self.pipeline ]
        
        wpilib.SmartDashboard.putNumberArray("April Tag ID", self.fidicial_ids)