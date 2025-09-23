import os
import sys 
import json

from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# certifi is a python package tht provides a set of root certificates. It is used by python library 
# That needs to make a secure HTTP coonnection 
import certifi

# This line reetrives the part of bundle of CA certfifcates provided by certfiy and store it in 
ca=certifi.where() # Trusted security authorities and this is done for SSL or TLS connection to verify  the server you connected to has a trusted certificate ensured 


import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

#-------------------------------- Converting Data to JSON ------------------------------
    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            
            # As our dataset will be having index, and we are uploaduing this to MongoDb , we will drop index
            data.reset_index(drop=True,inplace=True)

            # here we are converting the dataset using Transpose and storing it in json and this whole thing is in form of list 
            records=list(json.loads(data.T.to_json()).values())

            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
#------------------------------- Insert data into mongo --------------------------------
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collecion=collection
            self.records=records
            
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL) # we will send the data to this URL
            self.database=self.mongo_client[self.database] # mongo client -> database

            self.collecion=self.database[self.collecion] # database -> collection
            self.collecion.insert_many(self.records) # Insert 
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

# --------------------------- Intitate ------------------------------------------------        
if __name__=="__main__":
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="KAUSTUBHAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)

