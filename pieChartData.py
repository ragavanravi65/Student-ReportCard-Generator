from reportlab.graphics.charts.piecharts import(Pie)
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.validators import Auto
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing,String


def pieChartData1(timeSpent):
    data=[int(float(timeSpent['Q1'])),int(float(timeSpent['Q2'])),int(float(timeSpent['Q3'])),int(float(timeSpent['Q4'])),int(float(timeSpent['Q5']))]
    chart=Pie()
    chart.data=data
    chart.x=25
    chart.slices[3].popout = 5
    chart.slices[0].fillColor=colors.Color(red=(79.0/255),green=(129.0/255),blue=(189.0/255))
    chart.slices[1].fillColor=colors.Color(red=(192.0/255),green=(80.0/255),blue=(77.0/255))
    # chart.y=5
    # title=String(90,300,'Piechart',fontSize=14)
    chart.labels=['Q1','Q2','Q3','Q4','Q5']
    legend=Legend()
    legend.x=165
    legend.y=80
    legend.alignment='right'
    legend.colorNamePairs=Auto(obj=chart)
    drawing=Drawing(240,120)
    # drawing.add(title)
    drawing.add(chart)
    drawing.add(legend)
    return drawing

def pieChartData2(AttemptStatus):
    countAttempted=0
    countUnattempted=0
    for i in AttemptStatus.values():
        if(i=='Attempted'):
            countAttempted+=1
        elif(i=='Unattempted'):
            countUnattempted+=1
        else:
            continue
    data=[countAttempted,countUnattempted]
    chart=Pie()
    chart.data=data
    chart.x=60
    chart.slices[0].popout =10 
    chart.labels=['Attempted','Unattempted']
    chart.sideLabels=True
    legend=Legend()
    legend.x=180
    legend.y=20
    legend.alignment='right'
    legend.colorNamePairs=Auto(obj=chart)
    drawing=Drawing(240,120)
    drawing.add(chart)
    drawing.add(legend)
    return drawing

def pieChartData3(outcome):
    countCorrect=0
    countIncorrect=0
    for i in outcome.values():
        if(i=='Correct'):
            countCorrect+=1
        elif(i=='Incorrect'):
            countIncorrect+=1
        else:
            continue
    data=[countCorrect,countIncorrect]
    chart=Pie()
    chart.data=data
    chart.x=40
    chart.slices[0].popout =10 
    chart.slices[0].fillColor=colors.Color(red=(148.0/255),green=(207.0/255),blue=(23.0/255))  #148, 207, 23
    chart.slices[1].fillColor=colors.Color(red=(173.0/255),green=(47.0/255),blue=(47.0/255))  #173, 47, 47
    chart.labels=['Correct','Incorrect']
    chart.sideLabels=True
    legend=Legend()
    legend.x=200
    legend.y=45
    legend.alignment='right'
    legend.colorNamePairs=Auto(obj=chart)
    drawing=Drawing(240,120)
    drawing.add(chart)
    drawing.add(legend)
    return drawing 