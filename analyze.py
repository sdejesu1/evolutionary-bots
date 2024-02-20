import numpy
import matplotlib.pyplot as pyplot

backLegSensorValues = numpy.load("data/backleg_sensor_vals.npy")
frontLegSensorValues = numpy.load("data/frontleg_sensor_vals.npy")
targetAngleValues = numpy.load("data/targetAngles.npy")
print(targetAngleValues)
pyplot.plot(targetAngleValues, label="Target Angles", linewidth=2)
#pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=4)
#pyplot.plot(frontLegSensorValues, label="Front Leg")

pyplot.legend()
pyplot.show()
