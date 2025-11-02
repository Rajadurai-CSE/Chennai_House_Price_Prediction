import os
import sys
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception_handler import CustomException
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score
import dill

def evaluate_models(x_train,y_train,x_test,y_test,models,params):

  
  report = {}
  
  models_list = list(models.values())
  models_param = list(params.values())
  for i in range(len(models_list)):
    rsv = RandomizedSearchCV(n_iter=10,cv=5,estimator = models_list[i],param_distributions=models_param[i])
    rsv.fit(x_train,y_train)

    y_train_pred = rsv.best_estimator_.predict(x_train)
    y_test_pred = rsv.best_estimator_.predict(x_test)

    train_r2score = r2_score(y_true=y_train,y_pred=y_train_pred)
    test_r2score = r2_score(y_true=y_test,y_pred=y_test_pred)

    report[list(models.keys())[i]] = [train_r2score,test_r2score,rsv.best_estimator_]

  return report

def save_model(model_obj,location_to_save):
  os.makedirs(os.path.dirname(location_to_save),exist_ok=True)
  try:

    with open(location_to_save,'wb') as file_location:
      dill.dump(model_obj,file_location)

    logging.info('Model Pickle saved successfully')

  except Exception as e:
    raise CustomException(e,sys)



def load_object(path):
  try:
    read_obj = open(path,'rb')
    obj = dill.load(read_obj)
    read_obj.close()
    return obj
  
  except Exception as e:
    raise CustomException(e,sys)
