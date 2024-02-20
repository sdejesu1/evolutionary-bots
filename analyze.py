import numpy
import matplotlib.pyplot as pyplot

backLegSensorValues = numpy.load("data/backleg_sensor_vals.npy")
frontLegSensorValues = numpy.load("data/frontleg_sensor_vals.npy")
#targetAngleValues = numpy.load("data/targetAngles.npy")
#print(targetAngleValues)
back_targetAngleValues = numpy.load("data/back_targetAngles.npy")
front_targetAngleValues = numpy.load("data/front_targetAngles.npy")
pyplot.plot(back_targetAngleValues, label="Back Target Angles", linewidth=3)
pyplot.plot(front_targetAngleValues, label="Front Target Angles", linewidth=3)
#pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=4)
#pyplot.plot(frontLegSensorValues, label="Front Leg")

pyplot.legend()
pyplot.show()
