#main code goes here
from AppConstant import *
from pieChartData import *
from barchartData import *
from completeStudentMarklist import *
from studentReport import *
from ruler import *
from reportlab.pdfgen import canvas  
from reportlab.rl_config import defaultPageSize 
from reportlab.pdfbase.pdfmetrics import stringWidth
# from reportlab.platypus import Table, TableStyle, Paragraph
# from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.graphics.shapes import Drawing,String
# from reportlab.graphics.charts.barcharts import(VerticalBarChart)
# from reportlab.graphics.charts.piecharts import(Pie)
# from reportlab.graphics.charts.legends import Legend
# from reportlab.lib.validators import Auto

def home(studentBasicInfo,timeSpent,AttemptStatus,markedOpt,outcome,score):
    documentName,documentTitle,heading,image,student_dataTable_one,student_dataTable_two,studentDetailTable,timeSpent,AttemptStatus,outcome=appConstantValue(studentBasicInfo,timeSpent,AttemptStatus,markedOpt,outcome,score)
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[1]
    pdf=canvas.Canvas(documentName) #,bottomup=0,pagesize=letter
    pdf.setTitle(documentTitle)
    # pdf.drawString(10,20,str(PAGE_HEIGHT))
    text_width = stringWidth(heading,"Helvetica",2)
    # pdf.drawString(10,10,str(text_width))
    # use below to know your page width details:  841 y axis,595 x axis
    pdf.drawCentredString(295,790,heading) #(PAGE_WIDTH - text_width)/4,100
    #drawMyRuler(pdf)    #can make use of this for scaling puurpose
    # adding logo below the title
    pdf.drawInlineImage(image,250,725,90,55)
    # pdf.drawString(10,10,str(PAGE_WIDTH))


    # inclusion of table data for student based details
    drawStudentReportTable(pdf,student_dataTable_one,student_dataTable_two)
    completeResultTable(pdf,PAGE_WIDTH,studentDetailTable)

    #chart representation
    chartTables=Table([
        [barChartData(timeSpent),pieChartData1(timeSpent)],
        [pieChartData2(AttemptStatus),pieChartData3(outcome)]

    ],270,150)
    chartTables.setStyle([
        ('VALIGN',(0,0),(-1,-1),'CENTER'),
        ('ALIGN',(0,0),(-1,-1),'CENTER')
    ])
    chartTables.wrapOn(pdf,814,350)
    chartTables.drawOn(pdf,0,0)

    #dummy values inside pie3
    # pdf.drawString(333,76,"67%")
    # pdf.drawString(390,60,"33%")
    #final save to  make the pdf exportable document
    pdf.save()
