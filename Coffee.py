import pandas as pd
import plotly.express as px
import numpy as np
import csv

df = pd.read_csv("Sleep.csv")

with open("Sleep.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop (0)

#fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
#fig.show()

coffee = []
sleep = []

for i in range(len(data)):
    coffee.append(float(data[i][1]))
    sleep.append(float(data[i][2]))

correlation = np.corrcoef(coffee,sleep)
print("The correlation between coffee and sleep is ", correlation)