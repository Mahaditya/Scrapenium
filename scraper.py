''' import statements '''
from node_picker import pick_all , quit,pick,pick_similar
from urls import url_list
from data_processing import manage_data
from node_selectors import xpaths,class_names
import pandas as pd

data=[]
print(url_list)
for url in url_list:
    temp=pick_all(url)
    data.append(temp)
manage_data(data)
quit()