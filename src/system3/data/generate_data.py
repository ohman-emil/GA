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

from numpy import linspace, cos, sin, arange

import methods
import solvers

step_lengths = [0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125, 0.0015625, 0.00078125]

t_max = 100
total_points=100
t0 = [1, 1] # Values at t0

funcs = [ # Functions
    lambda t, data: 7.8*data[0] + -9.6*data[1],
    lambda t, data: 7.3*data[0] + -7.8*data[1]
]

a = 1
b = -5/(2*sqrt(231))

values = []
error = []

for step in step_lengths:
    time_points = linspace(0, total_points*step, num=total_points) # Create a list of all time values for which the function should be evaluated

    analytic_sols = [ # Analytic solutions
        a*(
            (78/73)*cos(sqrt(231)/5*time_points)-
            ((2*sqrt(231))/73)*sin(sqrt(231)/5*time_points)
        )+
        b*(
            ((2*sqrt(231))/73)*cos(sqrt(231)/5*time_points)+
            (78/73)*sin(sqrt(231)/5*time_points)
        ),
        a*cos(sqrt(231)/5*time_points)+b*sin(sqrt(231)/5*time_points)
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
        methods.calculateError(step, temp_values, analytic_sols)
    )

with open('errors.csv', 'w') as doc:
    writer = csv.writer(doc) # Create a writer instance
    writer.writerow(['steplength', 'euler1', 'euler2', 'heun1', 'heun2'])
    ids = arange(0, len(error)) # Numpy list of integers from 0. Equal to the amount of functions
    writer.writerows(error) # Write csv data