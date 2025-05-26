import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''This function will ingest the dataframe into database table'''
    df.to_sql(table_name, con = engine, if_exists='replace', index=False)

def load_raw_data():
    '''this fuction will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('Data'):
        df = pd.read_csv('Data/'+file)
        logging.info(f"Ingesting {file} in db")
        ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info("----------Ingestion Complete---------")
    logging.info(f"Total Time Taken: {total_time} minutues")

if __name__ == '__main__':
    load_raw_data()