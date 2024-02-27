import numpy
import random
import pybullet as p
import time as t
import pybullet_data
import constants as c
from world import WORLD
from robot import ROBOT
from motor import MOTOR


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
            self.robot.Act(i)

            print(i)
            t.sleep(1 / 30)

    def __del__(self):
        p.disconnect()
