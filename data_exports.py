# import pandas as pd
import mysql.connector
import datetime
import time
import csv 
def export_to_csv(data):
    # fields = ['Name','Title','Location','LinkedIn']
    # filename = "TorreDataNew.csv"
    # with open(filename, 'w') as csvfile:
    # csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(fields)
    # data=','.join(data)
    # data=data+"\n"
    # print(data)
    with open("output.csv", 'a',encoding="utf-8",newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)

# def export_to_google_sheets(df):
#     pass

