import math
import matplotlib.pyplot as plt

# Class which solves system of differential equations using Euler's method
# data = An object which contains:
    # t0 = List. List of function values for t=0
    # h = Float. Step size
    # t_end = Int. t-value where the computation should end
    # func = List. List of functions. Takes input (t, [ARRAY OF FUNCTION VALUES AT t])
class Euler:
    def solve(data):
        try:
            t0 = data['t0']
            h = data['h']
            t_end = data['t_end']
            func = data['func']
        except KeyError:
            print("Input does not contain enough data")
            return 0


        t_curr = 0 # Current y
        t_points = [t_curr] # List of all time points

        values = [] # List of lists of all values
        [values.append([val]) for val in t0] # Add all t0 values to values list

        while t_curr < t_end:
            for idx, f in enumerate(func):
                curr_slope = f(t_curr, [var[-1] for var in values])
                values[idx].append(values[idx][-1] + h * curr_slope)
                print(values[idx][-1])

            t_curr = t_curr + h
            t_points.append(t_curr)

        return t_points, values

t_p, v = Euler.solve({
    't0': [5, 10],
    'h': 0.01,
    't_end': 15,
    'func': [
        lambda t, data: 2*data[0] + 8*data[1],
        lambda t, data: -1*data[0] - 2*data[1]
    ]
})

plt.plot(t_p, v[0])
plt.plot(t_p, v[1])
plt.show()