import wpilib
import commands2

from photonlibpy import photonCamera
from photonlibpy import packet
from photonlibpy import photonPipelineResult
from photonlibpy import photonPoseEstimator
from photonlibpy import photonTrackedTarget
from photonlibpy import multiTargetPNPResult
from photonlibpy import estimatedRobotPose

class VisionSubsystem(commands2.Subsystem):
    
    def  __init__(self):
        
        # Creates PhotonVision functions dosen't use them yet
        self.camera = photonCamera
        
        # self.camera.
        