import wpilib
import commands2
import photonlibpy
import logging

logger = logging.getLogger("Vision")

from photonlibpy import estimatedRobotPose
from photonlibpy import multiTargetPNPResult
from photonlibpy.photonCamera import PhotonCamera
from photonlibpy.photonPipelineResult import PhotonPipelineResult
from photonlibpy import packet
from photonlibpy import photonPoseEstimator
from photonlibpy.photonTrackedTarget import PhotonTrackedTarget

from wpimath.geometry import Pose3d, Transform3d, Translation3d
from wpimath.units import metersToFeet, metersToInches

from constants import OP


class visionSub(commands2.Subsystem):
    
   def  __init__(self):
      
      # Start camera server 
      self.camera = PhotonCamera("Limelight")
      
      # gets latest result from camera
      self.result = self.camera.getLatestResult()
      
      # Checks if limelight detects targets
      self.hasTargets = self.result.hasTargets()
      
      # Recieves the latest targets seen by the limelight
      self.targets = self.result.getTargets()
      
      # April Tag Layout   (Currently empty/ not being used)
      self.aprilTagLayout = photonPoseEstimator.AprilTagFieldLayout()
      
      # # Position estimation strategy that is used by the PhotonPoseEstimator class
      self.PoseStrat = photonPoseEstimator.PoseStrategy.CLOSEST_TO_REFERENCE_POSE
      
      # This boolean is used to determine what pipeline to use by default it is true
      self.pipeLine = True
      self.pipeLineValue = 0
      
        
        
   def isDetecting(self, id: int) -> bool: # Check if desired april tag is beeing seen
      for i in self.targets:
         if i.getFiducialId() == id:
            return True
      return False

   def getTagOdometry(self, id: int): # Get the yaw, pitch, and skew value of desired target if seen  
      for i in self.targets:
         if i.getFiducialId() == id:
            return [i.getYaw(), i.getPitch(), i.getSkew()]
        
   def togglePipeLine(self, value):
      # Change PipleLine to desired one
      self.camera.setPipelineIndex(value)
            
   def captureImage(self):
      # Capture pre-process camera stream image
      self.camera.takeInputSnapshot()

      # Capture post-process camera stream image
      self.camera.takeOutputSnapshot()
   
   def nothingCommand(self):
        return False
   
    
   # Next 10 methods will return info about the target beeing seen
         
   def getTargetYaw(self, id: int) -> float: # Return the yaw of the desired target if seen
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getYaw()
          
   def getTargetPitch(self, id: int) -> float: # Return the yaw of the desired target if seen
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getPitch()
          
   def getTargetSkew(self, id: int) -> float: # Return the Skew of the desired target if seen
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getSkew()

   def GetTargetArea(self, id: int) -> float: # returns the percentage of area the target takes up on the camera
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getArea()
      return 0
          
   def getTargetID(self) -> tuple: # Return a list of tags beeing seen
      listId = ()
      for i in self.targets:
         listId += i.getFiducialId()
      return listId
    
   def getTargetDistance1(self, id: int): # Returns the X distance of the Desired ID Tag if seeen
      for i in self.targets:
         if i.getFiducialId() == id:
            distnace = i.getBestCameraToTarget().X()
         if (distnace is None):
            distnace = 0
         return distnace
    
   def getTargetDistance(self, id: int): # Returns the X distance of the Desired ID Tag if seeen
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getBestCameraToTarget().X()
    
   def getHeightDistance(self, id: int): # Returns the Y distance of the Desired ID Tag if seeen
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getBestCameraToTarget().Y()
    
   def getAllignmentDistance(self, id: int): # Returns the Z distance of the Desired ID Tag if seeen
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getBestCameraToTarget().Z()

   def GetTargetAmbiguity(self, id: int) -> float: # returns the ambiguity of the target
      for i in self.targets:
         if i.getFiducialId() == id:
            return i.getPoseAmbiguity()

   def GetTargetCorners(self, id: int) -> list: # returns the corners of desired target when seen
      corners = []
      for i in self.targets:
         corners = i.getDetectedCorners
      return corners
    
    
        
   def periodic(self) -> None:
        
      # Get most recent results and target data
      self.result = self.camera.getLatestResult()
      self.hasTargets = self.result.hasTargets()
      self.targets = self.result.getTargets()
      
      if (self.getTargetDistance(4) is None):
         self.distance = 0
      else:
         self.distance = metersToInches(float(self.getTargetDistance(4)))
         
      # Debug values by logging
      # logger.info(f"{self.getTargetDistance(4)} distance to speaker")
      # logger.info(f"{self.distance} distance to speaker")
      # logger.info(f"{self.distance} Yaw Value")
      
      # Display values on smart dashboard
      wpilib.SmartDashboard.putBoolean("Is April tag 4 detected", self.isDetecting(4))
      wpilib.SmartDashboard.putNumber("Tag size", self.GetTargetArea(4))
      wpilib.SmartDashboard.putNumber("Distance to speaker", self.distance)
      
      wpilib.SmartDashboard.putData(wpilib.Field2d())