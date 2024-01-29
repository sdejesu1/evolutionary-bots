import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# size of box
length = 1
height = 1
width = 1

# position of box
x = 0
y = 0
z = 0.5

#pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
#pyrosim.Send_Cube(name="Box2", pos=[x, y, z + 1] , size=[length, width, height])


for idx_y in range(0, 5):
	y = idx_y
	for idx_x in range(0, 5):
		x = idx_x
		for idx_boxes in range(0,10):
        		pyrosim.Send_Cube(name="Box" + str(idx_boxes+1), pos=[x, y, z + idx_boxes] , size=[length * (.9 ** (idx_boxes+1)), width *(.9 ** (idx_boxes+1)), height * (.9 ** (idx_boxes+1))])


pyrosim.End()
