import matplotlib.pyplot as plt
from matplotlib import ticker
from numpy import geomspace#, linspace
import csv

data = []
with open('src/systems/system1/errors.csv', 'r') as file:
    reader = csv.reader(file)
    [data.append(row) for row in reader]

plot_data = []
for idx in range(len(data[0])):
    plot_data.append([float(element[idx]) for element in data[1:]])


plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams["figure.figsize"] = (16,8)
fig, ax = plt.subplots()

plt.plot(plot_data[0], plot_data[1], marker='o', label='Euler Ekv. 1')
plt.plot(plot_data[0], plot_data[2], marker='o', label='Euler Ekv. 2')
plt.plot(plot_data[0], plot_data[3], marker='o', label='Heun Ekv. 1')
plt.plot(plot_data[0], plot_data[4], marker='o', label='Heun Ekv. 2')

ax.set_xscale('log')
ax.set_xlabel('Steglängd', fontsize='x-large')
ax.set_ylabel('Avvikelse', fontsize='x-large')
ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
ax.set_xticks(geomspace(max(plot_data[0]), min(plot_data[0]), 5))
ax.legend(loc='upper left', fontsize='x-large', frameon=True)

plt.savefig('sys_1_errors.svg', bbox_inches='tight')
plt.show()
