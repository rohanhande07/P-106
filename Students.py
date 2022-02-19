import pandas as pd
import numpy as np
import csv

df = pd.read_csv("Marks.csv")

with open("Marks.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop (0)

days = []
marks = []

for i in range(len(data)):
    days.append(float(data[i][2]))
    marks.append(float(data[i][1]))

correlation = np.corrcoef(days,marks)
print("The correlation between marks and days present is ", correlation)