import json
import openpyxl
from ddt import file_data,data,unpack
import pytest

import utilities.utility


#
# def data(path):
#     def dec(fun):
#         def wrap(*args,**item):
#             with open(path,'r') as f:
#                 a=json.load(f)
#                 fun(*args, a)
#
#
#         return wrap
#     return dec
#
#
#
#
# @data(r"../Test data/testdata.json",)
# def testdata(data_dict):
#     going_from = data_dict['going_from']
#     going_to = data_dict['going_to']
#     date = data_dict['date']
#
#     print(going_from)
#     print(going_to)
#     print(date)


# def testxl_writer():
#    workbook=openpyxl.Workbook()
#    sheet=workbook.active
#    sheet['A1'] = 'Name'
#    sheet['B1'] = 'Age'
#    sheet['A2'] = 'John'
#    sheet['B2'] = 30
#    sheet['A3'] = 'Alice'
#    sheet['B3'] = 25
#    workbook.save('xlwriter.xlsx')

@pytest.mark.parametrize("Name, Age",utilities.utility.read_data_from_excel(r"C:\Users\91789\PycharmProjects\Final_project\test_cases\xlwriter.xlsx", 'Sheet'))
def test001(Name,Age):
    print(Name,' ',Age)


