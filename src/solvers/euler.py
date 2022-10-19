import math
import matplotlib.pyplot as plt

# Method: solve (Solves a system of ODEs using Euler's method)
    # Arguments:
        # t0: List. List of function values for t=0
        # t_values: A list of all time values for which the function should be evaluated.
        # func: List. List of functions. Takes input (t, [ARRAY OF FUNCTION VALUES AT t])
    # Returns: list of lists of values
def solve(t0, t_values, func):
    values = [] # List of lists of all values, 2d list
    [values.append([val]) for val in t0] # Add all t0 values to values list

    for t_idx, t in enumerate(t_values):
        if (t_idx == 0): continue # Effects of bad code

        step_size = (t - t_values[t_idx - 1]) # Difference between prev and current time point

        for idx, f in enumerate(func): # Loop through all functions and calculate their slope
            curr_slope = f(t, [var[-1] for var in values]) # Calculate slope for the current function

            new_value = values[idx][-1] + step_size * curr_slope # Calculate the new value

            values[idx].append(new_value) # Append new value to list

    return values