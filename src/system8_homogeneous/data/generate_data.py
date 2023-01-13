import sys

# Hack for importing files in directory. This is not exemplary, but there are better things to focus on.
try:
    sys.path.append('./src')
    import methods
    import solvers
except ModuleNotFoundError:
    sys.path.append('../..')
    import methods
    import solvers
except Exception as e:
    print(f'Module import error: {e}')

import csv
from math import sqrt

from numpy import arange, cos, sin, trapz

import methods
import solvers

step_lengths = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625]

t_max = 100
t0 = [1, 1] # Values at t0

funcs = [ # Functions
    lambda t, data: 6.9*data[0] + -9.5*data[1],
    lambda t, data: 8.2*data[0] + -6.9*data[1]
]

a = 1
b = sqrt(13/233)

values = []
error = []

for step in step_lengths:
    time_points = arange(0, t_max, step) # Create a list of all time values for which the function should be evaluated

    analytic_sols = [ # Analytic solutions
        a*(
            ((69/82)*cos((sqrt(3029)/10)*time_points))-
            ((sqrt(3029)/82)*sin((sqrt(3029)/10)*time_points))
        )+
        b*(
            ((sqrt(3029)/82)*cos((sqrt(3029)/10)*time_points)+
            (69/82)*sin((sqrt(3029)/10)*time_points))
        ),
        a*cos((sqrt(3029)/10)*time_points)+b*sin((sqrt(3029)/10)*time_points)
    ]

    temp_values = []
    temp_values.extend( # Add solution of Euler's method into list
        solvers.euler(
            t0,
            time_points,
            funcs
        )
    )
    temp_values.extend( # Add solution of Heun's method into list
        solvers.heun(
            t0,
            time_points,
            funcs
        )
    )
    
    values.append(temp_values)

    with open(f'step_{str(step).replace(".", "-")}.csv', 'w') as doc:
        writer = csv.writer(doc) # Create a writer instance
        writer.writerow(['t', 'euler1', 'euler2', 'heun1', 'heun2'])
        writer.writerows(methods.generateCSVData(time_points, temp_values)) # Write csv data with time points and values
    
    error.append(
        methods.calculateError(step, temp_values, analytic_sols, time_points)
    )

with open('errors.csv', 'w') as doc:
    writer = csv.writer(doc) # Create a writer instance
    writer.writerow(['steplength', 'euler1', 'euler2', 'heun1', 'heun2'])
    ids = arange(0, len(error)) # Numpy list of integers from 0. Equal to the amount of functions
    writer.writerows(error) # Write csv data