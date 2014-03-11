import pandas as pd
import csv
import glob
import os

td        	= '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/tables/'
varn      	= 'kd/'
spli		= 'kd_splits/'
buf_dist 	= ['30','60','90'] #meters
crash_ty 	= ['bik_inj','bik_kil','ped_inj','ped_kil']
list_typesU = ['bikinj','bikkil','pedinj','pedkil']
di 			= td+varn
ds          = td+spli

siyears     = range(1995, 2014)
alyears     = ['1995_2013']
years       = alyears + siyears

for year in years:
	year = str(year)
	for bufdist in buf_dist:
		for crashty, typesU in zip(crash_ty, list_typesU):
			df1 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_'+year+'_zon_stat.csv')
			df2 = pd.read_csv(ds+'r'+bufdist+'_'+crashty+'_'+year+'_zon_stat.csv')

			pieces = [df1, df2]

			concatenated = pd.concat(pieces)

			concatenated.to_csv(td+'kd_all/'+'r'+bufdist+'_'+crashty+'_'+year+'_zon_stat.csv',index=False)

			dfg = concatenated.groupby(by='segmid').mean()

			dfg.to_csv(td+'kd_all/'+'r'+bufdist+'_'+crashty+'_'+year+'_zon_stat_grp.csv',index=True)




