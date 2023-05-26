import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

excel = pd.read_excel('Data set\CO2-by-source.xlsx', 'Training data')

x_train = np.array(excel["Year"].to_numpy())
y_train = np.array(excel["Total sum"].to_numpy())

plt.plot(x_train, y_train, 'o')
plt.show()

def nonlinear_func(x, a, b, c):
    return a * np.exp(-b * x) + c

params, params_covariance = curve_fit(nonlinear_func, x_train, y_train, p0=[1, 1, 1])

a_opt, b_opt, c_opt = params

# Create an array of optimized parameters
optimized_params = np.array([a_opt, b_opt, c_opt])

print("Optimized Parameters:", optimized_params)

y_plot = nonlinear_func(x_train, a_opt, b_opt, c_opt)

plt.scatter(x_train, y_train, label='Actual Data')
plt.plot(x_train, y_plot, 'r', label='Fitted Curve')
plt.show()