import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from sklearn.model_selection import train_test_split
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.exception_handler import CustomException
# from data_transformation import data_transformation
# from model_trainer import best_model_finder
import kaggle
import requests
import json




@dataclass
class data_ingestion_config:
  train_data_path : str = os.path.join('artifacts','datasets' ,'train.csv') # artifacts will be present inside the src
  test_data_path : str = os.path.join('artifacts','datasets' , 'test.csv')
  # raw_data_path : str 
  raw_data_path:str = os.path.join('artifacts','datasets','Chennai houseing sale.csv')


class data_ingestion:
  def __init__(self):
    self.ingestion_config = data_ingestion_config()

  def ingest(self):
   
    logging.info('Data Ingestion Intiated')
    try:
      # If we are using api 

      # api_url = ""
      # response = requests.get(api_url)
      # if response.status_code == 200:
      #   # Parse the JSON response
      #   data = response.json()
      #   df = pd.read_json(data)
      # else:
      #   print(f"Error: {response.status_code}")

      os.makedirs(os.path.join(os.getcwd(),"artifacts","datasets"),exist_ok=True)
      kaggle.api.dataset_download_files("kunwarakash/chennai-housing-sales-price",path=os.path.join(os.getcwd(),"artifacts","datasets"),unzip=True,quiet=True)
      logging.info('Saved raw data')

      df = pd.read_csv(os.path.join(os.getcwd(),"artifacts","datasets","Chennai houseing sale.csv"))
      logging.info('Read the dataset')
      #ingesting the data
     
      
      logging.info('Intiated the train test split')
      train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
      train_set.to_csv(self.ingestion_config.train_data_path,index=False)
      test_set.to_csv(self.ingestion_config.test_data_path,index=False)
      logging.info('Saved the train test split data')
    except Exception as e:
      raise CustomException(e,sys)
    

if __name__ == '__main__':
 
  obj = data_ingestion()
  obj.ingest()
  # dt = data_transformation()
  # x_train,x_test =  dt.intiate_transformation(obj.ingestion_config.train_data_path,obj.ingestion_config.test_data_path)
  # print(best_model_finder(train_df=x_train,test_df=x_test).pick_best_model())




