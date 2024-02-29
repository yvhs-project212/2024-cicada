import wpilib
import rev
import commands2
from subsystems.armSubsystem import ArmSubsystem
import constants

class ArmWithJoystick (commands2.Command):

    def __init__(self, armSubsystem: ArmSubsystem) -> None:
        super().__init__()
        self.armSubsystem = armSubsystem
        self.addRequirements(armSubsystem)
        self.joystickInput = wpilib.XboxController(constants.OP.operator_joystick_port).getLeftY
 
    def execute(self):
        self.armSubsystem.armwithjoystick(self.joystickInput())

    def isFinished(self):
        return False
    
    def end(self, interrupted: bool):
        self.armSubsystem.arm_stop()

