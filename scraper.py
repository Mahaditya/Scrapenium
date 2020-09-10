''' import statements '''
from node_picker import pick_all , quit,pick
from urls import url_list
from data_processing import manage_data
from node_selectors import xpaths
import pandas as pd

data=[]
print(pick(xpaths['rate_array']))
for url in url_list:
    temp=pick_all(url)
    data.append(temp)

manage_data(data)
quit()