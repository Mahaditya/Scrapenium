# from node_picker import pick_all,quit,pick,pick_similar,
# from node_picker import pick_group,login,SearchLinkedIn
from urls import url_list,login_urls
# from data_processing import manage_data
from data_exports import export_to_database,export_to_csv
from node_selectors import xpaths
# from data_processing import manage_data
# import pandas as pd
from flask import Flask, request
from GoogleSearch import GoogleSearch 
import csv

searcher=GoogleSearch(driver)

app = Flask(__name__)
def scrape():
    fields = [i for i in xpaths.keys()]
    filename = "output.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
    for url in url_list:
        temp=pick_all(url)
        print(temp)
        if temp[0]=="None":
            linked_in=searcher.SearchGoogle(temp[1],temp[2],temp[3])
            # if linked_in==None:
            #     continue
            # else:
            temp[0]=linked_in
        else:
            export_to_csv(temp)
def scrapeTopTal():
    

@app.route("/hello",methods=['POST'])
def hello():
    print("inside hello")
    return "after hello"
@app.route("/fetchCodeMentorData",methods=['POST'])
def fetchCodeMentorData():
    scrape()
    return "done"

# if __name__ == '__main__':
#      app.run(host='0.0.0.0',port=80)
# scrape()
