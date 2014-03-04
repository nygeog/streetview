import pandas as pd
import csv
import glob
import os

td        	= '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/tables/'
td          = '/Users/danielmsheehan/Desktop/tables/' # for desktop

varn      	= 'kd/'
split       = 'kd_splits/'
buf_dist 	= ['30','60','90'] #meters
crash_ty 	= ['bik_inj','bik_kil','ped_inj','ped_kil']
list_typesU = ['bikinj','bikkil','pedinj','pedkil']
di 			= td+varn
ds          = td+split

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
			df['segmid_temp'] = df['SEGMIDTEXT'][1:]
			df = df.drop('SEGMIDTEXT', axis=1)
			df['segmid'] = df['segmid_temp']
			df = df.drop('segmid_temp', axis=1)

			df.to_csv(ds+'r'+bufdist+'_'+crashty+'_'+year+'_zon_stat.csv' , index=False)



# for bufdist in buf_dist:
# 	for crashty, typesU in zip(crash_ty, list_typesU):
# 		ag    = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/exchange/from_20140108_steve/newyork_with_rating_date_uid.csv')
# 		agdroplist = ['description','start_lat','start_lng','end_lat','end_lng','image_date','rating_date']
# 		ag    = ag.drop(agdroplist, axis=1)
# 		df1995 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_1995_zon_stat.csv')
# 		df1996 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_1996_zon_stat.csv')
# 		df1997 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_1997_zon_stat.csv')
# 		df1998 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_1998_zon_stat.csv')
# 		df1999 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_1999_zon_stat.csv')
# 		df2000 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2000_zon_stat.csv')
# 		df2001 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2001_zon_stat.csv')
# 		df2002 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2002_zon_stat.csv')
# 		df2003 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2003_zon_stat.csv')
# 		df2004 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2004_zon_stat.csv')
# 		df2005 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2005_zon_stat.csv')
# 		df2006 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2006_zon_stat.csv')
# 		df2007 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2007_zon_stat.csv')
# 		df2008 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2008_zon_stat.csv')
# 		df2009 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2009_zon_stat.csv')
# 		df2010 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2010_zon_stat.csv')
# 		df2011 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2011_zon_stat.csv')
# 		df2012 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2012_zon_stat.csv')
# 		df2013 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_2013_zon_stat.csv')
# 		df9513 = pd.read_csv(di+'r'+bufdist+'_'+crashty+'_1995_2013_zon_stat.csv')

# 		merged = ag.merge(df1995, how='outer', on='segmid').merge(df1996, how='outer', on='segmid').merge(df1997, how='outer', on='segmid').merge(df1998, how='outer', on='segmid').merge(df1999, how='outer', on='segmid').merge(df2000, how='outer', on='segmid').merge(df2001, how='outer', on='segmid').merge(df2002, how='outer', on='segmid').merge(df2003, how='outer', on='segmid').merge(df2004, how='outer', on='segmid').merge(df2005, how='outer', on='segmid').merge(df2006, how='outer', on='segmid').merge(df2007, how='outer', on='segmid').merge(df2008, how='outer', on='segmid').merge(df2009, how='outer', on='segmid').merge(df2010, how='outer', on='segmid').merge(df2011, how='outer', on='segmid').merge(df2012, how='outer', on='segmid').merge(df2013, how='outer', on='segmid').merge(df9513, how='outer', on='segmid')

# 		#merged = merged.fillna(0)
# 		df     = merged
# 		df     = df.drop('segmid',axis=1)

# 		df.to_csv(di+'/r'+bufdist+'_all_'+typesU+'.csv', index=False)

# ag    = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/exchange/from_20140108_steve/newyork_with_rating_date_uid.csv')
# agdroplist = ['description','start_lat','start_lng','end_lat','end_lng','image_date','rating_date']
# ag    = ag.drop(agdroplist, axis=1)

# df30a = pd.read_csv(di+'/r30_all_bikinj.csv')#.drop('svsuid',axis=1)
# df30b = pd.read_csv(di+'/r30_all_bikkil.csv')#.drop('svsuid',axis=1)
# df30c = pd.read_csv(di+'/r30_all_pedinj.csv')#.drop('svsuid',axis=1)
# df30d = pd.read_csv(di+'/r30_all_pedkil.csv')#.drop('svsuid',axis=1)
# df60a = pd.read_csv(di+'/r60_all_bikinj.csv')#.drop('svsuid',axis=1)
# df60b = pd.read_csv(di+'/r60_all_bikkil.csv')#.drop('svsuid',axis=1)
# df60c = pd.read_csv(di+'/r60_all_pedinj.csv')#.drop('svsuid',axis=1)
# df60d = pd.read_csv(di+'/r60_all_pedkil.csv')#.drop('svsuid',axis=1)
# df90a = pd.read_csv(di+'/r90_all_bikinj.csv')#.drop('svsuid',axis=1)
# df90b = pd.read_csv(di+'/r90_all_bikkil.csv')#.drop('svsuid',axis=1)
# df90c = pd.read_csv(di+'/r90_all_pedinj.csv')#.drop('svsuid',axis=1)
# df90d = pd.read_csv(di+'/r90_all_pedkil.csv')#.drop('svsuid',axis=1)

# merged = ag.merge(df30a, how='outer', on='svsuid').merge(df30b, how='outer', on='svsuid').merge(df30c, how='outer', on='svsuid').merge(df30d, how='outer', on='svsuid').merge(df60a, how='outer', on='svsuid').merge(df60b, how='outer', on='svsuid').merge(df60c, how='outer', on='svsuid').merge(df60d, how='outer', on='svsuid').merge(df90a, how='outer', on='svsuid').merge(df90b, how='outer', on='svsuid').merge(df90c, how='outer', on='svsuid').merge(df90d, how='outer', on='svsuid')
# #merged = merged.fillna(0)
# df     = merged

# df.to_csv(di+'/all_bufs_all_crashes_all_years.csv', index=False)



