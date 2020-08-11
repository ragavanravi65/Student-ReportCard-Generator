import xlrd
from home import *
location = ("sample.xlsx")
studentDet=[]
studentBasicInfo=[]
timeSpent={}  # col 11
AttemptStatus={} #col 15
markedOpt={} #col 16
outcome={} #col 18
score={} #col 19
workbook = xlrd.open_workbook(location) 
sheet = workbook.sheet_by_index(0) 
print('Enter the registration number:')
regNo = input()
for i in range(sheet.nrows):
    try:
        if(int(regNo) == int(sheet.cell_value(i,2))):
         studentDet.append(sheet.row_values(i))
    
    except:
        # print("exception occured")
        continue
print(len(studentDet))
for i in range (len(studentDet)):
    timeSpent[studentDet[i][11]]=str(studentDet[i][12])
    AttemptStatus[studentDet[i][11]]=str(studentDet[i][15])
    markedOpt[studentDet[i][11]]=str(studentDet[i][16])
    outcome[studentDet[i][11]]=str(studentDet[i][18])
    score[studentDet[i][11]]=int(studentDet[i][19])

studentBasicInfo=studentDet[0]
    
# print(timeSpent)
# print(AttemptStatus)
# print(markedOpt)
# print(outcome)
# print(score)
# print(studentBasicInfo)

home(studentBasicInfo,timeSpent,AttemptStatus,markedOpt,outcome,score)