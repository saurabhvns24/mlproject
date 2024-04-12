from src.mlproject.logger import logging
from src.mlproject.exception import CustomeException
from src.mlproject.components.data_ingestion import DataIngetion
from src.mlproject.components.data_ingestion import DataIngetionConfig
import sys

if __name__ == "main":
    logging.info("the execution is started")

    try:
        # data_ingestion_config = DataIngetionConfig()
        data_ingestion = DataIngetion()
        data_ingestion.initiate_data_ingetion

    except Exception as e :
        logging.info("Exception = {e}")
        raise CustomeException(e,sys)    

