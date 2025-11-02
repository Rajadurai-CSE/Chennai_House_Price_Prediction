#Configuration File
import os
import sys
ROOT_DIRECTORY = os.getcwd()

DATAPATH = os.path.join(ROOT_DIRECTORY,"artifacts","datasets")

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'
RAW_DATA_FILE = 'Chennai houseing sale.csv'

MODEL_NAME = 'best_model.pkl'

SAVED_MODEL = os.path.join(ROOT_DIRECTORY,"artifacts","trained_models")

TARGET_FEATURE = 'SALES_PRICE'
NON_MATCHING_SAVE_POINT = os.path.join(ROOT_DIRECTORY,'artifacts','non_matching')

RAW_FEATURES = ['BUILDTYPE', 'AREA', 'INT_SQFT','N_BEDROOM', 'N_BATHROOM', 'PARK_FACIL', 'STREET', 'QS_ROOMS','QS_BATHROOM','QS_BEDROOM','QS_OVERALL','DATE_SALE','DATE_BUILD']

FEATURES_TO_DROP = ['QS_ROOMS','QS_BATHROOM','QS_BEDROOM','QS_OVERALL']

FEATURE_TO_ADD = 'PROPERTY_AGE' 
FEATURE_TO_ADD_BY_COLUMNS = ['DATE_SALE','DATE_BUILD']

FINAL_FEATURES = ['BUILDTYPE', 'AREA', 'INT_SQFT','N_BEDROOM', 'N_BATHROOM', 'PARK_FACIL', 'STREET','PROPERTY_AGE']

NUM_FEATURES = ['AREA', 'INT_SQFT','N_BEDROOM', 'N_BATHROOM','PROPERTY_AGE']

CAT_FEATURES = ['BUILDTYPE', 'AREA','PARK_FACIL','STREET']


FEATURES_TO_MODIFY = {'BUILDTYPE': ['commercial','house','others'], 'AREA':['chrompet', 't nagar', 'anna nagar', 'karapakkam', 'velachery', 'kk nagar', 'adyar'], 'PARK_FACIL':['yes','no'],'STREET':['paved','gravel','no access']}
ACCEPTABLE_NAN_PER = 5
ACCEPTABLE_NON_MATCHING = 2.5

CUSTOM_CLEANING_FEATURES = ['AREA','BUILDTYPE','BIN_SQFT']

# DROP_FEATURE = 'CoapplicantIncome'
# LOG_FEATURES = ['ApplicantIncome','LoanAmount']


