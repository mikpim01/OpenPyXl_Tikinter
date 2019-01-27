import openpyxl as excel


def CreateExcelFile(path,filename,sheetname):
    wb = excel.Workbook()
    ws = wb.active
    ws.title = sheetname
    wb.save(path+"\\"+filename)
    

    

