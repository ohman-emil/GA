import csv
import sys

system = sys.argv[1]

colors = [
    [0, 114, 189],
    [217, 83, 25],
    [237, 177, 32],
    [126, 47, 142],
    [119, 172, 48],
    [77, 190, 238],
    [162, 20, 47]
]
    
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

# Specify the axis environment options
axis_options = {
    'xmode': 'log',
    'xlabel': 'Steglängd',
    'ylabel': 'Avvikelse',
    'width': '\\textwidth',
    'height': '0.6\\textwidth',
    'grid': 'both',
    'minor grid style': '{draw=gray!33}',
    'major grid style': '{draw=gray}',
    'legend pos': 'north west'
}

# Convert the options into a TikZ-friendly format
axis_options_string = ""
for option in axis_options.items():
    if not option[1]: axis_options_string += f'{option[0]},' # Some options do not require a value. If options[1] is set to false, omit a value.

    else: axis_options_string += f'{option[0]}={option[1]},'

file_contents = "% Automatically generated code. github.com/ohman-emil/GA\n"
file_contents += f'\\begin{{tikzpicture}}\n' # Begin TikZ environment

# Add color definitions
for color_idx, color in enumerate(colors):
    file_contents += f'\definecolor{{clr{color_idx}}}{{RGB}}{{{str(color)[1:-1]}}}\n'

file_contents += f'\\begin{{axis}}[{axis_options_string}]\n' # Begin axis environment. Add the axis options as well

# Loop over every system and add TikZ code with data to file_contents
for system_data_idx, system_data in enumerate(mod_data):

    # Specify the plot environment options
    plot_options = {
        'line width': '1pt',
        'mark': '*',
        'color': f'clr{system_data_idx % len(colors)}'
    }

    # Convert the options into a TikZ-friendly format
    plot_options_string = ""
    for option in plot_options.items():
        plot_options_string += f'{option[0]}={option[1]},'

    file_contents += f'\\addplot[{plot_options_string}] table {{\n' # Begin the plot

    for data_value in system_data:
        file_contents += f'{data_value[0]} {data_value[1]}\n' # Write the current step length (0th element) together with the data value

    file_contents += '};\n' # End the plot
    file_contents += f'\\addlegendentry{{{data[0][system_data_idx + 1].capitalize()}}}\n' # Add the header in the csv-file as a legend entry. Make the first char capital.

file_contents += f'\\end{{axis}}\n\\end{{tikzpicture}}' # End the TikZ and axis environments

# Open file and add the file contents
with open(f'src/system{system}/diagrams/sys_{system}_errors.tex', 'w') as file_to_write:
    file_to_write.write(file_contents)