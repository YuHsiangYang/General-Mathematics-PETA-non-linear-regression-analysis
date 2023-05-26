# Documentation for the regression analysis model used in General mathematics Performance Task #1

Creator: Yu-Hsiang

## Set-up:
Python version: 3.11.3
Installed packages:
```
Package           Version
----------------- -------
contourpy         1.0.7
cycler            0.11.0
et-xmlfile        1.1.0
fonttools         4.39.4
kiwisolver        1.4.4
matplotlib        3.7.1
metaplot          1.1.0
numpy             1.24.3
openpyxl          3.1.2
packaging         23.1
pandas            2.0.1
Pillow            9.5.0
Pint              0.22
pip               23.1.2
pyparsing         3.0.9
python-dateutil   2.8.2
pytz              2023.3
scipy             1.10.1
setuptools        65.5.0
six               1.16.0
typing_extensions 4.6.2
tzdata            2023.3
```

The code reads an Excel file containing data on CO2 emissions, plots the data, fits a non-linear curve to it using the curve_fit function from the scipy.optimize library, and plots the fitted curve against the actual data. 


## Here is a step by step explanation: 
1. The necessary libraries are imported: pandas, numpy, scipy.optimize, and matplotlib.pyplot. 
2. The Excel file containing the data is read into a pandas DataFrame object called "excel". 
3. Two numpy arrays are created: "x_train" contains the "Year" column from the DataFrame, and "y_train" contains the "Total sum" column. These arrays will be used as the x and y values for plotting and curve fitting. 
4. The data points are plotted using the "plt.plot" function and displayed using the "plt.show" function. 
5. A non-linear function called "nonlinear_func" is defined, which takes an input array "x" and three parameters "a", "b", and "c", and returns the value of the function at each point in "x". 
6. The "curve_fit" function is used to fit the "nonlinear_func" to the data, using "x_train" and "y_train" as inputs and an initial guess for the parameters of [1, 1, 1]. The optimized parameters are returned as a numpy array called "params". 
7. The optimized parameters are separated into individual variables "a_opt", "b_opt", and "c_opt". 
8. The optimized parameters are stored in a numpy array called "optimized_params". 
9. The fitted curve is generated using "nonlinear_func" and the optimized parameters, and plotted against the actual data using the "plt.scatter" and "plt.plot" functions. The plot is displayed using the "plt.show" function.

## References:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
https://scipy-cookbook.readthedocs.io/items/robust_regression.html
