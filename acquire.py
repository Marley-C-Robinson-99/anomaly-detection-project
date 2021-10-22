import pandas as pd
import numpy as np
import os
import env
def get_db_url(host = env.host, user = env.user, password = env.password, db = 'zillow'):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def create_cohort_data():
    '''
    puts cohort data into a pandas dataframe
    '''
    query = '''
        SELECT *
            FROM logs
            LEFT JOIN cohorts on cohorts.id = logs.user_id
        WHERE cohort_id IS NOT NULL;
    '''
    df = pd.read_sql(query, get_db_url(db = "curriculum_logs"))
    return df


def get_cohort_data():
    '''
    gets our cohort csv and reads it into a pandas dataframe
    '''
    if os.path.isfile("cohort.csv"):
        df = pd.read_csv("cohort.csv",index_col = 0)
    else:
        df = create_cohort_data()
        df.to_csv("cohort.csv")
    return df

def get_cohort_information_data():
    '''
    gets our cohort csv and reads it into a pandas dataframe
    '''
    url = "https://raw.githubusercontent.com/Marley-C-Robinson-99/anomaly-detection-project/main/cohorts_information%20-%20cohorts.csv"
    filename = "cohorts_information - cohorts.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col = 0)
    else:
        df = pd.read_csv(url, index_col = 0)
        df.to_csv(filename)
    return df