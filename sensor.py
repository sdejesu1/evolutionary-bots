import numpy as numpy
import constants as c
from pyrosim import pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.NUM_SIMULATION_STEPS)

    def Get_Value(self, stepIndex):
        self.values[stepIndex] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save("data/sensor_vals.npy", self.values)
