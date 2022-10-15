# Hack for importing files in solvers. This is not exemplary, but there are better things to focus on.
import sys
sys.path.append('./src/solvers')

import euler
import matplotlib.pyplot as plt
from numpy import sin, cos, array, trapz

step = 0.01
t_max = 15

t_points, values = euler.solve(
    [2, 0], # Values at t0
    step, # Step size
    t_max, # Time which to end
    [ # Functions
        lambda t, data: 2*data[0] + 8*data[1],
        lambda t, data: -1*data[0] - 2*data[1]
    ]
)

t_points = array(t_points) # Convert to numpy array

plt.plot(t_points, values[0], color='hotpink') # Plot numeric solution

analytic_sol = 2 * cos(2 * t_points) + 2 * sin(2 * t_points) # Solution obtained using eigenvalue-eigenvector method.
plt.plot(t_points, analytic_sol, color='mediumblue') # Plot analytical solution

plt.fill_between(t_points, analytic_sol, values[0], alpha=0.25, color='aqua') # Fill space between analytical and numeric solution

diff = abs(values[0]-analytic_sol) # Difference between analytical and numeric solution. Absolute value to make integration easier
plt.plot(t_points, diff, color='green') # Plot difference
plt.fill_between(t_points, diff, color='green', alpha=0.25) # Fill space betwen x-axis and the difference

total_error = trapz(diff, x=t_points) # Integrate the difference to calculate total error
relative_error = total_error / t_max # Divide by t_max to caluculate relative error

print(relative_error)

plt.show()