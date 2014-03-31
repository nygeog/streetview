import pandas as pd
import glob
import csv

csv_dir = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census/merged/'
out_dir = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census/'

all_csvs = glob.glob(csv_dir+"*.csv")

df_list = []

print "concatenating (merge) all tracts' blocks into 1 file - 11 seconds"

i = 0
for allcsvs in all_csvs:
	
	df = pd.read_csv(allcsvs, header=0, dtype={'geoid': object})
	df_list.append(df)
	i += 1
	print i

df   = pd.concat(df_list)
df   = df.sort_index(axis=1)

df.to_csv(out_dir+'census_2010_block.csv', sep=',', index=False)

