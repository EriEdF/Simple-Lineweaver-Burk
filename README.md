# Simple-Lineweaver–Burk
Analysis of Michaelis–Menten enzyme kinetics using the Lineweaver–Burk equation. Draws the Lineweaver–Burk plot using linear regression and estimates Km + Vmax.

# Example Output:
![sample_output](https://github.com/EriEdF/Simple-Lineweaver-Burk/blob/main/sample_data/sample_output.png)
```
Km: 0.000141811172810182
Vmax: 0.2536312215910251
```

# Dependencies
- Pandas
- Numpy
- Matplotlib
- SymPy
- Scikit-learn

# How to use
Install dependencies using pip:
```
$ pip install pandas numpy matplotlib sympy sklearn
```
Save your data as .csv file like this (or see sample_data.csv):
| cS     | v   |
|--------|-----|
| 0.0035 | 50  |
| 0.0065 | 80  |
| ...    | ... |

Input your data as an argument (or run without to automatically use sample_data.csv)
```
$ python main.py `your_data.csv`
```

# Interpretation
Nice and fast way to distinguish different types of enzyme inhibition. Using the Lineweaver–Burk equation for the determination of Km and Vmax is not recommended.

![Enzyme_Inhibition](https://upload.wikimedia.org/wikipedia/commons/8/87/Enzyme_Inhibition_lineweaver-burk_plots.gif)

Bizz1111, CC0, via Wikimedia Commons
