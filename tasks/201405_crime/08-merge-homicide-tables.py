import pandas as pd
import os

td = '/Users/danielmsheehan/GIS/201405_crime/data/tables/'

ce = td + 'census/'
hc = td + 'homicides_count/'
hz = td + 'homicides_zonal_stats/'

print 'merge census'
t1 = pd.read_csv(ce+'nyct2010.csv')
#Do not need t2 = pd.read_csv(ce+'tracts_2010_select_nyc.csv')
po = pd.read_csv(ce+'tract_pop_2010.csv')

print 'merge homicides count'
df = t1.drop('dcp_sq_meters',axis=1)
years = ['2005','2006','2007','2008','2009','2010','2005_2010']
for year in years:
	newTable = pd.read_csv(hc+'homicides_'+year+'_tracts_2010_dis.csv')
	df = df.merge(newTable,on='geoid', how='outer')
df = df.fillna(0)
df.to_csv(hc + 'all_homicides_count.csv',index=False)
dfhc = df

print 'merge homicides zonal stats'
df = t1.drop('dcp_sq_meters',axis=1)
years = ['2005','2006','2007','2008','2009','2010','2005_2010']
for year in years:
	newTable = pd.read_csv(hz+'homicides_'+year+'_tracts_2010_table.csv')
	df = df.merge(newTable,on='geoid', how='outer')
df = df.fillna(0)
df.to_csv(hz + 'all_homicides_zonal_stats.csv',index=False)
dfhz = df

print 'merge all'
df = t1.merge(po, on='geoid', how='inner').merge(dfhc, on='geoid', how='outer').merge(dfhz, on='geoid', how='outer')
df.to_csv(td + 'nyc_tracts_2010_homicide_counts_zonal_stats.csv',index=False)