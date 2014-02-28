import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

proj_path = "V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/"
pp = proj_path
pd = pp + 'data'

print 'import spatial analyst'
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

siyears     = range(1995, 2014)
alyears     = ['1995_2013']
years       = alyears + siyears
crashtypes = ['bik_inj','bik_kil','ped_inj','ped_kil']


buf = '30'
env.workspace = pd+"/processing/r"+buf+"_split.gdb"
fcList = arcpy.ListFeatureClasses()
arcpy.env.extent = "MAXOF"
last = len(fcList)

print 'zonal stats runs - XX hour'
for x in fcList:
	for crashtype in crashtypes:
		for i in range(1995, 2014):
			i_s  = str(i)
			arcpy.gp.ZonalStatisticsAsTable_sa(pd+'/processing/r'+buf+'_split.gdb/'+x,"segmidtext",pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s+'_kd',pd+'/processing/r'+buf+'_split.gdb/'+x+'_'+crashtype+'_'+i_s+'_zon',"DATA","ALL")
	print x + ' is done...' + time.strftime('%c') 
#holy shit started this for all features in the fc list!!!!!!!

