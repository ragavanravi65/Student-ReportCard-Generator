from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from AppConstant import *

def completeResultTable(pdf,PAGE_WIDTH,studentDetailTable):
    tableWidth=PAGE_WIDTH
    tableHeight=150
    x=0
    y=350
    style=TableStyle([
    ('BACKGROUND',(0,0),(-1,0),'#DCE6F1'),
    ('BACKGROUND',(0,1),(-1,-1),'#F2DCDB'),
    ('BOX',(0,0),(-1,-1),0.5,colors.black),
    ('GRID',(0,0),(-1,-3),0.5,colors.black),
    ('GRID',(-2,-2),(-1,-1),0.5,colors.black)
    ])
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    WrappedstudentDetailTable = [[Paragraph(cell, s) for cell in row] for row in studentDetailTable]
    fullTable=Table(WrappedstudentDetailTable,66)
    fullTable.setStyle(style)
    fullTable.wrapOn(pdf,tableWidth,tableHeight)
    fullTable.drawOn(pdf,x,y)