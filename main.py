from networkSecurity.components.data_ingestion import Data_ingestion
from networkSecurity.exception.exception import NetworkSecutityException
from networkSecurity.logging.logger import logging

from networkSecurity.entity.config_entity import DataIngestionConfig
                                               

from networkSecurity.entity.config_entity import TrainingPipelineConfig
from collections.abc import MutableMapping
import sys


if __name__ == "__main__":
    try:

        logging.info("==== Pipeline started ====")

        training_pipeline_config  = TrainingPipelineConfig()
        logging.info("TrainingPipelineConfig loaded.")

        data_ingestion_config = DataIngestionConfig(training_pipeline_config )

        logging.info("DataIngestionConfig created.")
          # Create Data Ingestion component
        data_ingestion = Data_ingestion(data_ingestion_config) 


          # Run data ingestion
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed. Artifact: {data_ingestion_artifact}")


        # Optional: Print file paths from artifact
        print("Train file path:", data_ingestion_artifact.train_file_path)
        print("Test file path:", data_ingestion_artifact.test_file_path)

        logging.info("==== Pipeline finished successfully ====")

    except Exception as e:
        logging.error("An error occurred in the main pipeline execution.")
        raise NetworkSecutityException(e, sys)