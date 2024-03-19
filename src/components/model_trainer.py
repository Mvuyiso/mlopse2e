#all the training code is saved here
import os
import sys
sys.path.insert(0, r"C:\Users\mvuyiso.gqwaru\OneDrive - Wabtec Corporation\Documents\MLOps\Krish Naik - End to End")

from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, GradientBoostingRegressor)

from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            # below, removing label column, and assigning train test split
            X_train, y_train, X_test, y_test =(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1])
            
            logging.info("data loaded - model training has initiated")

            models = {"Linear Regression": LinearRegression(),
                      "Lasso": Lasso(),
                      "Ridge": Ridge(),
                      "K-Neighbors Regressor": KNeighborsRegressor(),
                      "Decision Tree": DecisionTreeRegressor(),
                      "Random Forest Regressor": RandomForestRegressor(),
                      "XGBRegressor": XGBRegressor(), 
                      "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                      "AdaBoost Regressor": AdaBoostRegressor()
                      }
            
            parameters = {}
            
            #pass dict into function to be created
            model_report:dict=evaluate_model(X_train=X_train, y_train=y_train, 
                                             X_test=X_test, y_test=y_test,
                                             models=models)
            
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)]
            
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No good model")
            
            logging.info("Best models founds in training and test")

            save_object(self.model_trainer_config.trained_model_file_path,
                        obj=best_model)
            
            predicted = best_model.predict(X_test)
            r2_score = r2_score(y_test, predicted)







        except Exception as e:
            pass
