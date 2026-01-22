import numpy as np
import pandas as pd
from pandas import DataFrame




def add_columns_risk_level (df):
    df['risk_level'] = df['range_km'].apply(lambda x: "low" if x <= 20 else "medium" if x <= 100 else "high" if x <= 120 else "extreme")
    return df

def add_unknown(df):
    df['manufacturer'] = df['manufacturer'].replace(np.nan, "Unknown")
    return df