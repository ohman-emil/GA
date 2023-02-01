import csv
import sys

sys.path.append('./src')
import methods

system = sys.argv[1]
    
data = []
with open(f'src/system{system}/data/errors.csv', 'r') as file: # Open data file
    reader = csv.reader(file)
    for row in reader: # Loop over every row
        data.append(row)

mod_data = []
[mod_data.append([]) for _ in range(len(data[0]) - 1)] # Add an empty list into mod_data. One for every system.

for step_length_idx, step_length_data in enumerate(data):
    if step_length_idx == 0: continue # Skip over header

    for data_field_idx, data_field in enumerate(step_length_data):
        if data_field_idx == 0: continue # Skip over step length value

        mod_data[data_field_idx - 1].append([step_length_data[0], data_field]) # Add the step length and data pair into the mod_data structure

# Specify the axis and plot environment options
axis_options = {
    'xmode': 'log',
    'ymode': 'log',
    'xlabel': 'Steglängd',
    'ylabel': 'Avvikelse',
    'width': '\\textwidth',
    'height': '0.6\\textwidth',
    'grid': 'both',
    'minor grid style': '{draw=gray!33}',
    'major grid style': '{draw=gray}',
    'legend pos': 'north west'
}

plot_options = {
    'line width': '1pt',
    'mark': '*'
}

# Open file and add the file contents
with open(f'src/system{system}/diagrams/sys_{system}_errors.tex', 'w') as file_to_write:
    file_to_write.write(
        methods.createTikZStructure(
            axis_options,
            plot_options,
            mod_data,
            ['Euler 1', 'Euler 2', 'Heun 1', 'Heun 2']
        )
    )