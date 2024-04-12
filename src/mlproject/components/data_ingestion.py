#3 -- MYSQL -->Train test split-->dataset
import os
import sys
from src.mlproject.exception import CustomeException
from src.mlproject.logger import logging
from src.mlproject.util import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
 
@dataclass
class DataIngetionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')
class DataIngetion:
    def __init__(self):
        self.ingetion_config =  DataIngetionConfig()
    def initiate_data_ingetion(self):
        try:
            #read database
            logging.info("reading from mysql database")
            df = read_sql_data()
            logging.info("reading completed from mysql database")
            os.makedirs(os.path.dirname(self.ingetion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingetion_config.raw_data_path,
                      index=False,header=True)
            train_set,test_set =train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingetion_config.train_data_path,
                      index=False,header=True)
            df.to_csv(self.ingetion_config.test_data_path,
                      index=False,header=True)
            logging.info("Data Ingetion is completed")
            return (self.ingetion_config.train_data_path,
                   self.ingetion_config.test_data_path)
        except Exception as e:
            raise CustomeException(e,sys)
        
              

