import wpilib
import commands2
import photonlibpy

from photonlibpy import estimatedRobotPose
from photonlibpy import multiTargetPNPResult
from photonlibpy.photonCamera import PhotonCamera
from photonlibpy.photonPipelineResult import PhotonPipelineResult
from photonlibpy import packet
from photonlibpy import photonPoseEstimator
from photonlibpy.photonTrackedTarget import PhotonTrackedTarget

from wpimath.geometry import Pose3d, Transform3d, Translation3d

from constants import OP


class visionSub(commands2.Subsystem):
    
    # Dosen't initialize anything 
    def  __init__(self):
        
        # Start camera server 
        self.camera = PhotonCamera("limelight")
        # gets latest result from camera
        self.result = self.camera.getLatestResult()
        # Checks if limelight detects targets
        self.hasTargets = self.result.hasTargets()
        # April Tag Layout
        self.aprilTagLayout = photonPoseEstimator.AprilTagFieldLayout()
        # # Position estimation strategy that is used by the PhotonPoseEstimator class
        self.strat = photonPoseEstimator.PoseStrategy.CLOSEST_TO_REFERENCE_POSE
        # A Transform3d value that tells the robot the distance from the center of the robot to the camera mount position
        # self.robotToCam = Transform3d(0, 0, 0, 0)
        # Pose Estimation
        # self.pose = photonPoseEstimator.PhotonPoseEstimator(self.aprilTagLayout, self.strat, self.camera, self.robotToCam)
        
        
        self.trackedTarget = PhotonTrackedTarget
        self.pipeline = PhotonPipelineResult
        
        # self.yaw = self.trackedTarget.getYaw()
        # self.pitch = self.trackedTarget.getPitch()
        # self.area = self.trackedTarget.getArea()
        # self.skew = self.trackedTarget.getSkew()
        # self.ambiguity = self.trackedTarget.getPoseAmbiguity()
        # self.pose = self.trackedTarget.getBestCameraToTarget()
        # self.corners = self.trackedTarget.getDetectedCorners()
        # self.alternatePose = self.trackedTarget.getAlternateCameraToTarget()
        # self.aprilTagID  = self.trackedTarget.getFiducialId()
        
        # Capture pre-process camera stream image
        self.camera.takeInputSnapshot()

        # Capture post-process camera stream image
        self.camera.takeOutputSnapshot()
        
        
    def togglePipeLine(self):
        if (self.camera.getPipelineIndex() == 0):
            self.camera.setPipelineIndex(1)
        else:
            self.camera.setPipelineIndex(0)
            
    def setDriverMode(self):
        if (self.camera.getDriverMode() == True):
            self.camera.setDriverMode(False)
        else:
            self.camera.setDriverMode(True)
        
        
        
    def teleopPeriodic(self):
        
        self.fidicial_ids= [ i.getFiducialId for i in self.trackedTarget ]
        
        wpilib.SmartDashboard.putNumberArray("April Tag ID's", self.fidicial_ids)
        # wpilib.SmartDashboard.putNumber("Apri Tag Id", self.aprilTagID)
        
        
        self.result = self.camera.getLatestResult()
        self.targets = self.result.getTargets()
        
        
        wpilib.SmartDashboard.putNumberArray("Target Info", self.targets)