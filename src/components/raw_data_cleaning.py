import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from datetime import datetime
from rapidfuzz import process
from src.logger import logging
import config
from statistics import stdev

def initiate_raw_cleaning(df):

   os.makedirs(config.NON_MATCHING_SAVE_POINT,exist_ok=True)

   df = df.copy()

   logging.info("Raw Data Transformation started")

   #Remove masked data
   df.drop(config.FEATURES_TO_DROP,axis=1,inplace=True)

   logging.info("Removed Masked Columns")

   #Update to Imputation Method in next version
   #Check Nan ratio
   no_of_nans = df.isna().any(axis=1).sum()
   
   if (no_of_nans/len(df)) * 100 > config.ACCEPTABLE_NAN_PER:
      logging.info('Data Check Required. Nan Ratio greater than acceptable nan percentage')
      logging.info('Operation Stopped!')
      return False
   
   df.dropna(inplace=True)
   logging.info(f"Dropped {no_of_nans} nan rows")
   logging.info(f"Current length of Dataset : {len(df)}")


   # Custom Transformation start
   logging.info("Column Cleaning Started")

   for key,values in config.FEATURES_TO_MODIFY.items():
      df[key] = df[key].str.lower()
      unique_values = df[key].dropna().unique().tolist()
      standard_names = values
      counter = 0
      mapping = {}
      non_matching = []
      for i in unique_values:
            match, score, _ = process.extractOne(i, standard_names, score_cutoff=80)
            if match:
               if i!=match:
                  mapping[i] = match
            else:
               non_matching.append(i)
               counter+=1

      # Matching and Non Matching
      logging.info(f"Found {counter} values with no matching the default {key} names")
      non_matching_len = len(df[df[key].isin(non_matching)])

      if non_matching_len/len(df[~df[key].isna()]) >config.ACCEPTABLE_NON_MATCHING:
         
         logging.info('Operation Stopped!')
         logging.info(f'Data Check Required. No of non matching items in {key} columns greater than ACCEPTABLE NON MATCHING')
         return False
      
      df[key] = df[key].replace(mapping)
      df = df[~df[key].isin(non_matching)]
      with open(os.path.join(config.NON_MATCHING_SAVE_POINT,f"{key}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"),"w") as f:
         f.write(",".join(non_matching))
         f.write(f"Found {counter} values with no matching default {key} names \n")
         f.write(f"No of data items with no matching name {non_matching_len} \n")
      
   
   df[config.FEATURE_TO_ADD] = pd.DatetimeIndex(df[config.FEATURE_TO_ADD_BY_COLUMNS[0]]).year - pd.DatetimeIndex(df[config.FEATURE_TO_ADD_BY_COLUMNS[1]]).year

   return custom_cleaning(df)

def return_bin(x):
    return (int(x)//(100)) * (10)

def custom_cleaning(df):

   df = df.copy()
   
   _outlier = df[df['INT_SQFT']/df['N_BEDROOM']<400]

   logging.info(f'Found {len(_outlier)} outliers based on sqft and no of bedroom logic.')

   df.drop(df[df['INT_SQFT']/df['N_BEDROOM']<400].index,inplace=True)

   #Median Based outlier Treatment
   df['BIN_SQFT'] = df['INT_SQFT'].apply(return_bin)
  
   stats = df.groupby(config.CUSTOM_CLEANING_FEATURES).agg(
      median_sales = (config.TARGET_FEATURE,'median'),
      std_sales = (config.TARGET_FEATURE,'std'),
      count_sales = (config.TARGET_FEATURE,'count'),
      min_sales = (config.TARGET_FEATURE,'min'),
      max_sales = (config.TARGET_FEATURE,'max')
   ).reset_index()
   stats['std_sales'] = stats['std_sales'].fillna(0)

   df = df.merge(stats,on=config.CUSTOM_CLEANING_FEATURES,how='left')

   transformation_len = df[(df[config.TARGET_FEATURE] >= (df['median_sales']+2*df['std_sales'])) | (df[config.TARGET_FEATURE] <= (df['median_sales']-2*df['std_sales']))]['AREA'].value_counts().sum()

   logging.info(f"Found {transformation_len} outliers based on median strategy")

   df.drop(df[((df[config.TARGET_FEATURE] >= (df['median_sales']+2*df['std_sales'])) | (df[config.TARGET_FEATURE] <= (df['median_sales']-2*df['std_sales']))) & (df['count_sales']>9)].index,inplace=True)

   return df

if __name__ == '__main__':
   df = initiate_raw_cleaning(pd.read_csv(os.path.join(config.DATAPATH,config.RAW_DATA_FILE)))
   print(type(df)==bool)
