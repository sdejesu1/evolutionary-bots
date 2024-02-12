import numpy
import matplotlib.pyplot as pyplot

backLegSensorValues = numpy.load("data/backleg_sensor_vals.npy")
frontLegSensorValues = numpy.load("data/frontleg_sensor_vals.npy")
print(backLegSensorValues)
print(frontLegSensorValues)
pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=4)
pyplot.plot(frontLegSensorValues, label="Front Leg")

pyplot.legend()
pyplot.show()
