from xlrd import xldate_as_tuple
from datetime import datetime
def appConstantValue(studentBasicInfo,timeSpent,AttemptStatus,markedOpt,outcome,score):
    #pre-req constant values
    documentName=str(int(studentBasicInfo[2]))+'.pdf'
    documentTitle=str(int(studentBasicInfo[2]))
    heading='Wisdom Tests and Math Challenge'
    image='olympic.jpg'

    student_dataTable_one=[['Name of candidate',str(studentBasicInfo[1])],
    ['Grade',str(int(studentBasicInfo[3]))],
    ['School Name',str(studentBasicInfo[5])],
    ['City of Residence',str(studentBasicInfo[7])],
    ['Country of Residence',str(studentBasicInfo[9])]]

    student_dataTable_two=[['Registration No',str(int(studentBasicInfo[2]))],
        ['Gender',str(studentBasicInfo[4])],
        ['Date of birth',str(datetime(*(xldate_as_tuple(studentBasicInfo[6],0))))],
        ['Date of Test ',str(datetime(*(xldate_as_tuple(studentBasicInfo[8],0))))],
        ['Extra Time assistance',str(studentBasicInfo[10])]]

    studentDetailTable=[
        ['Question No','Time Spent on question (sec)','Score if correct','Score if incorrect',
        'Attempt status','What you marked','Correct Answer','Outcome (Correct/Incorrect/Not Attempted)','Your Score'],
        ['Q1',timeSpent['Q1'],'2','-1',AttemptStatus['Q1'],markedOpt['Q1'],'A',outcome['Q1'],str(score['Q1'])],
        ['Q2',timeSpent['Q2'],'2','-1',AttemptStatus['Q2'],markedOpt['Q2'],'B',outcome['Q2'],str(score['Q2'])],
        ['Q3',timeSpent['Q3'],'2','-1',AttemptStatus['Q3'],markedOpt['Q3'],'C',outcome['Q3'],str(score['Q3'])],
        ['Q4',timeSpent['Q4'],'2','-1',AttemptStatus['Q4'],markedOpt['Q4'],'D',outcome['Q4'],str(score['Q4'])],
        ['Q5',timeSpent['Q5'],'2','-1',AttemptStatus['Q5'],markedOpt['Q5'],'E',outcome['Q5'],str(score['Q5'])],
        ['','','','','','','','Total Score',str(sum(score.values()))],
        ['','','','','','','','Your overall percentile',str(int(sum(score.values())*10))]
    ]

    return documentName,documentTitle,heading,image,student_dataTable_one,student_dataTable_two,studentDetailTable,timeSpent,AttemptStatus,outcome