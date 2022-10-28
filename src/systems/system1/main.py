# Hack for importing files in directory. This is not exemplary, but there are better things to focus on.
import sys
sys.path.append('./src')

import solvers
import methods
import matplotlib.pyplot as plt
from numpy import sin, cos, array, trapz, arange, concatenate
import csv

step = 0.01
t_max = 100
t0 = [] # Values at t0 ADD VALUES
time_points = arange(0, t_max, step) # Create a list of all time values for which the function should be evaluated

funcs = [ # Functions
    lambda t, data: # ADD FUNCTION
    lambda t, data: # ADD FUNCTION
]

analytic_sols = [
    
]

values = []
values.extend( # Add solution of Euler's method into list
    solvers.euler(
        t0,
        time_points,
        funcs
    )
)
values.extend( # Add solution of Heun's method into list
    solvers.heun(
        t0,
        time_points,
        funcs
    )
)

fig, axes = plt.subplots(nrows=(len(values)), ncols=1)

error = []

for idx, sol in enumerate(values):
    axes[idx].plot(time_points, sol, color='hotpink') # Plot numeric solution

    analytic_sol = analytic_sols[idx % len(analytic_sols)] # Solution obtained using eigenvalue-eigenvector method.
    axes[idx].plot(time_points, analytic_sol, color='mediumblue') # Plot analytical solution

    axes[idx].fill_between(time_points, analytic_sol, sol, alpha=0.25, color='aqua') # Fill space between analytical and numeric solution

    diff = abs(sol-analytic_sol) # Difference between analytical and numeric solution. Absolute value to make integration easier
    function_range = max(sol)-min(sol) # Calculate range of numeric solution. Used to make errors easier to compare.

    axes[idx].plot(time_points, diff, color='green') # Plot difference
    axes[idx].fill_between(time_points, diff, color='green', alpha=0.25) # Fill space betwen x-axis and the difference

    E_1 = trapz(diff, x=time_points) # Calculate E_1 using numerical integration
    E_2 = E_1/function_range
    E_3 = E_1/t_max
    E_4 = E_1/(function_range*t_max)
    error.append([E_1, E_2, E_3, E_4]) # Append a list of all 4 errors


with open('data.csv', 'w') as doc:
    writer = csv.writer(doc) # Create a writer instance
    writer.writerows(methods.generateCSVData(time_points, values)) # Write csv data with time points and values

with open('errors.csv', 'w') as doc:
    writer = csv.writer(doc) # Create a writer instance
    ids = arange(0, len(error)) # Numpy list of integers from 0. Equal to the amount of functions
    writer.writerows(methods.generateCSVData(ids, error)) # Write csv data with ids and error data

plt.show()