import pandas as pd
import csv
import glob
import os

td        = '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/tables/'
varn      = 'rated_intersections_crashes_int/'
buf_dist = ['30','60','90'] #meters
crash_ty = ['bik_inj','bik_kil','ped_inj','ped_kil']
list_typesU = ['bikinj','bikkil','pedinj','pedkil']
# all_fname = 'all_'+varn #cafedn'
# csvext    = '.csv'
# ax        = di + '/'+ all_fname
# at        = ax + csvext


# for bufdist in buf_dist:
# 	for crashty in crash_ty:
# 		print 'clean up ' + bufdist + ' ' + crashty
# 		df = pd.read_csv(td+varn+'r'+bufdist+'_'+crashty+'_int_raw.csv')
# 		dropvars = ['OBJECTID','Shape','FID_crashes_'+crashty,'FID_r'+bufdist,'descriptio','start_lat','start_lng','end_lat','end_lng','image_date','rating_dat','BUFF_DIST']
# 		df = df.drop(dropvars, axis=1)
# 		df.to_csv(td+varn+'r'+bufdist+'_'+crashty+'_int.csv' , index=False)
# 		#os.remove(td+varn+'r'+bufdist+'_'+crashty+'_int_raw.csv')

# for bufdist in buf_dist:
# 	for crashty, typesU in zip(crash_ty, list_typesU):
# 		df = pd.read_csv(td+varn+'r'+bufdist+'_'+crashty+'_int.csv')
# 		dfg = df.groupby(['svsuid','year']).sum()
# 		dfg.to_csv(td+varn+'r'+bufdist+'_'+crashty+'_int_grp.csv', index=True)


for bufdist in buf_dist:
	for crashty, typesU in zip(crash_ty, list_typesU):
		print 'group and sum ' + bufdist + ' ' + crashty
		df = pd.read_csv(td+varn+'r'+bufdist+'_'+crashty+'_int_grp.csv')
		geo = 'r'+ bufdist
		types = crashty
		uids = 'svsuid'
		di = td+varn
		df = df.pivot(uids,'year',types)
		df = df.fillna(0)
		cols = list(df.columns.values)
		for i in range(1995,2014):
			i_s = str(i)
			df[geo+typesU+i_s] = 0
		print cols
		for i in cols:
			i_s = str(int(i))
			print i_s
			df[geo+typesU+i_s] = df[i]
		df = df.drop(cols, axis=1)
		df.to_csv(di+geo+'_'+typesU+'.csv', index=True)



di = td+varn

print 'merge csvs'
ag    = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/exchange/from_20140108_steve/newyork_with_rating_date_uid.csv')
agdroplist = ['description','start_lat','start_lng','end_lat','end_lng','image_date','rating_date']
ag    = ag.drop(agdroplist, axis=1)
r30a  = pd.read_csv(di+'r30_bikinj.csv')
r30b  = pd.read_csv(di+'r30_bikkil.csv')
r30c  = pd.read_csv(di+'r30_pedinj.csv')
r30d  = pd.read_csv(di+'r30_pedkil.csv')
r60a  = pd.read_csv(di+'r60_bikinj.csv')
r60b  = pd.read_csv(di+'r60_bikkil.csv')
r60c  = pd.read_csv(di+'r60_pedinj.csv')
r60d  = pd.read_csv(di+'r60_pedkil.csv')
r90a  = pd.read_csv(di+'r90_bikinj.csv')
r90b  = pd.read_csv(di+'r90_bikkil.csv')
r90c  = pd.read_csv(di+'r90_pedinj.csv')
r90d  = pd.read_csv(di+'r90_pedkil.csv')

merged = ag.merge(r30a, how='outer', on='svsuid').merge(r30b, how='outer', on='svsuid').merge(r30c, how='outer', on='svsuid').merge(r30d, how='outer', on='svsuid').merge(r60a, how='outer', on='svsuid').merge(r60b, how='outer', on='svsuid').merge(r60c, how='outer', on='svsuid').merge(r60d, how='outer', on='svsuid').merge(r90a, how='outer', on='svsuid').merge(r90b, how='outer', on='svsuid').merge(r90c, how='outer', on='svsuid').merge(r90d, how='outer', on='svsuid')
merged = merged.fillna(0)
df     = merged

for bufdist in buf_dist:
	for crashty, typesU in zip(crash_ty, list_typesU):
		geo = 'r'+ bufdist
		df[geo+typesU+'1995_2013'] = df[geo+typesU+'1995'] + df[geo+typesU+'1996'] + df[geo+typesU+'1997'] + df[geo+typesU+'1998'] + df[geo+typesU+'1999'] + df[geo+typesU+'2000'] + df[geo+typesU+'2001'] + df[geo+typesU+'2002'] + df[geo+typesU+'2003'] + df[geo+typesU+'2004'] + df[geo+typesU+'2005'] + df[geo+typesU+'2006'] + df[geo+typesU+'2007'] + df[geo+typesU+'2008'] + df[geo+typesU+'2009'] + df[geo+typesU+'2010'] + df[geo+typesU+'2011'] + df[geo+typesU+'2012'] + df[geo+typesU+'2013']

df.to_csv(di+'all_crashes.csv', index=False)


# ct['ctcntcafeall']  = ct['ctcntcafeenclosed']+ct['ctcntcafeunenclosed']
# r1['r1cntcafeall']  = r1['r1cntcafeenclosed']+r1['r1cntcafeunenclosed']
# n1['n1cntcafeall']  = n1['n1cntcafeenclosed']+n1['n1cntcafeunenclosed']
# n2['n2cntcafeall']  = n2['n2cntcafeenclosed']+n2['n2cntcafeunenclosed']


# merged = ag.merge(ct, how='outer', on='geoid').merge(r1, how='outer', on='msmuid').merge(n1, how='outer', on='msmuid').merge(n2, how='outer', on='msmuid')
# merged.to_csv(td+varn+'/all_'+varn+'.csv', index=False)

# print 'add percent ---- fields'
# df = pd.read_csv(at)
# # for geo in geos:
# # 	df[geo+'treepcthoodcanopy'] = df[geo+'treecanopyareasqmtr']/df[geo+'areasqmtr']

# df = df.drop('geoid', axis = 1)
# for geo in geos:
# 	df = df.drop(geo+'areasqmtr', axis = 1)
# 	df = df.fillna(0)

# df.to_csv(ax + '_pct.csv', index='False')