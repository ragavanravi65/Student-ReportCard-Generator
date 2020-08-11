from reportlab.graphics.charts.barcharts import(VerticalBarChart)
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing,String
def barChartData(timeSpent):
    data=[(int(float(timeSpent['Q1'])),int(float(timeSpent['Q2'])),int(float(timeSpent['Q3'])),int(float(timeSpent['Q4'])),int(float(timeSpent['Q5'])))]
    chart=VerticalBarChart()
    chart.data=data
    chart.x=25
    # chart.y=5
    chart.valueAxis.valueMin=0
    chart.valueAxis.valueMax=100
    chart.valueAxis.valueStep=20
    chart.bars[0].fillColor=colors.Color(red=(79.0/255),green=(129.0/255),blue=(189.0/255))
    chart.categoryAxis.categoryNames=['Q1','Q2','Q3','Q4','Q5']
    # title=String(90,300,'BarChart',fontSize=14) 
    drawing=Drawing(240,120)
    # drawing.add(title)
    drawing.add(chart)
    return drawing