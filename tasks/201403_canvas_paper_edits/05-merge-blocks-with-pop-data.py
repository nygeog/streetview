import pandas as pd
import re, urllib, time, zipfile, os

dfpop = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/blocks_2000_esri_pop.txt', dtype=str)

dfstreets = pd.read_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/streets_right_40_feet_blocks_2000_select.txt', dtype=str)

streetsdrops = ['OBJECTID','FID_streets_right_buffer_40_ft_centroid','DYNAMAP_ID','PREFIX','PRETYPE','NAME','TYPE','SUFFIX','NAME_TYPE','NAME_FLAG','PREFIX1','PRETYPE1','NAME1','TYPE1','SUFFIX1','NAME_TYPE1','NAME_FLAG1','PREFIX2','PRETYPE2','NAME2','TYPE2','SUFFIX2','NAME_TYPE2','NAME_FLAG2','PREFIX3','PRETYPE3','NAME3','TYPE3','SUFFIX3','NAME_TYPE3','NAME_FLAG3','PREFIX4','PRETYPE4','NAME4','TYPE4','SUFFIX4','NAME_TYPE4','NAME_FLAG4','PREFIX5','PRETYPE5','NAME5','TYPE5','SUFFIX5','NAME_TYPE5','NAME_FLAG5','L_F_ADD_INT','L_T_ADD_INT','R_F_ADD_INT','R_T_ADD_INT','POSTAL_L','POSTAL_R','FCC','ACC','SHIELD','HWY_NUM','SPEED','ONE_WAY','TOLL','STATUS','F_ZLEV','T_ZLEV','FT_DIR','TF_DIR','ROADCLASS','PLACENAME_L','PLACENAME_R','STATE_L','STATE_R','STATE','COUNTRY','RENDERCL','FULLNAME','SHIELD_CL','SHIELD_LBL','All_Near_Points_IN_FID','All_Near_Points_NEAR_FID','All_Near_Points_NEAR_DIST','All_Near_Points_NEAR_X','All_Near_Points_NEAR_Y','All_Near_Points_Tract','Start_X_DD','Start_Y_DD','End_X_DD','End_Y_DD','STFID','SAMPORD','GEO2000','MSACMA99','PLACE','STABBR','UPLACE98','CCITY0','MERGEPLC','URBRAND','RANDNU','Type_1','BUFF_DIST','ORIG_FID','FID_blocks_2000_select_40_feet','NAME00','MTFCC00','UR00','UACE00','FUNCSTAT00','ALAND00','AWATER00','INTPTLAT00','INTPTLON00']

dfstreets = dfstreets.drop(streetsdrops, axis=1)

dfpopid = 'FIPS'
dfstreetsid = 'BLKIDFP00'

merged = dfpop.merge(dfstreets, left_on=dfpopid, right_on=dfstreetsid, how='right')

merged = merged.drop(['ObjectID','STATE_FIPS','CNTY_FIPS','STCOFIPS','TRACT','BLOCK','STATEFP00','COUNTYFP00','TRACTCE00','BLOCKCE00'], axis=1)

merged.to_csv('/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/streets_right_40_feet_blocks_2000_select_with_pop.csv', index=False)