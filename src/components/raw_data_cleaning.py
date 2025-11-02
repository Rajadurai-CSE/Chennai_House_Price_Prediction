import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from datetime import datetime
from rapidfuzz import process
from src.logger import logging

def initiate_raw_cleaning(df):
   df = df.copy()
   logging.info("Raw Data Transformation started")
   #Remove masked data
   df.drop(['QS_ROOMS','QS_BATHROOM','QS_BEDROOM','QS_OVERALL'],axis=1)

   logging.info("Removed Masked Columns")
   #Check Nan ratio
   no_of_nans = df.isna().sum().sum()
   
   if (no_of_nans/len(df)) * 100 >10:
      logging.info('Data Check Required. Nan Ratio greater than 10%')
      logging.info('Operation Stopped!')
      return False
      # if Nan ratio acceptable Remove Nans # Will replace with imputing methods in future
   # Custom Transformation start

   logging.info("Area Column Cleaning Started")
   df['AREA'] = df['AREA'].str.lower()
   unique_areas = df['AREA'].dropna().unique().tolist()
   standard_names = ['chrompet', 't nagar', 'anna nagar', 'karapakkam', 'velachery', 'kk nagar', 'adyar']
   counter = 0
   mapping = {}
   non_matching = []
   for area in unique_areas:
         match, score, _ = process.extractOne(area, standard_names, score_cutoff=80)
         if match:
            if area!=match:
               mapping[area] = match
         else:
            non_matching.append(area)
            counter+=1

   # Matching and Non Matching
   logging.info(f"Found {counter} data items with no matching area names")
   df['AREA'] = df['AREA'].replace(mapping)

   df = df[~df['AREA'].isin(non_matching)]

   df['AREA'] = df['AREA'].replace({'chrompet':0, 't nagar':1, 'anna nagar':2, 'karapakkam':3, 'velachery':4, 'kk nagar':5, 'adyar':6})

   df['AREA'] = df['AREA'].astype(int)
   SAVE_POINT = os.path.join(os.getcwd(),'artifacts','non_matching')
   os.makedirs(SAVE_POINT,exist_ok=True)

   with open(os.path.join(SAVE_POINT,f"non_matching_areas_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"),"w") as f:
      f.write(",".join(non_matching))
      f.write(f"Found {counter} data items with no matching area names")
      
   
   df['Property_age'] = pd.DatetimeIndex(df['DATE_SALE']).year - pd.DatetimeIndex(df['DATE_BUILD']).year

   logging.info("BuildType Column Cleaning Started")
   df['BUILDTYPE'] = df['BUILDTYPE'].str.lower()

   unique_buildtype = df['BUILDTYPE'].dropna().unique().tolist()
   standard_buildtype_names = ['commercial', 'others','house']
   buildtype_counter = 0
   buildtype_mapping = {}
   non_matching_buildtype = []
   for buildtype in unique_buildtype:
         match, score, _ = process.extractOne(buildtype, standard_buildtype_names, score_cutoff=80)
         if match:
            if buildtype!=match:
               buildtype_mapping[buildtype] = match
         else:
            non_matching_buildtype.append(buildtype)
            buildtype_counter+=1

   with open(os.path.join(SAVE_POINT,f"non_matching_buildtype_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"),"w") as f:
      f.write(",".join(non_matching_buildtype))
      f.write(f"Found {buildtype_counter} data items with no matching buildtype names")

   df['BUILDTYPE'] = df['BUILDTYPE'].replace(buildtype_mapping)

   df = df[~df['BUILDTYPE'].isin(non_matching_buildtype)]

   df['BUILDTYPE'] = df['BUILDTYPE'].replace({'commercial':0, 'others':1,'house':2})
   df['BUILDTYPE'] = df['BUILDTYPE'].astype(int)

   logging.info(f"Found {counter} data items with no matching buildtype names")
   logging.info("Raw Data Cleaning Sucessfull!!")
   
   df['PARK_FACIL'] = df['PARK_FACIL'].str.lower()
   unique_parkfacil = df['PARK_FACIL'].dropna().unique().tolist()
   parkfacil_match = {}
   non_matching_parkfacil = []
   for i in unique_parkfacil:
      if i[0]=='y':
         if (i!='yes'):
            parkfacil_match[i] = 'yes'
      elif i[0]=='n':
         if (i!='no'):
            parkfacil_match[i] =  'no'
      else:
         non_matching_parkfacil.append(i)
         
            


   df['PARK_FACIL'] = df['PARK_FACIL'].replace(parkfacil_match)
   df = df[~df['PARK_FACIL'].isin(non_matching_parkfacil)]
   df['PARK_FACIL'] = df['PARK_FACIL'].astype(int)
         
         
   df.dropna(inplace=True)
   return df
   
