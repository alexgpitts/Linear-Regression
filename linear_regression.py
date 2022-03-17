"""
Summary:    Simple program to calculate linear regetion based on a set of points. 
            Takes two user strings in the format "int, int, int, ... int"

Author: Alex Pitts
Date: 3/10/2022

"""


import pandas as pd
import numpy as np

def main():
    xpoints = input("enter all your x values (1, 2, 3, 4, etc.): ")
    ypoints = input("enter all your y values (1, 2, 3, 4, etc.): ")

 

    xpoints = xpoints.split(", ")
    ypoints = ypoints.split(", ")

    if(len(xpoints)!=len(ypoints)):
        print("error: please enter an equal number of x and y values...\n")
        xpoints = input("enter all your x values (1, 2, 3, 4, etc.): ")
        ypoints = input("enter all your y values (1, 2, 3, 4, etc.): ")
        xpoints = xpoints.split(", ")
        ypoints = ypoints.split(", ")

    for i in range(len(xpoints)):
        xpoints[i] = float(xpoints[i])
        ypoints[i] = float(ypoints[i])


    n = len(xpoints)
        
    print("...\n")
    print("X values =", xpoints)
    print("Y values =", ypoints)
    print("N =", n)

    xsum = 0.
    ysum = 0.
    xysum = 0.
    x2sum = 0.

    for i in range(len(xpoints)):
        xsum += xpoints[i]
        ysum += ypoints[i]
        xysum += xpoints[i] * ypoints[i]
        x2sum += xpoints[i] * xpoints[i]
    ndigits = 3

    print("\nX_sum =", round(xsum, ndigits))
    print("y_sum =", round(ysum, ndigits))
    print("XY_sum =", round(xysum, ndigits))
    print("X^2_sum =", round(x2sum, ndigits))

    b1 = round((n*xysum-(xsum*ysum))/(n*x2sum-(xsum**2)), ndigits)
    b0 = round((ysum-(b1*xsum))/n, ndigits)

    print("...\n")
    print("b1 =", b1)
    print("b0 =", b0)

    print(f"Linear regression equation: y_hat = {b0} + {b1}x")


    Predictions = []
    Errors = []
    for i in range(len(xpoints)):
        prediction = b0+(b1*(xpoints[i]))
        error = ypoints[i] - prediction
        Predictions.append(prediction)
        Errors.append(error)

    data = np.array([Predictions, Errors]).T

    dataframe2 = pd.DataFrame(data, columns=["fitted y", "residual y"])

    dataframe2.index = dataframe2.index + 1
    pd.set_option('colheader_justify', 'center')

    print("...\n")
    print(dataframe2)

    input('\n\nPress ENTER to exit...') 

if __name__ == "__main__":
    main()