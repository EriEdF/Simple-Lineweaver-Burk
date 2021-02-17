import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve
from sklearn.linear_model import LinearRegression

plt.style.use('default')
plt.style.use('ggplot')

def import_data(data_file):
    try:
        return pd.read_csv(data_file)
    except FileNotFoundError:
        print("No such file as: " + data_file)
        exit()

try:
    print("Input data: " + sys.argv[1])
    filename = sys.argv[1]
except IndexError:
    print("No filename given, using 'sample_data.csv'")
    print("To use own data give the filname as an argument: python main.py 'filename'")
    filename = "sample_data.csv"

df = import_data(filename)
print(df)

# double reciprocal plot
df = df.rdiv(1)
x = np.array(df.cS).reshape(-1, 1)
y = np.array(df.v)

# linear regression
model = LinearRegression().fit(x, y)
y_pred = model.predict(x)

M = model.coef_[0]
B = model.intercept_

# solve equation to get 1/Km
xvar = symbols('xvar')
expr = M * xvar + B
reci_Km = solve(expr)

# no more reciprocals
Km = 1 / abs(reci_Km[0])
Vmax = 1 / abs(B)

plt.plot(x, y_pred, color='k', label='Regression model')
plt.scatter(x, y, edgecolor='k', facecolor='blue', alpha=0.5, label='Sample data')
plt.plot(x, y_pred, color='k', label='Regression model')
plt.xlabel("1 / [Substrate]")
plt.ylabel("1 / Enzyme Activity")
plt.legend(facecolor='white')
plt.show()

print('')
print(f"y = {M}x + {B}")
print(' ')
print(f'Km: {Km}')
print(f'Vmax: {Vmax}')
print(' ')
print("Coefficient of determination:", model.score(x, y))
