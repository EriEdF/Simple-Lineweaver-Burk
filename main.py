import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


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

x = np.array(df.cS).reshape((-1, 1))
y = np.array(df.v)
model = LinearRegression().fit(x, y)
y_pred = model.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.show()

print("Coefficient of determination:", model.score(x, y))
