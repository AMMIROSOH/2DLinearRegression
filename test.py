import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from main import LinearRegression

file = pd.read_csv('student-mat.csv', sep=";")
length = len(file)
absences = []
failures = []

for i in range(0, length):
    absences.append(file['absences'][i])
    failures.append(file['failures'][i])


ln = LinearRegression([absences, failures], sliced=True)

plt.plot(absences, failures, 'o')
axes = plt.gca()
x_vals = np.array(axes.get_xlim())
y_vals = ln.y_intercept + ln.slope * x_vals
plt.plot(x_vals, y_vals, 'r')
plt.show()

            