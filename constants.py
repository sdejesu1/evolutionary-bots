import numpy as numpy

# Joint Control Parameters
BACK_AMPLITUDE = numpy.pi / 8
BACK_FREQUENCY = 10
BACK_PHASE_OFFSET = numpy.pi

FRONT_AMPLITUDE = numpy.pi / 4
FRONT_FREQUENCY = 10
FRONT_PHASE_OFFSET = numpy.pi

# Simulation Parameters
NUM_SIMULATION_STEPS = 1000
SIMULATION_TIME_STEP = 1 / 1000
MAX_MOTOR_FORCE = 100

# number of generations for hill climber
numberOfGenerations = 10
