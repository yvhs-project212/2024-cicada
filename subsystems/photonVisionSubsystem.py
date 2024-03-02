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
from wpilib import shuffleboard

from wpimath.geometry import Pose3d, Transform3d, Translation3d

from constants import OP


class visionSub(commands2.Subsystem):
    
    # Dosen't initialize anything 
    def  __init__(self):
        
        # self.vision = visionSub
        self.board = shuffleboard.Shuffleboard
        
        self.aprilTags = (0,
                        "Blue Source Right",
                        "Blue Source Left",
                        "Red Speaker Right",
                        "Red Speaker Left",
                        "Red Amp",
                        "Blue Amp",
                        "Blue Speaker Right",
                        "Blue Speaker Left",
                        "Red Source Right",
                        "Red Source Left",
                        "Red Stage Left",
                        "Red Stage Middle",
                        "Red Stage Right",
                        "Blue Stage Left",
                        "Blue Stage Middle",
                        "Blue Stage Right"
      )
        
        # Start camera server 
        self.camera = PhotonCamera("limelight")
        
        # gets latest result from camera
        self.result = self.camera.getLatestResult()
        
        # Checks if limelight detects targets
        self.hasTargets = self.result.hasTargets()
        
        # Recieves the latest targets seen by the limelight
        self.targets = self.result.getTargets()
        
        # April Tag Layout   (Currently empty/ not being used)
        self.aprilTagLayout = photonPoseEstimator.AprilTagFieldLayout()
        
        # # Position estimation strategy that is used by the PhotonPoseEstimator class
        self.strat = photonPoseEstimator.PoseStrategy.CLOSEST_TO_REFERENCE_POSE
        
        if (len(self.targets) != 1):
            return
        
        self.trackedTarget = self.targets[0]
        self.pipeline = PhotonPipelineResult
        
        self.yaw = self.trackedTarget.getYaw()
        self.pitch = self.trackedTarget.getPitch()
        self.area = self.trackedTarget.getArea()
        self.skew = self.trackedTarget.getSkew()
        self.ambiguity = self.trackedTarget.getPoseAmbiguity()
        self.corners = self.trackedTarget.getDetectedCorners()
        self.pose = self.trackedTarget.getBestCameraToTarget()
        self.alternatePose = self.trackedTarget.getAlternateCameraToTarget()
        self.aprilTagID  = self.trackedTarget.getFiducialId()
        
        
    def isDetecting(self, id: int) -> bool:
      if len(self.targets) <= 0:
         pass
      for i in self.targets:
         if i == id:
            return True
      return False

    def getTagOdometry(self, id: int) -> tuple:
      if len(self.targets) <= 0:
         pass
      for i in self.targets:
         if i == id:
            return (i.getYaw(), i.getPitch(), i.getSkew())

    def getAllTags(self) -> tuple:
      if len(self.targets) <= 0 :
         pass
      listId = ()
      for i in self.targets:
         listId += i.getFiducialId()
      return listId
  
    def GetTagSize(self, id: int) -> float:
      if len(self.targets) <= 0 :
         pass
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getArea()
      return 10000
  
    def VideoTelemetry(self) -> None:
      if len(self.targets) <= 0 :
         pass
      self.board.addEventMarker("Tags", f"{self.getAllTags()}", shuffleboard.ShuffleboardEventImportance.kHigh)
      pass
        
    def togglePipeLine(self, pipelineValue):
        # Change PipleLine to desired one
        self.camera.setPipelineIndex(pipelineValue)
            
    def captureImage(self):
        # Capture pre-process camera stream image
        self.camera.takeInputSnapshot()

        # Capture post-process camera stream image
        self.camera.takeOutputSnapshot()
        
    def nothingCommand(self):
        return False
        
        
    def periodic(self) -> None:
        
        # self.fidicial_ids= [ i.getFiducialId() for i in self.trackedTarget ]s
        # wpilib.SmartDashboard.putNumberArray("April Tag ID's", self.fidicial_ids)
        
        
        # Display AprilTag ID's and a list of target info
        # wpilib.SmartDashboard.putNumber("Apri Tag Id", self.trackedTarget.getPitch())
        # wpilib.SmartDashboard.putNumberArray("Tags Detected", self.trackedTarget.getFiducialId)
        
        # wpilib.SmartDashboard.putNumberArray("Tags Detected", visionSub.getAllTags(self))
        
        # Get most recent results and target data
        # self.result = self.camera.getLatestResult()
        # self.targets = self.result.getTargets()
        
        wpilib.SmartDashboard.putBoolean("Is April tag 8 detected", self.isDetecting(8))
        wpilib.SmartDashboard.putNumber("Tag size", self.GetTagSize(8))
        