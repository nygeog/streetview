import pandas as pd

df = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/NationalSampleFinalSelected_cleaned20121103.csv')
df.columns = ['strtname',
'state',
'v3',
'startlon',
'startlat',
'endlon',
'endlat',
'stnum',
'ctynum',
'trtnum',
'trtfips',
'v12',
'sample',
'v14',
'v15',
'segid']

print len(df.columns)

df.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/NationalSample.csv', index=False)

df = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/streets_right_40_feet_blocks_2000_select_with_pop_census_data_fipschar.csv')

df.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/streets_right_40_feet_blocks_2000_final.csv', index=False)