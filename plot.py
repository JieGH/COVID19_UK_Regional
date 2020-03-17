import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import requests
from datetime import date


day = date.today()


# set the filepath and load in a shapefile
url = 'https://www.arcgis.com/sharing/rest/content/items/b684319181f94875a6879bbc833ca3a6/data'
myfile = requests.get(url)
open('%s.csv' %day , 'wb').write(myfile.content)

data = pd.read_csv('%s.csv' %day, index_col ="GSS_NM") 

# retrieving row by loc method 
n1 = data.loc[["Newcastle upon Tyne", "Gateshead","North Tyneside","South Tyneside","Sunderland","Northumberland", "County Durham"]] 
print
print("====== COVID-19 in North East England =====")
print(n1)
print
print("Update: %s" %day)
print("===========================================")




