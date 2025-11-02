import sys
import os
sys.path.append(os.getcwd())
from src.utils import evaluate_models,save_model
from src.logger import logging
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from dataclasses import dataclass
@dataclass
class best_model_config:
  model_obj_path : str = os.path.join('artifacts','models','best_model.pkl') # artifacts will be present inside the src

def models():
  models_list = {
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "XGBRegressor": XGBRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Lightgbm Regressor": LGBMRegressor()
            }
  params = {
    "Random Forest": {
        "n_estimators": [100, 200, 300],
        "max_depth": [3,5,7],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2"]
    },
    "Gradient Boosting": {
        "learning_rate": [0.01, 0.05, 0.1],
        "n_estimators": [100, 200, 300],
        "subsample": [0.6, 0.8, 1.0],
        "max_depth": [3, 5, 7],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    },
    "XGBRegressor": {
        "learning_rate": [0.01, 0.05, 0.1],
        "n_estimators": [100, 200, 300],
        "max_depth": [3, 5, 7],
        "subsample": [0.6, 0.8, 1.0],
        "colsample_bytree": [0.6, 0.8, 1.0],
        "gamma": [0, 0.1, 0.2]
    },
    "AdaBoost Regressor": {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.05, 0.1, 0.5, 1.0],
        "loss": ["linear", "square", "exponential"],
         "max_depth": [3, 5, 7]
    },
    "Lightgbm Regressor": {
        "learning_rate": [0.01, 0.05, 0.1],
        "n_estimators": [100, 200, 300],
        "num_leaves": [31, 63, 127],
        "max_depth": [3,5,7],
        "subsample": [0.6, 0.8, 1.0],
        "colsample_bytree": [0.6, 0.8, 1.0]
        }
    }
   
  return models_list,params
   


class best_model_finder:
    def __init__(self,train_df,test_df,train_features,to_predict):
      self.model_path = best_model_config().model_obj_path
      self.train_df = train_df
      self.test_df = test_df
      self.models_list,self.params = models()
      self.threshold = 0.8
      self.train_features = train_features
      self.to_predict = to_predict
      
    def pick_best_model(self):
        x_train = self.train_df[self.train_features]
        y_train = self.train_df[self.to_predict]
        x_test = self.test_df[self.train_features]
        y_test = self.test_df[self.to_predict]

        report = evaluate_models(x_train,y_train,x_test,y_test,self.models_list,self.params)
        best_model = max(report, key=lambda k: report[k][1])
        best_model_ = report[best_model]


        if best_model_[0] >= self.threshold and best_model_[1]>=  self.threshold:
           logging.info('Best Model Found')
           
           save_model(best_model_[2],self.model_path)
           
           return f"Best Model Test R2 Score {best_model_[1]} and Model Name {best_model}"
        
        else:
           return "Best Model not found"



        #After getting report pick a model whose r2 training score and test score is minimum of 0.75

        #Sort function
        #Pick the key with max r2_test score 
        # check if train and test score is above threshold
        #if available then save the model
        #else return no best model found


