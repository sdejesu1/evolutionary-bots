import random
import sys

import numpy
import pyrosim.pyrosim as pyrosim
import os


class SOLUTION:
    def __init__(self):
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        os.system("python3 simulate.py " + directOrGUI)
        # opening fitness.txt
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()
        #def Create_Brain():
        #def Create_Body():

    def Mutate(self):
        self.weights[random.randint(0, 2)][random.randint(0, 1)] = random.random() * 2 - 1

    def Create_World(self):
        # creating brain
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # two nested loops: outside - sensor, inside - motor
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
