# Hack for importing files in solvers directory. This is not exemplary, but there are better things to focus on.
import sys
sys.path.append('./src/solvers')
import numpy as np

import euler
import matplotlib.pyplot as plt
from numpy import sin, cos, array, trapz

step = 0.01
t_max = 15
time_points = np.arange(0, t_max, step) # Create a list of all time values for which the function should be evaluated

values = euler.solve(
    [2, 0], # Values at t0
    time_points,
    [ # Functions
        lambda t, data: 2*data[0] + 8*data[1],
        lambda t, data: -1*data[0] - 2*data[1]
    ]
)

plt.plot(time_points, values[0], color='hotpink') # Plot numeric solution

analytic_sol = 2 * cos(2 * time_points) + 2 * sin(2 * time_points) # Solution obtained using eigenvalue-eigenvector method.
plt.plot(time_points, analytic_sol, color='mediumblue') # Plot analytical solution

plt.fill_between(time_points, analytic_sol, values[0], alpha=0.25, color='aqua') # Fill space between analytical and numeric solution

diff = abs(values[0]-analytic_sol) # Difference between analytical and numeric solution. Absolute value to make integration easier
plt.plot(time_points, diff, color='green') # Plot difference
plt.fill_between(time_points, diff, color='green', alpha=0.25) # Fill space betwen x-axis and the difference

total_error = trapz(diff, x=time_points) # Integrate the difference to calculate total error
relative_error = total_error / t_max # Divide by t_max to caluculate relative error

print(relative_error)

plt.show()