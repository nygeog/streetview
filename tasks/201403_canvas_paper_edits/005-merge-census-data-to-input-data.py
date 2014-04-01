import pandas as pd

dfnat = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/_original/NationalSample.csv')

dfblo = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/misc/list_of_blocks.csv', dtype={'BLKIDFP00': object})

dfcen = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census/census_2010_block.csv', dtype={'geoid': object})


merged1 = dfblo.merge(dfcen, left_on='BLKIDFP00', right_on='geoid', how='left')

merged1 = merged1.drop(['XCoord','YCoord'], axis=1)

merged1.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/streets_right_40_feet_blocks_2000_select_with_pop_census_data.csv', index=False)
