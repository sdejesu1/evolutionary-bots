import numpy
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
print(backLegSensorValues)
for i in range(0, 1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_BackLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=-numpy.pi/4,
		maxForce=100
	)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId,
		jointName=b'Torso_FrontLeg',
		controlMode=p.POSITION_CONTROL,
		targetPosition=numpy.pi/4,
		maxForce=100
	)

	print(backLegSensorValues[i])
	print(frontLegSensorValues[i])
	print(i)
	t.sleep(1/70)

numpy.save("data/backleg_sensor_vals.npy", backLegSensorValues)
numpy.save("data/frontleg_sensor_vals.npy", frontLegSensorValues)

p.disconnect()
