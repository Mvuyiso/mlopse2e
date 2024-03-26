import sys

sys.path.insert(0, r"C:\Users\mvuyiso.gqwaru\OneDrive - Wabtec Corporation\Documents\MLOps\Krish Naik - End to End")
from src.exception import CustomException
from src.utils import load_object
import pandas as pd
import numpy as np
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        """
        This method is used to make predictions on new data using
        the trained model and preprocessor.

        Arguments:
            features (pd.DataFrame): The new data on which the model
                will make predictions.

        Returns:
            pred (np.array): The predictions made by the model
                on the new data.
        """
        try:
            # Load the model and preprocessor
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Scale the new data using the preprocessor
            data_scaled = preprocessor.transform(features)

            # Make predictions on the scaled data
            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict) # this is because we are returning a dictionary

        except Exception as e:
            raise CustomException(e, sys)