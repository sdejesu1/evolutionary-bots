import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR
from pyrosim.neuralNetwork import NEURAL_NETWORK



class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, stepIndex):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(stepIndex)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Act(self, stepIndex):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                print(neuronName, jointName, desiredAngle)
                self.motors[jointName.encode('ASCII')].Set_Value(desiredAngle, self)

        #for motor in self.motors:
            #self.motors[motor].Set_Value(desiredAngle, self)
