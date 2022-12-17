import matplotlib.pyplot as plt
from matplotlib import ticker, font_manager
from numpy import geomspace
import csv
import os

# SET FONT_PATH ENV VAR POINTING TO A TTF FILE

font_path = os.getenv('FONT_PATH') # Font path
font_manager.fontManager.addfont(font_path) # Add font to matplotlib lib
prop = font_manager.FontProperties(fname=font_path) # Get its properties

data = []
with open('src/system5/homogeneous/data/errors.csv', 'r') as file: # Open data file
    reader = csv.reader(file)
    [data.append(row) for row in reader] # Add each row to the data list

plot_data = []
for idx in range(len(data[0])):
    plot_data.append([float(element[idx]) for element in data[1:]]) # Convert data to float and change the data structure a bit, so every value in a column is grouped instead

# matplotlib parameters
params = {
    "figure.figsize": (8.8, 4.4),
    "font.family": "serif",
    "font.serif": prop.get_name() # Get name from font_manager
}

plt.rcParams.update(params) # Add the params to matplotlib
fig, ax = plt.subplots() # Create a subplot

# Plot each equation one at a time
plt.plot(plot_data[0], plot_data[1], marker='o', label='Euler Ekv. 1')
plt.plot(plot_data[0], plot_data[2], marker='o', label='Euler Ekv. 2')
plt.plot(plot_data[0], plot_data[3], marker='o', label='Heun Ekv. 1')
plt.plot(plot_data[0], plot_data[4], marker='o', label='Heun Ekv. 2')

ax.set_xscale('log') # Make x-axis log scale
ax.set_xlabel('Steglängd', fontsize='x-large')
ax.set_ylabel('Avvikelse', fontsize='x-large')
ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter()) # Add ticks to x-axis
ax.set_xticks(geomspace(max(plot_data[0]), min(plot_data[0]), 10)) # Add equally spaces ticks to x-axis
ax.set_xticks([], minor=True) # Remove the minor ticks
ax.legend(loc='upper left', fontsize='x-large', frameon=True) # Add legend
plt.grid() # Add grid lines

plt.savefig('sys_5_homogeneous_errors.svg', bbox_inches='tight') # Save figure
plt.show() # And show it!
