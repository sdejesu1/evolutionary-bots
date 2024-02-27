import numpy as numpy
import constants as c
from pyrosim import pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = numpy.zeros(c.NUM_SIMULATION_STEPS)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.BACK_AMPLITUDE
        self.frequency = c.BACK_FREQUENCY
        self.offset = c.BACK_PHASE_OFFSET
        # init target angles to range [-pi/4, pi/4]
        self.values = numpy.linspace(0, (2 * numpy.pi), c.NUM_SIMULATION_STEPS)
        if self.jointName == "b'Torso_FrontLeg'":
            self.frequency *= 0.5
        # targetAngles = numpy.sin(targetAngles)
        for i in range(0, c.NUM_SIMULATION_STEPS):
            self.values[i] = self.amplitude * numpy.sin(self.frequency * self.values[i] + self.offset)


    def Set_Value(self, stepIndex, robot):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.values[stepIndex],
            maxForce=c.MAX_MOTOR_FORCE
        )

    def Save_Values(self):
        numpy.save("data/motorValues.npy", self.values)