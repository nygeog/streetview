import pandas as pd
import os

td = '/Users/danielmsheehan/GIS/201405_crime/data/tables/'

ce = td + 'census/'
hc = td + 'homicides_count/'
hz = td + 'homicides_zonal_stats/'

# print 'clean up homicide counts'
# years = ['2005','2006','2007','2008','2009','2010','2005_2010']
# for year in years:
# 	df = pd.read_csv(hc+'homicides_'+year+'_tracts_2010_dis_raw.csv')
# 	df = df[['GEOID10','SUM_num_victim']]
# 	df['geoid'] = df['GEOID10']
# 	df['cnthomicide'+year] = df['SUM_num_victim']
# 	df = df.drop(['SUM_num_victim','GEOID10'],axis=1)
# 	df.to_csv(hc+'homicides_'+year+'_tracts_2010_dis.csv',index=False)
# 	os.remove(hc+'homicides_'+year+'_tracts_2010_dis_raw.csv')

# print 'clean up homicide zonal stats'
# years = ['2005','2006','2007','2008','2009','2010','2005_2010']
# for year in years:
# 	df = pd.read_csv(hz+'homicides_'+year+'_tracts_2010_table_raw.csv')
# 	df = df[['GEOID','COUNT','AREA','MIN','MAX','RANGE','MEAN','STD','SUM']]
# 	df['geoidTEMP'] = df['GEOID']
# 	df = df.drop('GEOID', axis=1)
# 	df['geoid'] = df['geoidTEMP']
# 	df['homzonstatmin'+year] = df['MIN']
# 	df['homzonstatmax'+year] = df['MAX']
# 	df['homzonstatrng'+year] = df['RANGE']
# 	df['homzonstatavg'+year] = df['MEAN']
# 	df['homzonstatstd'+year] = df['STD']
# 	df['homzonstatsum'+year] = df['SUM']
# 	df = df.drop(['geoidTEMP','MIN','MAX','RANGE','MEAN','STD','SUM','COUNT','AREA'],axis=1)
# 	df.to_csv(hz+'homicides_'+year+'_tracts_2010_table.csv',index=False)
# 	os.remove(hz+'homicides_'+year+'_tracts_2010_table_raw.csv')

# print 'clean up tiger census tract data'
# df = pd.read_csv(ce+'tracts_2010_select_nyc_raw.csv')
# df = df[['GEOID10','ALAND10','AWATER10','sq_meters']]
# df['geoid'] = df['GEOID10']
# df['tigerlandarea'] = df['ALAND10']
# df['tigerwaterarea'] = df['AWATER10']
# df['unclippedareasqmeters'] = df['sq_meters']
# df = df.drop(['GEOID10','ALAND10','AWATER10','sq_meters'],axis=1)
# df.to_csv(ce+'tracts_2010_select_nyc.csv',index=False)
# os.remove(ce+'tracts_2010_select_nyc_raw.csv')

# print 'clean up dcp census tract data'
# df = pd.read_csv(ce+'nyct2010_raw.csv')
# df = df[['geoid','sq_meters']]
# df['dcp_sq_meters'] = df['sq_meters']
# df = df.drop('sq_meters',axis=1)
# df.to_csv(ce+'nyct2010.csv',index=False)
# os.remove(ce+'nyct2010_raw.csv')

# print 'clean up census population counts'
# df = pd.read_csv(ce+'sf1_2010_tract_st36_totpop.csv',dtype={'state': object,'county': object,'tract': object})
# df['geoid'] = df.state.map(str) + df.county.map(str)  + df.tract.map(str) 
# df['totpop2010'] = df['P0010001']
# df = df.drop(['state','county','tract','P0010001'],axis=1)
# df.to_csv(ce+'tract_pop_2010.csv',index=False)
# os.remove(ce+'sf1_2010_tract_st36_totpop.csv')





