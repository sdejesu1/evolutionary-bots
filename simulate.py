import numpy
import random
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

amplitude = numpy.pi/4
frequency = 1
phaseOffset = 0

# initializing variables
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
# init target angles to range [-pi/4, pi/4]
targetAngles = numpy.linspace(0, (2*numpy.pi), 1000)
#targetAngles = numpy.sin(targetAngles)

# modifying construction of targetAngles
for i in range(0, 1000):
	targetAngles[i] = amplitude * numpy.sin(frequency * targetAngles[i] + phaseOffset)

numpy.save("data/targetAngles.npy", targetAngles)
exit()


print(targetAngles)
print(backLegSensorValues)
for i in range(0, 1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_BackLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=targetAngles[i],
		maxForce=200
	)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_FrontLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=targetAngles[i],
		maxForce=200
	)

	print(backLegSensorValues[i])
	print(frontLegSensorValues[i])
	print(i)
	t.sleep(1/70)

numpy.save("data/backleg_sensor_vals.npy", backLegSensorValues)
numpy.save("data/frontleg_sensor_vals.npy", frontLegSensorValues)

p.disconnect()
