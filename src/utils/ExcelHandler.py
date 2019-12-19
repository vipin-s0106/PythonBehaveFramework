from openpyxl import workbook
import openpyxl


def read_excel(filepath,sheetname):
    wb = openpyxl.load_workbook(filepath)
    work_sheet = wb[sheetname]
    print(work_sheet.max_row)



def create_excel_template(header,filepath,sheetname):
    pass


def write_excel(filepath,sheetname):
    pass


def writing_resultset(resultset):
    pass
