import pandas as pd


dfpop = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/streets_right_40_feet_blocks_2000_select_with_pop.csv', dtype={'FIPS': object})
dfpop = dfpop.drop('BLKIDFP00', axis=1)

dfcen = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census/census_2010_block.csv', dtype={'geoid': object})

merged = dfpop.merge(dfcen, left_on='FIPS', right_on='geoid', how='left')

merged.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/streets_right_40_feet_blocks_2000_select_with_pop_census_data.csv', index=False)