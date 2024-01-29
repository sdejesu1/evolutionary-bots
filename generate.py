import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

# size of box
length = 1
height = 3
width = 2

# position of box
x = 0
y = 0
z = 1.5
pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
pyrosim.End()
