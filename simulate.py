import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for i in range(1, 1001):
	p.stepSimulation()
	print(i)
	t.sleep(1/70)

p.disconnect()
