# Hack for importing files in directory. This is not exemplary, but there are better things to focus on.
import sys
sys.path.append('./src')

import solvers
import matplotlib.pyplot as plt
from numpy import sin, cos, array, trapz, arange, concatenate

step = 0.01
t_max = 100
time_points = arange(0, t_max, step) # Create a list of all time values for which the function should be evaluated

values = []

values.extend( # Add solution of Euler's method into list
    solvers.euler(
        [2, 0], # Values at t0
        time_points,
        [ # Functions
            lambda t, data: 2*data[0] + 8*data[1],
            lambda t, data: -1*data[0] - 2*data[1]
        ]
    )
)

values.extend( # Add solution of Heun's method into list
    solvers.heun(
        [2, 0], # Values at t0
        time_points,
        [ # Functions
            lambda t, data: 2*data[0] + 8*data[1],
            lambda t, data: -1*data[0] - 2*data[1]
        ]
    )
)

fig, axes = plt.subplots(nrows=(len(values)), ncols=1)

analytic_sols = [
    2 * cos(2 * time_points) + 2 * sin(2 * time_points),
    -1 * sin(2 * time_points)
]

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

    calculated_error = trapz(diff, x=time_points)/function_range
    error.append(calculated_error)

    # WRITE A FILE IN /SRC/-DIRECTORY WHICH HANDLES ERROR QUANTIFICATIONS?

print(error)

plt.show()