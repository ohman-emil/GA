import sys
import csv
import methods

systems = ['1', '2', '3', '4', '5_inhomogeneous', '6_inhomogeneous', '7_inhomogeneous', '8_inhomogeneous']

data = []
for system_idx, system in enumerate(systems):
    data.append([])
    with open(f'src/system{system}/data/errors.csv', 'r') as file: # Open data file
        reader = csv.reader(file)
        for row in reader: # Loop over every row
            data[system_idx].append(row)

mod_data = [[] for _ in systems] # Add a list with every step length in it
print(mod_data)

for system_idx, system_data in enumerate(data):
    for row in system_data[1:]:
        row = [float(item) for item in row] # Convert every item in the list to float
        
        difference = (0.5*(row[3]+row[4])) / (0.5*(row[1]+row[2])) # Percentage difference of avg. of the two functions

        mod_data[system_idx].append([row[0], difference])
    
print(mod_data)

# Specify the axis and plot environment options
axis_options = {
    'xmode': 'log',
    'ymode': 'log',
    'xlabel': 'Steglängd',
    'ylabel': 'Andelsskillnad',
    'width': '\\textwidth',
    'height': '0.6\\textwidth',
    'grid': 'both',
    'minor grid style': '{draw=gray!33}',
    'major grid style': '{draw=gray}',
    'legend pos': 'north west',
    'legend columns': '2',
    'legend style': '{column sep=1.5ex}'
}

plot_options = {
    'line width': '1pt',
    'mark': '*'
}

legend = ['\hspace{{-1.25ex}}' + item for item in ['1', '2', '3', '4', '5', '6', '7', '8']]

# Open file and add the file contents
with open(f'src/diagrams/diff_euler_heun.tex', 'w') as file_to_write:
    file_to_write.write(
        methods.createTikZStructure(
            axis_options,
            plot_options,
            mod_data,
            legend
        )
    )
