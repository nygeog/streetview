import pandas as pd

df = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/misc/list_of_blocks.csv', dtype={'BLKIDFP00': str})

dropfields = ['XCoord','YCoord','SEGID','STATEFP00','COUNTYFP00','TRACTCE00','BLOCKCE00','ALAND00','AWATER00']

df = df.drop(dropfields, axis=1)

df.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/just_blocks_2000.csv', index=False, header=False)