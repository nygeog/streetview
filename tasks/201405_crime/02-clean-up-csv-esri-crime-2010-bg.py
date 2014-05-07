import pandas as pd
import shutil
import errno

workspace = '/Volumes/Echo/GIS/projects/streetview/tasks/201405_crime/data/tables/'
outspace = '/Volumes/Echo/GIS/projects/streetview/tasks/201405_crime/data/output/esri_2010_crime/'
inFile    = 'crime2010_bg_raw.csv'
outFile   = 'crime2010_bg.csv'
df = pd.read_csv(workspace+inFile, dtype={'ID': object})

validCols = ['ID','ST_ABBREV','CRMCYTOTC','CRMCYPERC','CRMCYMURD','CRMCYRAPE','CRMCYROBB','CRMCYASST','CRMCYPROC','CRMCYBURG','CRMCYLARC','CRMCYMVEH','Shape_Area']

df = df[validCols]

df['bgareasqmeters'] = df['Shape_Area']
df = df.drop('Shape_Area',axis=1)

df['bg2010'] = df['ID']

df['ct2010'] = df['ID'].str[:11]


df.to_csv(workspace+outFile, index=False)

# test for count of 2010 tracts
# dfg = df.groupby('ct2010').sum()
# dfg.to_csv(workspace+'crime2010_bg_tract_test.csv', index=False)

shutil.copy2(workspace+outFile, outspace+outFile)

docs = '/Users/danielmsheehan/Dropbox/GIS/Data/Esri/CrimeIndexData2010/Documentation/'

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

copyanything(docs, outspace+'documentation/')


copyanything(outspace, '/Users/danielmsheehan/Dropbox/GIS/Exchange/Steve/esri_2010_crime/')