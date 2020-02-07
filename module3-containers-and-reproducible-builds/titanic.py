#anaconda prompt
#move to folder with file
##conda create -n db-env python=3.7
#conda activate db-env
#pip install pymongo[srv]
import csv
import json
import pandas as pd
import sys, getopt, pprint
import pymongo
#CSV to JSON Conversion
csvfile = open('titanic.csv', 'r')
reader = csv.DictReader(csvfile)
#connect to client
client = pymongo.MongoClient("mongodb+srv://user:password@cluster0-4d5yc.mongodb.net/test?retryWrites=true&w=majority")
#Create titanic database)
db = client.titanic
db.segment.drop()
header= [ "survived", "pclass", "name", "sex", "age", "siblings", "parents", "fare"]
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.segment.insert(row)

#above code worked