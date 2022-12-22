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

step_lengths = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125]

t_max = 100
t0 = [1, 1] # Values at t0

funcs = [ # Functions
    lambda t, data: 2.3*data[0] + 5.0*data[1],
    lambda t, data: -5.8*data[0] + -2.3*data[1]
]

a = 1
b = -81/sqrt(2371)

values = []
error = []

for step in step_lengths:
    time_points = arange(0, t_max, step) # Create a list of all time values for which the function should be evaluated

    analytic_sols = [ # Analytic solutions
        a*(
            ((-23/58)*cos(sqrt(2371)/10*time_points))-
            ((-sqrt(2371)/58)*sin(sqrt(2371)/10*time_points))
        )+
        b*(
            ((-sqrt(2371)/58)*cos(sqrt(2371)/10*time_points)+
            (-23/58)*sin(sqrt(2371)/10*time_points))
        ),
        a*cos(sqrt(2371)/10*time_points)+b*sin(sqrt(2371)/10*time_points)
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
    
    temp_error = [step]
    for idx, sol in enumerate(temp_values):
        analytic_sol = analytic_sols[idx % len(analytic_sols)] # Solution obtained using eigenvalue-eigenvector method.

        diff = abs(sol-analytic_sol) # Difference between analytical and numeric solution. Absolute value to make integration easier
        function_range = max(sol)-min(sol) # Calculate range of numeric solution. Used to make errors easier to compare.

        temp_error.append(trapz(diff, x=time_points)/function_range)

    error.append(temp_error)

    values.append(temp_values)

    with open(f'step_{str(step).replace(".", "-")}.csv', 'w') as doc:
        writer = csv.writer(doc) # Create a writer instance
        writer.writerow(['t', 'euler1', 'euler2', 'heun1', 'heun2'])
        writer.writerows(methods.generateCSVData(time_points, temp_values)) # Write csv data with time points and values

with open('errors.csv', 'w') as doc:
    writer = csv.writer(doc) # Create a writer instance
    writer.writerow(['steplength', 'euler1', 'euler2', 'heun1', 'heun2'])
    ids = arange(0, len(error)) # Numpy list of integers from 0. Equal to the amount of functions
    writer.writerows(error) # Write csv data