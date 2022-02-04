import os
import csv
import pysftp
import pandas as pd
from pymongo import MongoClient
import json
import urllib

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None #not advised for production, really not.
srv = pysftp.Connection(host=os.environ.get("SFTP_HOST", ""), username=os.environ.get("SFTP_USERNAME", ""),
                        password=os.environ.get("SFTP_PASSWORD", ""), cnopts=cnopts) #log="./temp/pysftp.log"

with srv.cd('upload'):  # chdir to upload
    srv.get('products.csv', preserve_mtime=True)  # get file from sftpserver

# Closes the connection
srv.close()
print('Successfully downloaded csv')

""" Imports a csv file at path csv_name to a mongo collection
returns: count of the documents in the new collection
"""
client = MongoClient(os.environ.get("MANGODB2_HOST"), port=27017, username=os.environ.get("MANGODB2_USERNAME"),password=os.environ.get("MANGODB2_PASSWORD"), authMechanism='SCRAM-SHA-256')
db = client["mangodb2"]
coll = db["products"]
data = pd.read_csv("products.csv", header=0)
payload = json.loads(data.to_json(orient='records'))
#coll.remove() #chrashed when coll hasn't been initialized yet
print(payload)
coll.insert_many(payload)
#print("inserted "+coll.count()+" into mango2") #same no insert, no coll
print("did the import thing")
