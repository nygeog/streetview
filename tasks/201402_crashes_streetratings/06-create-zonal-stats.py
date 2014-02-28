import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

proj_path = "V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/"
pp = proj_path
pd = pp + 'data'
prjdir = 'V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data'
inpdir = prjdir + '/input'
prodir = prjdir + '/processing'
tabdir = prjdir + '/tables'
int_xy = inpdir + '/rated_intersections/rated_intersections.shp'
int_r_buf = inpdir + '/rated_intersections/r'

print 'import spatial analyst'
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

siyears     = range(1995, 2014)
alyears     = ['1995_2013']
years       = alyears + siyears
crashtypes = ['bik_inj','bik_kil','ped_inj','ped_kil']

print 'zonal stats on the non-overlapping features'
buf_dist = ['30','60','90']
for buf in buf_dist:
	for crashtype in crashtypes:
		for i in years:
			i_s  = str(i)
			arcpy.gp.ZonalStatisticsAsTable_sa(int_r_buf+buf+'_dis_erase_ov.shp',"segmid",pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s+'_kd',pd+'/processing/zonal_stats.gdb/r'+buf+'_'+crashtype+'_'+i_s+'_zon',"DATA","ALL")
			print buf + crashtype + i_s + ' is done...' + time.strftime('%c') 

#What's next is to just do the inputs that were put into the bufs gdbs (these are the splits)
#put them in the processing r30_split, r60_split, r90_split, then figure out how to merge the tables/data. 

print 'now zonal stats on the features that overlap'
siyears     = range(1995, 2014)
alyears     = ['1995_2013']
years       = alyears + siyears

buf = '30'
env.workspace = pd+"/input/rated_intersections/r"+buf+".gdb"
fcList = arcpy.ListFeatureClasses()
arcpy.env.extent = "MAXOF"
print 'zonal stats runs - XX hour'
for x in fcList:
	for crashtype in crashtypes:
		for i in years:
			i_s  = str(i)
			arcpy.gp.ZonalStatisticsAsTable_sa(pd+"/input/rated_intersections/r"+buf+".gdb/"+x,"segmid",pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s+'_kd',pd+'/processing/r'+buf+'_split.gdb/'+x+'_'+crashtype+'_'+i_s+'_zon',"DATA","ALL")
	print x + ' is done...' + time.strftime('%c') 

buf = '60'
env.workspace = pd+"/input/rated_intersections/r"+buf+".gdb"
fcList = arcpy.ListFeatureClasses()
arcpy.env.extent = "MAXOF"
print 'zonal stats runs - XX hour'
for x in fcList:
	for crashtype in crashtypes:
		for i in years:
			i_s  = str(i)
			arcpy.gp.ZonalStatisticsAsTable_sa(pd+"/input/rated_intersections/r"+buf+".gdb/"+x,"segmid",pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s+'_kd',pd+'/processing/r'+buf+'_split.gdb/'+x+'_'+crashtype+'_'+i_s+'_zon',"DATA","ALL")
	print x + ' is done...' + time.strftime('%c') 

buf = '90'
env.workspace = pd+"/input/rated_intersections/r"+buf+".gdb"
fcList = arcpy.ListFeatureClasses()
arcpy.env.extent = "MAXOF"
print 'zonal stats runs - XX hour'
for x in fcList:
	for crashtype in crashtypes:
		for i in years:
			i_s  = str(i)
			arcpy.gp.ZonalStatisticsAsTable_sa(pd+"/input/rated_intersections/r"+buf+".gdb/"+x,"segmid",pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s+'_kd',pd+'/processing/r'+buf+'_split.gdb/'+x+'_'+crashtype+'_'+i_s+'_zon',"DATA","ALL")
	print x + ' is done...' + time.strftime('%c') 





print 'now time to merge all the split zonal stats tables into one table per year per crash type'
siyears     = range(1995, 2014)
alyears     = ['1995_2013']
years       = alyears + siyears
buf_dist = ['30','60','90']

path = "V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/processing/r"
mid  = '_split.gdb/'

for buf in buf_dist:
	buf = str(buf)
	env.workspace = pd+"/input/rated_intersections/r"+buf+".gdb"
	for crashtype in crashtypes:
		for year in years:
			year = str(year)
			fcList = arcpy.ListFeatureClasses()
			inFCs = [] 
			for i in fcList:
				inFCs.append(path+buf+mid+i.encode("utf-8") + '_' + crashtype + '_' + year + '_zon')
			
			print inFCs
			arcpy.Merge_management(inFCs, "V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/processing/zonal_stats_splits_merged.gdb/r"+buf+'_'+crashtype+'_'+year)


			print buf + crashtype + year


