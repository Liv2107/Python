# Learning different Ml models in Python.
# Starting with Linear Regression Model only using NumPy.


# y = mx + b
# m = steepness
# b = distance


# goal is to minimise the error of the line - best line fit possible.
# this is done by tweeking m and b so that for x I get the best y value.


# E = 1/n * E(yi - (mx + b))^2 - mean squared error function.
# This takes the Y value and subtracts the line value to find the error.

# m = m - L * E/m
# b = b - L * E/b


import pandas as pd
import matplotlib.pyplot as plt

# using an example dataset to predict medical costs based on bmi.
data = pd.read_csv('datasets/insurance.csv')

# visualisation
plt.scatter(data.bmi, data.charges, color="black")
plt.title("How BMI can affect Medical Insurance prices")
plt.show()

def mse(m, b, points):

    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].bmi
        y = points.iloc[i].charges

        total_error += (y - (m*x + b)) ** 2

    total_error / float(len(points)) # MSE

# gradient descent
def grad(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].bmi
        y = points.iloc[i].charges

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m, b

m = 0
b = 0
L = 0.0001
epochs = 300 # interations - this is to iterate to find the best solution for m and b resulting in the lines best fit.

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = grad(m, b, data, L)

print(m, b)

plt.scatter(data.bmi, data.charges, color="black")
plt.plot(list(range(20, 50)), [m*x + b for x in range(20, 50)], color="red") # line
plt.title("How BMI can affect Medical Insurance prices")
plt.show()