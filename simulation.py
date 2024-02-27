import numpy
import random
import pybullet as p
import time as t
import pybullet_data
import constants as c
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(0, c.NUM_SIMULATION_STEPS):
            p.stepSimulation()
            self.robot.sense(i)
            """
    
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
            """
            print(i)
            t.sleep(1 / 1000)

        '''numpy.save("data/backleg_sensor_vals.npy", backLegSensorValues)
        numpy.save("data/frontleg_sensor_vals.npy", frontLegSensorValues)'''

    def __del__(self):
        p.disconnect()
