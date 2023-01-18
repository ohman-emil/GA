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
        step_length: Step length
        values: A list of list of all numerically generated data
        analytic_sols: A list of the analytically generated data
    Returns: A list of errors for each list in values
"""
def calculateError(step_length, values, analytic_sols):
    temp_error = [step_length]
    for idx, sol in enumerate(values):
        analytic_sol = analytic_sols[idx % len(analytic_sols)] # Solution obtained using eigenvalue-eigenvector method.

        diff = sum(abs(sol-analytic_sol)) # Difference between analytical and numeric solution.
        function_range = max(analytic_sol)-min(analytic_sol) # Calculate range of numeric solution. Used to take an average value.

        total_error = diff/(len(analytic_sol)*function_range)

        print(idx, total_error)

        temp_error.append(total_error)
    
    return temp_error

"""
Methodd: createTikZStructure
    Arguments:
        --: --
    Returns: 
"""
colors_list = [[0, 114, 189], [217, 83, 25], [237, 177, 32], [126, 47, 142], [119, 172, 48], [77, 190, 238], [162, 20, 47]]
def createTikZStructure(axis_options, plot_options, data, legend_data, colors = colors_list):
    file_contents = '% Automatically generated code. github.com/ohman-emil/GA\n'
    file_contents += f'\\begin{{tikzpicture}}\n'

    axis_options_string = ""
    for option in axis_options.items():
        if not option[1]: axis_options_string += f'{option[0]},' # Some options do not require a value. If options[1] is set to false, omit a value.

        else: axis_options_string += f'{option[0]}={option[1]},'

    # Add color definitions
    for color_idx, color in enumerate(colors):
        file_contents += f'\definecolor{{clr{color_idx}}}{{RGB}}{{{str(color)[1:-1]}}}\n'

    file_contents += f'\\begin{{axis}}[{axis_options_string}]\n' # Begin axis environment. Add the axis options as well

    # Loop over every system and add TikZ code with data to file_contents
    for data_idx, data_value in enumerate(data):
        # Convert the options into a TikZ-friendly format
        plot_options_string = ""
        for option in plot_options.items():
            plot_options_string += f'{option[0]}={option[1]},'
        
        if colors:
            plot_options_string += f'color=clr{data_idx % len(colors)}'

        file_contents += f'\\addplot[{plot_options_string}] table {{\n' # Begin the plot

        for data_field in data_value:
            file_contents += f'{data_field[0]} {data_field[1]}\n' # Write the current step length (0th element) together with the data value

        file_contents += '};\n' # End the plot
        
        if legend_data:
            file_contents += f'\\addlegendentry{{{legend_data[data_idx]}}}\n' # Add the header in the csv-file as a legend entry.
        
    file_contents += f'\\end{{axis}}\n\\end{{tikzpicture}}' # End the TikZ and axis environments

    return file_contents