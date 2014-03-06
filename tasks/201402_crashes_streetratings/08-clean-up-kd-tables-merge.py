import pandas as pd
import csv
import glob
import os

td        	= '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/tables/'
varn      	= 'kd/'
spli        = 'kd_splits/'
buf_dist 	= ['30','60','90'] #meters
crash_ty 	= ['bik_inj','bik_kil','ped_inj','ped_kil']
list_typesU = ['bikinj','bikkil','pedinj','pedkil']
di 			= td+varn
ds          = td+spli

siyears     = range(1995, 2014)
alyears     = ['1995_2013']
years       = alyears + siyears

stat_list   = ['COUNT','AREA','MIN','MAX','RANGE','MEAN','STD','SUM']

print 'for regular kds'

for bufdist in buf_dist:
	for crashty, typesU in zip(crash_ty, list_typesU):
		for year in years:
			year = str(year)
			print 'clean up ' + bufdist + ' ' + crashty
			df = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_'+year+'_zon.csv')
			df = df.drop('OBJECTID', axis=1)
			for stat in stat_list:
				df['r'+bufdist+typesU+year+'kd'+stat.lower()] = df[stat]
			df = df.drop(stat_list, axis=1)
			df['segmid_temp'] = df['SEGMID']
			df = df.drop('SEGMID', axis=1)
			df['segmid'] = df['segmid_temp']
			df = df.drop('segmid_temp', axis=1)

			df.to_csv(di+'r'+bufdist+'_'+crashty+'_'+year+'_zon_stat.csv' , index=False)

print 'for kd splits'

for bufdist in buf_dist:
	for crashty, typesU in zip(crash_ty, list_typesU):
		for year in years:
			year = str(year)
			print 'clean up ' + bufdist + ' ' + crashty
			df = pd.read_csv(ds+'r'+bufdist+'_'+crashty+'_'+year+'_zon.csv')
			df = df.drop('OBJECTID', axis=1)
			for stat in stat_list:
				df['r'+bufdist+typesU+year+'kd'+stat.lower()] = df[stat]
			df = df.drop(stat_list, axis=1)
			df['segmid_temp'] = df['SEGMIDTEXT'].str[1:]
			df = df.drop('SEGMIDTEXT', axis=1)
			df['segmid'] = df['segmid_temp']
			df = df.drop(['segmid_temp','ZONE_CODE'], axis=1)

			df.to_csv(ds+'r'+bufdist+'_'+crashty+'_'+year+'_zon_stat.csv' , index=False)



