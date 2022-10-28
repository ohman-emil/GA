# Method: generateCSVData (Manipulates data to work in a csv file)
    # Arguments:
        # time_points: A 1d numpy array of time-points. First column
        # values: A 2d list of all function values. One list per column
    # Returns: A csv file for writing to
def generateCSVData(time_points, values):
    time_points = time_points.tolist() # Convert to python list

    list_to_be_written = []

    for idx, t in enumerate(time_points):
        row = [val[idx] for val in values] # Add function values
        row.insert(0, t) # Add the time point at the beginning (first column) of the list
        list_to_be_written.append(row) # Append the new row
    
    return list_to_be_written