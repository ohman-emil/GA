# Method: euler (Solves a system of ODEs using Euler's method)
    # Arguments:
        # t0: List. List of function values for t=0
        # t_values: A list of all time values for which the function should be evaluated.
        # func: List. List of functions. Takes input (t, [ARRAY OF FUNCTION VALUES AT t])
    # Returns: list of lists of values
def euler(t0, t_values, func):
    values = [] # List of lists of all values, 2d list
    [values.append([val]) for val in t0] # Add all t0 values to values list

    for t_idx, t in enumerate(t_values):
        # Because the values for when t=0 are already appended, we skip over them here
        if (t_idx == 0): continue

        step_size = (t - t_values[t_idx - 1]) # Difference between prev and current time point

        for idx, f in enumerate(func): # Loop through all functions and calculate their slope
            curr_slope = f(t, [var[-1] for var in values]) # Calculate slope for the current function

            new_value = values[idx][-1] + step_size * curr_slope # Calculate the new value

            values[idx].append(new_value) # Append new value to list

    return values

# Method: heun (Solves a system of ODEs using Heuns's method)
    # Arguments:
        # t0: List. List of function values for t=0
        # t_values: A list of all time values for which the function should be evaluated.
        # func: List. List of functions. Takes input (t, [ARRAY OF FUNCTION VALUES AT t])
    # Returns: list of lists of values
def heun(t0, t_values, func):
    values = [] # List of lists of all values, 2d list
    [values.append([val]) for val in t0] # Add all t0 values to values list

    for t_idx, t in enumerate(t_values):
        # Because the values for when t=0 are already appended, we skip over them here
        if (t_idx == 0): continue

        latest_func_values = [var[-1] for var in values] # Create a list of all the last function values
        step_size = (t - t_values[t_idx - 1]) # Difference between prev and current time point

        # Calculate x-hat
        x_hat = [] # List of all predicted function values
        for idx, f in enumerate(func):
            predicted_slope = f(t, latest_func_values) # Calculate slope for the current function
            predicted_value = values[idx][-1] + step_size * predicted_slope # Calculate the new value
            x_hat.append(predicted_value)

        for idx, f in enumerate(func): # Loop through all functions and calculate their slope
            new_value = values[idx][-1] + 0.5*step_size*( # Calculate new value using Heun's method
                f(t, latest_func_values) + f(t, x_hat)
            )

            values[idx].append(new_value) # Append new value to list

    return values