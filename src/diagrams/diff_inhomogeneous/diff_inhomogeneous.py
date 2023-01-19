import csv
import sys

sys.path.append('./src')
import methods

system_num = sys.argv[1]

data = [[], []]

for system_idx, system_type in enumerate(['homogeneous', 'inhomogeneous']):
    with open(f'src/system{system_num}_{system_type}/data/errors.csv') as file:
        reader = csv.reader(file)
        for idx, row in enumerate(reader):
            if idx == 0: continue # Headers have index 0; do not add them into the data list
            data[system_idx].append(row)

result = []

for step_idx in range(len(data[0])):
    for system_idx in range(len(data[0][step_idx])):
        if system_idx == 0: continue # Skip step lengths
        diff = f'{float(data[1][step_idx][system_idx]) - float(data[0][step_idx][system_idx]):.24f}' # 24 digits of precision
        result.append([data[0][step_idx][0], diff])

mod_data = [[], [], [], []]
for idx, data_values in enumerate(result):
    mod_data[idx % 4].append(data_values)

# Specify the axis and plot environment options
axis_options = {
    'xmode': 'log',
    'xlabel': 'Steglängd',
    'ylabel': 'Skillnad i avvikelse',
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
with open(f'src/diagrams/diff_inhomogeneous/diff_inhomogeneous_system_{system_num}.tex', 'w') as file_to_write:
    file_to_write.write(
        methods.createTikZStructure(
            axis_options,
            plot_options,
            mod_data,
            ['Euler 1', 'Euler 2', 'Heun 1', 'Heun 2']
        )
    )