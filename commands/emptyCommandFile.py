# import wpilib
# import commands2
# import commands2.cmd
# import Subsystems.emptySubsystemFile

# from Subsystems.emptySubsystemFile import emptySub

# class emptySubCommand(commands2.Command):
    
#     def __init__(self, emptySubsystemFile: emptySub) -> None:
#         super().__init__()
#         self.emptySub = emptySubsystemFile

#     def initialize(self):
#         import logging
#         logger = logging.getLogger("jhony")
#         logger.info("emptySubRunning")

#     def execute(self):
#         self.emptySub.firstCommand

#     def isFinished(self):
#         return False

#     def end(self, interrupted: bool):
#         self.emptySub.endCommand()