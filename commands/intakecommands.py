import wpilib
import commands2
import commands2.cmd
from subsystems.intakesubsystem import intake_ss
import constants
import rev

class intake(commands2.Command):
     def __init__(self, intakesubsystem: intake_ss) -> None:
           super().__init__()
           self.intakesubsystem = intakesubsystem
    
     def initialize(self):
          import logging
          logger = logging.getLogger("gael obeso gutierrez")
          logger.info("intake")


     def execute(self):
           self.intakesubsystem.intake()

     def isFinished(self):
           return False
     
     def end(self, interrupted: bool):
           self.intakesubsystem.stop()

class outtake(commands2.Command):
     def __init__(self, intakesubsystem: intake_ss) -> None:
           super().__init__()
           self.intakesubsystem = intakesubsystem
    
     def initialize(self):
           import logging
           logger = logging.getLogger("gael obeso gutierrez")
           logger.info("outtake")

     def execute(self):
           self.intakesubsystem.outtake()

     def isFinished(self):
           return False
     
     def end(self, interrupted: bool):
           self.intakesubsystem.stop()

class stop(commands2.Command):
      def __init__(self, intakesubsystem: intake_ss) -> None:
            super().__init__()
            self.intakesubsystem = intakesubsystem
      
      def initialize(self):
            import logging
            logger = logging.getLogger("gael obeso gutierrez")
            logger.info("stop")

      def execute(self):
            self.intakesubsystem.stop()

      def isFinished(self):
            return False
      
      def end(self, interrupted: bool):
            self.intakesubsystem.stop()