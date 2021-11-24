# Simple-Lineweaver–Burk
Analysis of Michaelis–Menten enzyme kinetics using the Lineweaver–Burk equation. Plots the Lineweaver–Burk graph using linear regression and estimates Km + Vmax.

## Example Output:
![sample_output](https://github.com/EriEdF/Simple-Lineweaver-Burk/blob/main/sample_data/sample_output.png)
```
Km: 0.000141811172810182
Vmax: 0.2536312215910251

Coefficient of determination: 0.995776951975508
```

## Installation and usage
#### Requires
- Python 3
- Pandas
- Numpy
- Matplotlib
- Scikit-learn

Install python dependencies:
```
# using pip package manager
$ pip install pandas numpy matplotlib sklearn
```
Save your data as .csv file. Place the substrate concentration in the 'cS' column and reaction rate in the 'v' column (Example: /sample_data/sample_data.csv ):
| cS     | v   |
|--------|-----|
| 0.0035 | 50  |
| 0.0065 | 80  |
| ...    | ... |

Input your data as an argument (or run without to use sample_data.csv)
```
# run with your data
$ python main.py `your_data.csv`

# run with sample_data
$ python main.py
```
