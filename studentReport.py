from reportlab.platypus import Table, TableStyle, Paragraph
from AppConstant import *
from reportlab.lib import colors

def drawStudentReportTable(pdf,student_dataTable_one,student_dataTable_two):
    tableWidth = 400
    tableHeight = 100
    x1 = 70
    y1 = 600
    firstTable = Table(student_dataTable_one)

    style=TableStyle([
    ('BACKGROUND',(1,0),(1,-1),'#F2DCDB'),
    ('GRID',(0,0),(-1,-1),0.5,colors.black)
    ])
    firstTable.setStyle(style)
    firstTable.wrapOn(pdf, tableWidth, tableHeight)
    firstTable.drawOn(pdf, x1, y1)
    x2 = 300
    y2 = 600
    secondTable = Table(student_dataTable_two)
    secondTable.setStyle(style)
    secondTable.wrapOn(pdf, tableWidth, tableHeight)
    secondTable.drawOn(pdf, x2, y2)
