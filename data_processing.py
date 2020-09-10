import pandas as pd
from node_selectors import xpaths
from data_exports import export_to_csv

def manage_data(data):
    df=pd.DataFrame(data,columns=[i for i in xpaths.keys()])
    export_to_csv(df)
