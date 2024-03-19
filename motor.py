import numpy as numpy
import constants as c
from pyrosim import pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = numpy.zeros(c.NUM_SIMULATION_STEPS)

    def Set_Value(self, desiredAngle, robot):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.MAX_MOTOR_FORCE
        )
