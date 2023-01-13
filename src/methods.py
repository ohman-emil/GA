"""
Method: generateCSVData (Manipulates data to work in a csv file)
    Arguments:
        time_points: A 1d numpy array of time-points. First column
        values: A 2d list of all function values. One list per column
    Returns: A list of formatted data
"""
def generateCSVData(time_points, values):
    time_points = time_points.tolist() # Convert to python list

    list_to_be_written = []

    for idx, t in enumerate(time_points):
        row = [val[idx] for val in values] # Add function values
        row.insert(0, t) # Add the time point at the beginning (first column) of the list
        list_to_be_written.append(row) # Append the new row
    
    return list_to_be_written

"""
Method: calculateError (Calculates the errors of analytic function and numerical solution)
    Arguments:
        --: --
    Returns: A 
"""
def calculateError(step_length, values, analytic_sols, time_points):
    temp_error = [step_length]
    for idx, sol in enumerate(values):
        analytic_sol = analytic_sols[idx % len(analytic_sols)] # Solution obtained using eigenvalue-eigenvector method.

        diff = sum(abs(sol-analytic_sol)) # Difference between analytical and numeric solution.
        function_range = max(analytic_sol)-min(analytic_sol) # Calculate range of numeric solution. Used to take an average value.

        total_error = diff/(len(analytic_sol)*function_range)

        print(idx, total_error)

        temp_error.append(total_error)
    
    return temp_error
