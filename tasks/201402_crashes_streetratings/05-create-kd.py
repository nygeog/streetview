import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

proj_path = "V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/"
pp = proj_path
pd = pp + 'data'

# print 'clip by borough boundary'
# arcpy.Clip_analysis(pd+"/input/crashes/crashes.gdb/crashes_bik_inj",pd+"/input/borough_boundary/nybb_12a_av/nybb.shp",pd+"/processing/kd.gdb/crashes_bik_inj_1995_2013","#")
# arcpy.Clip_analysis(pd+"/input/crashes/crashes.gdb/crashes_bik_kil",pd+"/input/borough_boundary/nybb_12a_av/nybb.shp",pd+"/processing/kd.gdb/crashes_bik_kil_1995_2013","#")
# arcpy.Clip_analysis(pd+"/input/crashes/crashes.gdb/crashes_ped_inj",pd+"/input/borough_boundary/nybb_12a_av/nybb.shp",pd+"/processing/kd.gdb/crashes_ped_inj_1995_2013","#")
# arcpy.Clip_analysis(pd+"/input/crashes/crashes.gdb/crashes_ped_kil",pd+"/input/borough_boundary/nybb_12a_av/nybb.shp",pd+"/processing/kd.gdb/crashes_ped_kil_1995_2013","#")

# print 'crash types subset by year and type'
# crashtypes = ['bik_inj','bik_kil','ped_inj','ped_kil']
# for crashtype in crashtypes:
# 	for i in range(1995, 2014):
# 		i_s  = str(i)
# 		exp  = '"year" = ' + i_s
# 		arcpy.Select_analysis(pd+'/processing/kd.gdb/crashes_'+crashtype+'_1995_2013',pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s, exp)

print 'import spatial analyst'
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

print 'kd for crashes by type and by year'
crashtypes = ['bik_inj','bik_kil','ped_inj','ped_kil']

cellSize               = 50 #50 feet since these are small 30 meter buffers
searchRadius           = 3280.83
area_unit_scale_factor = "SQUARE_KILOMETERS"

for crashtype in crashtypes:
	populationField = crashtype
	for i in range(1995, 2014):
		i_s  = str(i)
		inFeatures = pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s
		outKernelDensity = KernelDensity(inFeatures, populationField, cellSize, searchRadius, area_unit_scale_factor)
		outKernelDensity.save(pd+'/processing/kd.gdb/crashes_'+crashtype+'_'+i_s+'_kd')

for crashtype in crashtypes:
	populationField = crashtype
	inFeatures = pd+'/processing/kd.gdb/crashes_'+crashtype+'_1995_2013'
	outKernelDensity = KernelDensity(inFeatures, populationField, cellSize, searchRadius, area_unit_scale_factor)
	outKernelDensity.save(pd+'/processing/kd.gdb/crashes_'+crashtype+'_1995_2013_kd')



