import pandas as pd
import re, urllib, time, zipfile, os

download_location = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/blocks/'

df = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/misc/list_of_tracts.txt', dtype=str)

df['County'] = df['Tract'].str[:5]

dfg = df.groupby('County').sum()

dfg = dfg.drop('Tract', axis=1)

dfg.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/misc/list_of_tracts_county.txt', index=True)

df = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/misc/list_of_tracts_county.txt', dtype=str)
df = pd.read_csv('.../file.txt', dtype=str)
df['DLlink'] = 'fe_2007_' + df['County'] + '_tabblock00.zip'

# n = []
# for i in df['DLlink']:
#     n.append(i)
# print n

# for y in n:
# 	dl_url = 
# 	urllib.urlretrieve(url_1st + stfi + url_2nd, download_location+"/tr"+stfi+"_d00_shp.zip")