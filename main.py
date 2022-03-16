import pandas as pd
import plotly_express as px
import csv

df = pd.read_csv("data.csv")
student_id = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = px.scatter(student_id, x = "student_id", y = "level", size = "attempt", color="attempt")
fig.show()
