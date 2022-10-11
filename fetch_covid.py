
import xlsxwriter
import pandas as pd
import numpy as np

import requests



timline = requests.get(url='https://covid19.th-stat.com/api/open/timeline')
workbook = xlsxwriter.Workbook('covid.xlsx')
worksheet =workbook.add_worksheet()

data_timeline = timline.json()
worksheet.write(0, 0, 'วันที่')
worksheet.write(0, 1, 'ผู้ติดเชื้อยืนยัน')
worksheet.write(0, 2, 'หายวันนี้')
worksheet.write(0, 3, 'หายทั้งหมด')
worksheet.write(0, 4, 'ผู้ติดเชื้อทั้งหมด')
worksheet.write(0, 5, 'ตายวันนี้')
worksheet.write(0, 6, 'ตายทั้งหมด')

for i in range(len(data_timeline['Data'])):
    worksheet.write(i+1, 0, data_timeline['Data'][i]['Date'])
    worksheet.write(i+1, 1, data_timeline['Data'][i]['NewConfirmed'])
    worksheet.write(i+1, 2, data_timeline['Data'][i]['NewRecovered'])
    worksheet.write(i+1, 3, data_timeline['Data'][i]['Recovered'])
    worksheet.write(i+1, 4, data_timeline['Data'][i]['Confirmed'])
    worksheet.write(i+1, 5, data_timeline['Data'][i]['NewDeaths'])
    worksheet.write(i+1, 6, data_timeline['Data'][i]['Deaths'])

workbook.close()
# for i in range(len(data['Data'])):


#       print("____________________________")

#      print(data['Data'][i]['Province'])
#     print(data['Data'][i]['Age'])
#    print(data['Data'][i]['District'])


