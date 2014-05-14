import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

print 'import spatial analyst'
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

# James Quinn Jan 03, 2014 12:08:57
# All the kernel density grids in the aforementioned directories were created using the following parameters:
# Output Cell Size: 150x150-feet
#  Search Radius: 1-kilometer (3280.83)
#  Output Area Units: Square Kilometers

cellSize               = 150
searchRadius           = 3280.83
area_unit_scale_factor = "SQUARE_KILOMETERS"

print 'kd for homicides by year'
populationField = 'num_victim'

years = ['2005','2006','2007','2008','2009','2010','2005_2010']
for year in years:
 	inFeatures = "Z:/GIS/201405_crime/data/processing/homicides/homicides.gdb/homicides_"+year
 	outKernelDensity = KernelDensity(inFeatures, populationField, cellSize, searchRadius, area_unit_scale_factor)
 	outKernelDensity.save("Z:/GIS/201405_crime/data/processing/homicides/homicides_kd.gdb/homicides_"+year)

years = ['2005','2006','2007','2008','2009','2010','2005_2010']
for year in years:
	inFeatureZone = "Z:/GIS/201405_crime/data/input/census/2010/dcp_tracts/nyct2010.shp"
	zoneField     = "geoid"
	inValRaster   = "Z:/GIS/201405_crime/data/processing/homicides/homicides_kd.gdb/homicides_"+year
	outRaster     = "Z:/GIS/201405_crime/data/processing/homicides/homicides_zs.gdb/homicides_"+year+"_tracts_2010"
	arcpy.gp.ZonalStatistics_sa(inFeatureZone,zoneField,inValRaster,outRaster,"MEAN","DATA")

years = ['2005','2006','2007','2008','2009','2010','2005_2010']
for year in years:
	inFeatureZone = "Z:/GIS/201405_crime/data/input/census/2010/dcp_tracts/nyct2010.shp"
	zoneField     = "geoid"
	inValRaster   = "Z:/GIS/201405_crime/data/processing/homicides/homicides_kd.gdb/homicides_"+year
	outTable      = "Z:/GIS/201405_crime/data/processing/homicides/homicides_zs.gdb/homicides_"+year+"_tracts_2010_table"
	arcpy.gp.ZonalStatisticsAsTable_sa(inFeatureZone,zoneField,inValRaster,outTable,"DATA","ALL")

print 'export count tables'
#gdb = 'V:/GIS/projects/streetview/tasks/201405_crime/data/input/crime/esri.gdb/'
#odr = 'V:/GIS/projects/streetview/tasks/201405_crime/data/tables/'
gdb = 'Z:/GIS/201405_crime/data/processing/homicides/homicides_zs.gdb/'
odr = 'Z:/GIS/201405_crime/data/tables/homicides_zonal_stats/'

for year in years:
	item = "homicides_"+year+"_tracts_2010_table"
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