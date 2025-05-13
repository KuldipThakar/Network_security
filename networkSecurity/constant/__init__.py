import os
import sys
import numpy as np
import pandas as pd

'''defining common constant variable for trainign pipeline'''


TARGET_COLUMN = "Result"
PIPELINE_NAME : str = "NetworkSecurity"
ARTIFACT_DIR : str = "Artifacts"
FILE_NAME : str = "phishing_080020_120.csv"

TRAINING_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str= "test.csv"

'''
Data ingestuion related constant strat with DATA_INGESTION VAR NAME 
'''