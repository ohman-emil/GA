# Hack for importing files in directory. This is not exemplary, but there are better things to focus on.
import sys
sys.path.append('./src')

import csv
from math import sqrt

import matplotlib.pyplot as plt
from numpy import arange, cos, sin

import solvers

step = 0.0125
t_max = 15
t0 = [1, 1] # Values at t0
time_points = arange(0, t_max, step) # Create a list of all time values for which the function should be evaluated

funcs = [ # Functions
    lambda t, data: 2.3*data[0] + 5.0*data[1] - 2.5,
    lambda t, data: -5.8*data[0] + -2.3*data[1] + 6.5
]

a = 2416/2371
b = -16/sqrt(2371)

analytic_sols = [ # Analytic solutions
    a*(
        ((-23/58)*cos(sqrt(2371)/10*time_points))-
        ((-sqrt(2371)/58)*sin(sqrt(2371)/10*time_points))
    )+
    b*(
        ((-sqrt(2371)/58)*cos(sqrt(2371)/10*time_points)+
        (-23/58)*sin(sqrt(2371)/10*time_points))
    )+(2675/2371),
    a*cos(sqrt(2371)/10*time_points)+b*sin(sqrt(2371)/10*time_points)+(-45/2371)
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

print([val[0] for val in analytic_sols])

fig, axes = plt.subplots(nrows=(len(values)), ncols=1)

for idx, sol in enumerate(values):
    axes[idx].plot(time_points, sol, color='hotpink') # Plot numeric solution

    analytic_sol = analytic_sols[idx % len(analytic_sols)] # Solution obtained using eigenvalue-eigenvector method.
    axes[idx].plot(time_points, analytic_sol, color='mediumblue') # Plot analytical solution

    axes[idx].fill_between(time_points, analytic_sol, sol, alpha=0.25, color='aqua') # Fill space between analytical and numeric solution

    diff = abs(sol-analytic_sol) # Difference between analytical and numeric solution. Absolute value to make integration easier
    function_range = max(sol)-min(sol) # Calculate range of numeric solution. Used to make errors easier to compare.

    axes[idx].plot(time_points, diff, color='green') # Plot difference
    axes[idx].fill_between(time_points, diff, color='green', alpha=0.25) # Fill space betwen x-axis and the difference


plt.savefig(f'diagram_step_{str(step).replace(".", "-")}.svg')
plt.show()