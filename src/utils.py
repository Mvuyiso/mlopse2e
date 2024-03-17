import os
import sys

sys.path.insert(0, r"C:\Users\mvuyiso.gqwaru\OneDrive - Wabtec Corporation\Documents\MLOps\Krish Naik - End to End")

import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
import dill


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    logging.info("A file was saved")