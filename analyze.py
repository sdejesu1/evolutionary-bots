import numpy
import matplotlib.pyplot as pyplot

backLegSensorValues = numpy.load("data/backleg_sensor_vals.npy")
print(backLegSensorValues)
pyplot.plot(backLegSensorValues)
pyplot.show()
