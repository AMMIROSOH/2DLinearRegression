import csv
import pandas as pd
from main import LinearRegression

file = pd.read_csv('Admission_Predict.csv', sep=",")
length = len(file)
absences = []
failures = []

for i in range(0, length):
    absences.append(file['GRE Score'][i])
    failures.append(file['Chance of Admit '][i])


ln = LinearRegression([absences, failures], sliced=True)
ln.draw()



            