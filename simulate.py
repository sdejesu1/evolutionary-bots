import numpy
import random
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

back_amplitude = numpy.pi/8
back_frequency = 10
back_phaseOffset = numpy.pi

front_amplitude = numpy.pi/4
front_frequency = 10
front_phaseOffset = numpy.pi

# initializing variables
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
# init target angles to range [-pi/4, pi/4]
back_targetAngles = numpy.linspace(0, (2*numpy.pi), 1000)
#targetAngles = numpy.sin(targetAngles)
for i in range(0, 1000):
	back_targetAngles[i] = back_amplitude * numpy.sin(back_frequency * back_targetAngles[i] + back_phaseOffset)

front_targetAngles = numpy.linspace(0, (2*numpy.pi), 1000)
for i in range(0, 1000):
	front_targetAngles[i] = front_amplitude * numpy.sin(front_frequency * front_targetAngles[i] + front_phaseOffset)

numpy.save("data/back_targetAngles.npy", back_targetAngles)
numpy.save("data/front_targetAngles.npy", front_targetAngles)
#exit()


print(backLegSensorValues)
for i in range(0, 1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_BackLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=back_targetAngles[i],
		maxForce=100
	)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_FrontLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=front_targetAngles[i],
		maxForce=100
	)

	print(backLegSensorValues[i])
	print(frontLegSensorValues[i])
	print(i)
	t.sleep(1/1000)

numpy.save("data/backleg_sensor_vals.npy", backLegSensorValues)
numpy.save("data/frontleg_sensor_vals.npy", frontLegSensorValues)

p.disconnect()
