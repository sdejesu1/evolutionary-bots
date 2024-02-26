import numpy
import random
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

import constants as c  # Import the constants file
from simulation import SIMULATION
"""
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# initializing variables
p.setGravity(0,0,-9.8)

#pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(c.NUM_SIMULATION_STEPS)
frontLegSensorValues = numpy.zeros(c.NUM_SIMULATION_STEPS)
# init target angles to range [-pi/4, pi/4]
back_targetAngles = numpy.linspace(0, (2*numpy.pi), c.NUM_SIMULATION_STEPS)
#targetAngles = numpy.sin(targetAngles)
for i in range(0, 1000):
	back_targetAngles[i] = c.BACK_AMPLITUDE * numpy.sin(c.BACK_FREQUENCY * back_targetAngles[i] + c.BACK_PHASE_OFFSET)

front_targetAngles = numpy.linspace(0, (2*numpy.pi), c.NUM_SIMULATION_STEPS)
for i in range(0, c.NUM_SIMULATION_STEPS):
	front_targetAngles[i] = c.FRONT_AMPLITUDE * numpy.sin(c.FRONT_FREQUENCY * front_targetAngles[i] + c.FRONT_PHASE_OFFSET)

numpy.save("data/back_targetAngles.npy", back_targetAngles)
numpy.save("data/front_targetAngles.npy", front_targetAngles)
#exit()


print(backLegSensorValues)
for i in range(0, c.NUM_SIMULATION_STEPS):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_BackLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=back_targetAngles[i],
		maxForce=c.MAX_MOTOR_FORCE
	)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_FrontLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=front_targetAngles[i],
		maxForce=c.MAX_MOTOR_FORCE
	)

	print(backLegSensorValues[i])
	print(frontLegSensorValues[i])
	print(i)
	t.sleep(1/1000)

numpy.save("data/backleg_sensor_vals.npy", backLegSensorValues)
numpy.save("data/frontleg_sensor_vals.npy", frontLegSensorValues)
"""
simulation = SIMULATION()
