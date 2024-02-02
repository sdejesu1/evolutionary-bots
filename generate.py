import pyrosim.pyrosim as pyrosim

# size of box
length = 1
height = 1
width = 1

# position of world box
world_x = 2
world_y = 2
world_z = 0.5

# position of link0
link0_x = 0
link0_y = 0
link0_z = 0.5

# position of link1
link1_x = 0
link1_y = 0
link1_z = 0.5

# position of link2
link2_x = 0
link2_y = 0
link2_z = 0.5

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[world_x, world_y, world_z] , size=[length, width, height])
	pyrosim.End()


def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Link0", pos=[link0_x, link0_y, link0_z] , size=[length, width, height])
	pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
	pyrosim.Send_Cube(name="Link1", pos=[link1_x, link1_y, link1_z] , size=[length, width, height])
	pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
	pyrosim.Send_Cube(name="Link2", pos=[link2_x, link2_y, link2_z] , size=[length, width, height])
	pyrosim.End()


Create_World()
Create_Robot()
