import pyrosim.pyrosim as pyrosim
import random

# constants
# size of box
length = 1
height = 1
width = 1

# position of world box
world_x = 10
world_y = 10
world_z = 0.5


def Generate_Brain():
    # creating brain
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    '''
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=1.0)
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=1.0)
    #pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=12.0)
    '''
    # two nested loops: outside - sensor, inside - motor
    for i in range(0, 3):
        for j in range(3, 5):
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=random.randint(-1, 1))

    pyrosim.End()


def Generate_Body():
    # creating world
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[world_x, world_y, world_z], size=[length, width, height])
    pyrosim.End()

    # creating torso, and leg links
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.End()


Generate_Body()
Generate_Brain()
