import pandas as pd
import numpy as np

import acquire
import prepare

def wrangle_cohort_data():
    '''
    This function takes in two dataframes and only leaves with one clean beautiful dataframe with all the
    information im going to need for the rest of this project.
    '''
    # Getting the data from the codeup sql database
    df = acquire.get_cohort_data()
    # Getting the data that holds cohort information
    info_df = acquire.get_cohort_information_data()
    # Joining the dataframes
    df = df.join(info_df,on = 'cohort_id',how = 'outer',lsuffix = 'str')
    df = prepare.clean_cohort_data(df)
    return df
