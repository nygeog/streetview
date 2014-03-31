import pandas as pd

df = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/NationalSampleFinalSelected_cleaned20121103.csv', header=None)

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

df.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/_original/NationalSample.csv', index=False)

