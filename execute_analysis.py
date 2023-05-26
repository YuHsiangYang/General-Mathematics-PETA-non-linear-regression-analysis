## These are the libaries needed to perform the regression analysis on the data set
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


excel = pd.read_excel('Data set\CO2-by-source.xlsx', 'Training data') ##import the excel file from the Data Set folder using pandas

## Convert the pandas DataFrame to numpy array so that it can be used in the curve_fit function
x_train = np.array(excel["Year"].to_numpy())
y_train = np.array(excel["Total sum"].to_numpy())


## Plot the data to see what it looks like
plt.plot(x_train, y_train, 'o')

plt.show() ##This command will show the data plot in a graph


## Define the function to be used in the curve_fit function
def nonlinear_func(x, a, b, c):
    return a * np.exp(-b * x) + c ## This is the form of the function that we are expecting


## Use the curve_fit function to fit the data to the function
params, params_covariance = curve_fit(nonlinear_func, x_train, y_train, p0=[1, 1, 1])
##params is the optimized parameters, while the params_covariance is the covariance of the parameters
print(params_covariance)

a_opt, b_opt, c_opt = params ##Decompose the optimized parameters into individual variables

# Create an array of optimized parameters
optimized_params = np.array([a_opt, b_opt, c_opt])

print("Optimized Parameters:", optimized_params) ##Print out the optimized parameters

y_plot = nonlinear_func(x_train, a_opt, b_opt, c_opt) ##Generate the y values from the optimized parameters in terms of x

plt.scatter(x_train, y_train, label='Actual Data') ##The scatter function will make the data points appear as dots
plt.plot(x_train, y_plot, 'r', label='Fitted Curve') ##The plot function will make the fitted curve appear as a line
plt.show()