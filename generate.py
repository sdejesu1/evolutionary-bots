import pyrosim.pyrosim as pyrosim

# size of box
length = 1
height = 1
width = 1

# position of world box
world_x = 10
world_y = 10
world_z = 0.5


def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[world_x, world_y, world_z] , size=[length, width, height])
	pyrosim.End()


def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length, width, height])
	pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[length, width, height])
	pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[length, width, height])

	pyrosim.Send_Joint( name = "torso_backleg" , parent= "Torso" , child = "BackLeg" , type = "fixed", position = [0,-0.5,0.5])
	pyrosim.Send_Joint( name = "torso_frontleg" , parent= "Torso" , child = "FrontLeg" , type = "fixed", position = [0,0.5,0.5])
	pyrosim.End()


Create_World()
Create_Robot()
