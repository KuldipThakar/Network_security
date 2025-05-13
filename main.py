from networkSecurity.components.data_ingestion import Data_ingestion
from networkSecurity.exception.exception import NetworkSecutityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = Data_ingestion(dataIngestionConfig) 
        data_ingestion.initiate_data_ingestion()
        print(dataIngestionConfig)

        logging.info("entered in to main block")

    except Exception as e:
        raise NetworkSecutityException(e,sys)