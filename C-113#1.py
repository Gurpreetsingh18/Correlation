import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()
def getDataSource(data_path):
    marks = []
    days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Coffee in ml"]))
            days.append(float(row["sleep in hours"]))

    return {"x" : marks, "y": days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee vs sleep :-  \n--->",correlation[0,1])

def setup():
    datasource = getDataSource("coffee vs sleep.csv")
    findCorrelation(datasource)
    plotFigure("coffee vs sleep.csv")

setup()