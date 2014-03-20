import pandas as pd
import glob
import csv

csv_dir = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census/working/'

acsv = glob.glob(csv_dir+"*pop_race_hisp_census_2000_block.csv")
bcsv = glob.glob(csv_dir+"*housing_census_2000_block.csv")

print 'create data frames for every file and merge by tract - 1 minute'
for a_csv, b_csv in zip(acsv,bcsv):
	a = pd.read_csv(a_csv, dtype={'geoid': object}).drop('state', axis = 1).drop('county', axis = 1).drop('tract', axis = 1).drop('block', axis = 1)
	b = pd.read_csv(b_csv, dtype={'geoid': object}).drop('state', axis = 1).drop('county', axis = 1).drop('tract', axis = 1).drop('block', axis = 1)
	#b = b.dropna(axis=1)
	merged = a.merge(b, on='geoid')
	merged.to_csv(a_csv.replace('/census/working/','/census/merged/').replace('_pop_race_hisp.csv','.csv'), index=False)