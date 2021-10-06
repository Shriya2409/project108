import csv
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
counter=[]
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist=False)
#fig.show()

fig2=ff.create_distplot([df["Weight(Pounds)"].tolist()], ["Weight"], show_hist=False)
fig2.show()