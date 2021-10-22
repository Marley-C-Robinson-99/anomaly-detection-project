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
    if os.path.isfile("cohorts_information - cohorts.csv"):
        df = pd.read_csv("cohorts_information - cohorts.csv",index_col = 0)
    else:
        print('get csv from the google classroom')
    return df