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

for i in range(0,10):
	print("Box" + str(i+1))
	pyrosim.Send_Cube(name="Box" + str(i+1), pos=[x, y, z + i] , size=[length * (.9 ** (i+1)), width *(.9 ** (i+1)), height * (.9 ** (i+1))])


pyrosim.End()
