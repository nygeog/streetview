import pandas as pd

workspace = '/Volumes/Echo/GIS/projects/streetview/tasks/201405_crime/data/tables/'
inFile    = 'crime2010_bg_raw.csv'
outFile   = 'crime2010_bg.csv'
df = pd.read_csv(workspace+inFile, dtype={'ID': object})

validCols = ['ID','NAME','ST_ABBREV','CRMCYTOTC','CRMCYPERC','CRMCYMURD','CRMCYRAPE','CRMCYROBB','CRMCYASST','CRMCYPROC','CRMCYBURG','CRMCYLARC','CRMCYMVEH','Shape_Area']

df = df[validCols]

df['bgareasqmeters'] = df['Shape_Area']
df = df.drop('Shape_Area',axis=1)

df['bg2010'] = df['ID']

df['ct2010'] = df['ID'].str[:11]


df.to_csv(workspace+outFile, index=False)