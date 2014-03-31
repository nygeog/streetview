import pandas as pd
import csv
import glob


csv_dir = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census/census/'

print 'add geoid field for each table - 5 seconds'
for a_csv in glob.glob(csv_dir+"*.csv"):
	bid = str(a_csv)[95:106]
	print bid
	with open(a_csv,'r') as csvinput:
	    with open(a_csv.replace('/census/census/','/census/working/'), 'w') as csvoutput:
	        writer = csv.writer(csvoutput, lineterminator='\n')
	        reader = csv.reader(csvinput)

	        all = []
	        row = next(reader)
	        row.append('geoid')
	        all.append(row)

	        cnt_cols = len(row)
	        z = cnt_cols

	        for row in reader:
	        	geoid_exp = bid + str(row[z-2]) #+ str(row[z-3]) 
	        	row.append(geoid_exp)
	        	all.append(row)

	        writer.writerows(all)