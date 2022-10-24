# Hack for importing files in directory. This is not exemplary, but there are better things to focus on.
import sys
sys.path.append('./src')

import solvers
import matplotlib.pyplot as plt
from numpy import sin, cos, array, trapz, arange, exp
import math

step = 0.01
t_max = 5
time_points = arange(0, t_max, step) # Create a list of all time values for which the function should be evaluated

values = solvers.euler(
    [2, 0], # Values at t0
    time_points,
    [ # Functions
        lambda t, data: 1*data[0] + 2*data[1],
        lambda t, data: -0.5*data[0] + 1*data[1]
    ]
)

fig, axes = plt.subplots(nrows=2, ncols=1)

analytic_sols = [
    2*(exp(time_points))*cos(time_points),
    -1*(exp(time_points))*sin(time_points)
]

for idx, sol in enumerate(values):
    axes[idx].plot(time_points, sol, color='hotpink') # Plot numeric solution

    analytic_sol = analytic_sols[idx] # Solution obtained using eigenvalue-eigenvector method.
    axes[idx].plot(time_points, analytic_sol, color='mediumblue') # Plot analytical solution

    axes[idx].fill_between(time_points, analytic_sol, sol, alpha=0.25, color='aqua') # Fill space between analytical and numeric solution

    diff = abs(sol-analytic_sol) # Difference between analytical and numeric solution. Absolute value to make integration easier
    axes[idx].plot(time_points, diff, color='green') # Plot difference
    axes[idx].fill_between(time_points, diff, color='green', alpha=0.25) # Fill space betwen x-axis and the difference

plt.show()

# total_error = trapz(diff, x=time_points) # Integrate the difference to calculate total error
# relative_error = total_error / t_max # Divide by t_max to caluculate relative error

# print(total_error, relative_error)