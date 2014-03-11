import pandas as pd
import csv
import glob
import os

pr_fold     = '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data'
td        	= pr_fold + '/tables/'

kd          = pd.read_csv(td + 'kd_all/all_bufs_all_crashes_all_years_kd.csv')
kd          = kd.drop('segmid',axis=1)
cr          = pd.read_csv(td + 'rated_intersections_crashes_int/all_crashes.csv')

ag    = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/exchange/from_20140108_steve/newyork_with_rating_date_uid.csv')

merged = ag.merge(cr, how='outer', on='svsuid').merge(kd, how='outer', on='svsuid')

merged.to_csv(pr_fold+'/output/rated_streets_crash_counts_and_kernel_densities.csv', index=False)