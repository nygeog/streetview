import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

print 'copy input data'
arcpy.FeatureClassToFeatureClass_conversion("W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp","Z:/GIS/201405_crime/data/input/homicides","homicides_2003_2011_valid_xy.shp","#","""LAT "LAT" true true false 19 Double 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,LAT,-1,-1;LONG "LONG" true true false 19 Double 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,LONG,-1,-1;inc_date "inc_date" true true false 8 Date 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,inc_date,-1,-1;inc_time "inc_time" true true false 8 Date 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,inc_time,-1,-1;boro "boro" true true false 254 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,boro,-1,-1;num_victim "num_victim" true true false 10 Double 0 10 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,num_victim,-1,-1;prim_motv "prim_motv" true true false 254 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,prim_motv,-1,-1;id "id" true true false 10 Double 0 10 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,id,-1,-1;weapon "weapon" true true false 254 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,weapon,-1,-1;lightdark "lightdark" true true false 254 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,lightdark,-1,-1;year "year" true true false 10 Double 0 10 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Homicides/homicides_2003_2011_valid_xy.shp,year,-1,-1""","#")
arcpy.FeatureClassToFeatureClass_conversion("W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp","Z:/GIS/201405_crime/data/input/census/2010/tracts","tl_2010_36_tract10.shp","#","""STATEFP10 "STATEFP10" true true false 2 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,STATEFP10,-1,-1;COUNTYFP10 "COUNTYFP10" true true false 3 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,COUNTYFP10,-1,-1;TRACTCE10 "TRACTCE10" true true false 6 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,TRACTCE10,-1,-1;GEOID10 "GEOID10" true true false 11 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,GEOID10,-1,-1;NAME10 "NAME10" true true false 7 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,NAME10,-1,-1;NAMELSAD10 "NAMELSAD10" true true false 20 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,NAMELSAD10,-1,-1;MTFCC10 "MTFCC10" true true false 5 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,MTFCC10,-1,-1;FUNCSTAT10 "FUNCSTAT10" true true false 1 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,FUNCSTAT10,-1,-1;ALAND10 "ALAND10" true true false 14 Double 0 14 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,ALAND10,-1,-1;AWATER10 "AWATER10" true true false 14 Double 0 14 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,AWATER10,-1,-1;INTPTLAT10 "INTPTLAT10" true true false 11 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,INTPTLAT10,-1,-1;INTPTLON10 "INTPTLON10" true true false 12 Text 0 0 ,First,#,W:/GIS/Data/Census/census_2010/tracts/tl_2010_36_tract10.shp,INTPTLON10,-1,-1""","#")
arcpy.FeatureClassToFeatureClass_conversion("W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp","Z:/GIS/201405_crime/data/input/census/2010/dcp_tracts","nyct2010.shp","#","""CTLabel "CTLabel" true true false 7 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,CTLabel,-1,-1;BoroCode "BoroCode" true true false 1 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,BoroCode,-1,-1;BoroName "BoroName" true true false 32 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,BoroName,-1,-1;CT2010 "CT2010" true true false 6 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,CT2010,-1,-1;BoroCT2010 "BoroCT2010" true true false 7 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,BoroCT2010,-1,-1;CDEligibil "CDEligibil" true true false 1 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,CDEligibil,-1,-1;PUMA "PUMA" true true false 4 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,PUMA,-1,-1;NTACode "NTACode" true true false 4 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,NTACode,-1,-1;NTAName "NTAName" true true false 75 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,NTAName,-1,-1;Shape_Leng "Shape_Leng" true true false 19 Double 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,Shape_Leng,-1,-1;Shape_Area "Shape_Area" true true false 19 Double 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,Shape_Area,-1,-1;geoid "geoid" true true false 254 Text 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,geoid,-1,-1;sq_km "sq_km" true true false 19 Double 0 0 ,First,#,W:/GIS/Data/Municipal/USA/New_York/New_York_City/Census/nyct2010_11a_av/nyct2010.shp,sq_km,-1,-1""","#")
print 'project ny state 2010 census tracts to stae plane nad 83 long island feet'
arcpy.Project_management("Z:/GIS/201405_crime/data/input/census/2010/tracts/tl_2010_36_tract10.shp","Z:/GIS/201405_crime/data/input/census/2010/tracts/tracts_2010","PROJCS['NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',984250.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-74.0],PARAMETER['Standard_Parallel_1',40.66666666666666],PARAMETER['Standard_Parallel_2',41.03333333333333],PARAMETER['Latitude_Of_Origin',40.16666666666666],UNIT['Foot_US',0.3048006096012192]]","#","GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
print 'area calc dcp tracts'
arcpy.AddField_management("Z:/GIS/201405_crime/data/input/census/2010/tracts/tracts_2010.shp","sq_meters","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management("Z:/GIS/201405_crime/data/input/census/2010/tracts/tracts_2010.shp","sq_meters","!shape.area@squaremeters!","PYTHON_9.3","#")
print 'select just nyc tracts'
arcpy.Select_analysis("Z:/GIS/201405_crime/data/input/census/2010/tracts/tracts_2010.shp","Z:/GIS/201405_crime/data/input/census/2010/tracts/tracts_2010_select_nyc.shp",""""COUNTYFP10" = '005' OR "COUNTYFP10" = '047' OR "COUNTYFP10" = '061' OR "COUNTYFP10" = '081' OR "COUNTYFP10" = '085'""")
print 'area calc dcp tracts'
arcpy.AddField_management("Z:/GIS/201405_crime/data/input/census/2010/dcp_tracts/nyct2010.shp","sq_meters","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.CalculateField_management("Z:/GIS/201405_crime/data/input/census/2010/dcp_tracts/nyct2010.shp","sq_meters","!shape.area@squaremeters!","PYTHON_9.3","#")

print 'select single years from 2005 - 2010'
for year in range(2005,2011):
	year = str(year)
	inFeature = "Z:/GIS/201405_crime/data/input/homicides/homicides_2003_2011_valid_xy.shp"
	outFeature= "Z:/GIS/201405_crime/data/processing/homicides/homicides.gdb/homicides_"+year
	Expression= """"year" = """ + year
	arcpy.Select_analysis(inFeature,outFeature,Expression)

print 'select range years 2005-2010 (6 years)'
inFeature = "Z:/GIS/201405_crime/data/input/homicides/homicides_2003_2011_valid_xy.shp"
outFeature= "Z:/GIS/201405_crime/data/processing/homicides/homicides.gdb/homicides_2005_2010"
Expression= """"year" = 2005 OR "year" = 2006 OR "year" = 2007 OR "year" = 2008 OR "year" = 2009 OR "year" = 2010"""
arcpy.Select_analysis(inFeature,outFeature,Expression)

years = ['2005','2006','2007','2008','2009','2010','2005_2010']
for year in years:
	inFeatures = "Z:/GIS/201405_crime/data/input/census/2010/tracts/tracts_2010_select_nyc.shp #;Z:/GIS/201405_crime/data/processing/homicides/homicides.gdb/homicides_"+year
	outFeatures    = "Z:/GIS/201405_crime/data/processing/homicides/homicides_int.gdb/homicides_"+year+"_tracts_2010"
	#arcpy.SpatialJoin_analysis(TargetFeatures,JoinFeatures,outFeatures,"JOIN_ONE_TO_ONE","KEEP_ALL","#","INTERSECT","#","#")
	arcpy.Intersect_analysis(inFeatures,outFeatures,"ALL","#","INPUT")

years = ['2005','2006','2007','2008','2009','2010','2005_2010']
for year in years:
	inFeatures = "Z:/GIS/201405_crime/data/processing/homicides/homicides_int.gdb/homicides_"+year+"_tracts_2010"
	outFeatures= "Z:/GIS/201405_crime/data/processing/homicides/homicides_int.gdb/homicides_"+year+"_tracts_2010_dis"
	arcpy.Dissolve_management(inFeatures,outFeatures,"GEOID10","num_victim SUM","MULTI_PART","DISSOLVE_LINES")

print 'export count tables'
#gdb = 'V:/GIS/projects/streetview/tasks/201405_crime/data/input/crime/esri.gdb/'
#odr = 'V:/GIS/projects/streetview/tasks/201405_crime/data/tables/'
gdb = 'Z:/GIS/201405_crime/data/processing/homicides/homicides_int.gdb/'
odr = 'Z:/GIS/201405_crime/data/tables/homicides_count/'

for year in years:
	item = 'homicides_'+year+'_tracts_2010_dis'
	table   = gdb + item
	outfile = odr + item + "_raw.csv"      
	#--first lets make a list of all of the fields in the table
	fields = arcpy.ListFields(table)
	field_names = [field.name for field in fields]
	with open(outfile,'wb') as f:
	    w = csv.writer(f)
	    #--write all field names to the output file
	    w.writerow(field_names)
	    #--now we make the search cursor that will iterate through the rows of the table
	    for row in arcpy.SearchCursor(table):
	        field_vals = [row.getValue(field.name) for field in fields]
	        w.writerow(field_vals)
	    del row
	print item + " raw export is complete"

print 'export census tracts data'
gdb = 'Z:/GIS/201405_crime/data/input/census/2010/tracts/'
odr = 'Z:/GIS/201405_crime/data/tables/census/'

item = 'tracts_2010_select_nyc'
table   = gdb + item + '.shp'
outfile = odr + item + "_raw.csv"      
#--first lets make a list of all of the fields in the table
fields = arcpy.ListFields(table)
field_names = [field.name for field in fields]
with open(outfile,'wb') as f:
    w = csv.writer(f)
    #--write all field names to the output file
    w.writerow(field_names)
    #--now we make the search cursor that will iterate through the rows of the table
    for row in arcpy.SearchCursor(table):
        field_vals = [row.getValue(field.name) for field in fields]
        w.writerow(field_vals)
    del row
print item + " raw export is complete"

print 'export dcp census tracts data'
gdb = 'Z:/GIS/201405_crime/data/input/census/2010/dcp_tracts/'
odr = 'Z:/GIS/201405_crime/data/tables/census/'

item = 'nyct2010'
table   = gdb + item + '.shp'
outfile = odr + item + "_raw.csv"      
#--first lets make a list of all of the fields in the table
fields = arcpy.ListFields(table)
field_names = [field.name for field in fields]
with open(outfile,'wb') as f:
    w = csv.writer(f)
    #--write all field names to the output file
    w.writerow(field_names)
    #--now we make the search cursor that will iterate through the rows of the table
    for row in arcpy.SearchCursor(table):
        field_vals = [row.getValue(field.name) for field in fields]
        w.writerow(field_vals)
    del row
print item + " raw export is complete"