import os 
import json
import sys

import pymongo.mongo_client
''' we are loading mongodb url from .env fdile this keeps passworfs and URL hidden and secure'''


from dotenv import load_dotenv 
from pymongo.mongo_client import MongoClient

load_dotenv()


MONGO_DB_URL= os.getenv("MONGO_DB_URL")

print(MONGO_DB_URL)

import certifi
''' certifi provides trusted SSL certificate'''
ca = certifi.where()
'''ca is a file path to a list of trusted certificate authorities (CAs).'''


''' what is certifi here? it is packagae that provide set of root certificates. this is to insure that they trust only certificates that is given'''
'''certified.where : the ca variable is certificate othoritis which are trusted which is ussuallty done for ssl certificates'''


import pandas as pd
import numpy as np
import pymongo
from networkSecurity.exception.exception import NetworkSecutityException
from networkSecurity.logging.logger import logger

class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecutityException(e,sys)
        
    def csvToJson_Converter(self,filePath):
        '''read csv , convert to jason like list of dictionarues which mongo db understand '''
        try:
            data = pd.read_csv(filePath)
            data.reset_index(drop=True,inplace=True)
            '''here we have removed the index from the csv file'''
            records = list(json.loads(data.T.to_json()).values())
            '''this convert pandas dataframe data into a list of jason style python dictonaries


🔹 data.T
This transposes the DataFrame (rows become columns, and vice versa).
   Name  Age
0  Alice   30
1  Bob     25

AFTER data.T

       0     1
Name  Alice  Bob
Age     30    25


🔹 data.T.to_json()
Converts the transposed DataFrame to a JSON string (orient='columns' by default).
{"0": {"Name": "Alice", "Age": 30}, "1": {"Name": "Bob", "Age": 25}}


🔹 json.loads(...) Parses the JSON string into a Python dictionary:
{
    "0": {"Name": "Alice", "Age": 30},
    "1": {"Name": "Bob", "Age": 25}
}

🔹 .values()
Extracts just the values (the dictionaries):
[{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}]
'''
            return records
            
        except Exception as e:
            raise NetworkDataExtract(e,sys)
        
    def insert_data_mongoDB(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_client = MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecutityException(e,sys)
        
if __name__ == '__main__':
        FILE_PATH = "Network_Data\phising_080020_120.csv"
        DATABASE = "KULDIPAI"
        collection ="NetworkData"
        networkobj = NetworkDataExtract()
        records = networkobj.csvToJson_Converter(filePath=FILE_PATH)
        print(records)
        no_of_records = networkobj.insert_data_mongoDB(records,DATABASE, collection)
        print(no_of_records)

    

    
