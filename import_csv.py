import os
import csv
import pysftp
import pandas as pd
from pymongo import MongoClient
import json
from pprint import pprint

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None #not advised for production, really not.
srv = pysftp.Connection(host=os.environ.get("SFTP_HOST", ""), username=os.environ.get("SFTP_USERNAME", ""),
                        password=os.environ.get("SFTP_PASSWORD", ""), cnopts=cnopts) #log="./temp/pysftp.log"

with srv.cd('upload'):  # chdir to upload
    srv.get('products.csv', preserve_mtime=True)  # get file from sftpserver

# Closes the connection
srv.close()
print('Successfully downloaded csv')

#open connection to mangodb2
client = MongoClient(os.environ.get("MANGODB2_HOST"), port=27017, username=os.environ.get("MANGODB2_USERNAME"),password=os.environ.get("MANGODB2_PASSWORD"), authMechanism='SCRAM-SHA-256')
db = client["mangodb2"]
#check if a collection named products already exists and delete it
collectionnames = db.list_collection_names()
if "products" in collectionnames:
    db.drop_collection("products")
    print("deleted old products collection on mangodb2")
#read data from csv, create collection called products, insert csv-data into collection
data = pd.read_csv("products.csv", header=0)
payload = json.loads(data.to_json(orient='records'))
coll = db["products"]
result = coll.insert_many(payload)
print("imported {} products into mango2".format(len(result.inserted_ids)))
for product in coll.find():
    pprint(product["name"])