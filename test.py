import csv
import pandas as pd
from main import LinearRegression

file = pd.read_csv('student-mat.csv', sep=";")
length = len(file)
absences = []
failures = []

for i in range(0, length):
    absences.append(file['absences'][i])
    failures.append(file['failures'][i])


ln = LinearRegression([absences, failures], sliced=True)
ln.draw()



            