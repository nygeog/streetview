import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

proj_path = "U:/GIS/projects/streetview/tasks/201402_crashes_streetratings/"
pp = proj_path
pd = pp + 'data'

bufs = ['r30','r60','r90']
crashtypes = ['bik_inj','bik_kil','ped_inj','ped_kil']
#----- Export all tables to csvs
# print 'export all geos to csv at:' +  time.strftime('%c') + ' - 3 minutes'
# for buf in bufs:
# 	for crashtype in crashtypes:
# 		for i in range(1995, 2014):
# 			i_s  = str(i)
# 			table   = pd+'/processing/zonal_stats.gdb/'+buf+'_'+crashtype+'_'+i_s+'_zon'
# 			outfile = pd+'/tables/kd/'+buf+'_'+crashtype+'_'+i_s+'_zon.csv'  

# 			#--first lets make a list of all of the fields in the table
# 			fields = arcpy.ListFields(table)
# 			field_names = [field.name for field in fields]

# 			with open(outfile,'wb') as f:
# 			    w = csv.writer(f)
# 			    #--write all field names to the output file
# 			    w.writerow(field_names)

# 			    #--now we make the search cursor that will iterate through the rows of the table
# 			    for row in arcpy.SearchCursor(table):
# 			        field_vals = [row.getValue(field.name) for field in fields]
# 			        w.writerow(field_vals)
# 			    del row
# 			print buf+'_'+crashtype + i_s + " raw export is complete"

# print 'export all geos to csv at:' +  time.strftime('%c') + ' - 1 minute'
# for buf in bufs:
# 	for crashtype in crashtypes:
# 		table   = pd+'/processing/zonal_stats.gdb/'+buf+'_'+crashtype+'_1995_2013_zon'
# 		outfile = pd+'/tables/kd/'+buf+'_'+crashtype+'_1995_2013_zon.csv'  

# 		#--first lets make a list of all of the fields in the table
# 		fields = arcpy.ListFields(table)
# 		field_names = [field.name for field in fields]

# 		with open(outfile,'wb') as f:
# 		    w = csv.writer(f)
# 		    #--write all field names to the output file
# 		    w.writerow(field_names)

# 		    #--now we make the search cursor that will iterate through the rows of the table
# 		    for row in arcpy.SearchCursor(table):
# 		        field_vals = [row.getValue(field.name) for field in fields]
# 		        w.writerow(field_vals)
# 		    del row
# 		print buf+'_'+crashtype + i_s + " raw export is complete"


#----- Export all tables to csvs
print 'export all split geos to csv at:' +  time.strftime('%c') + ' - 3 minutes'
for buf in bufs:
	for crashtype in crashtypes:
		for i in range(1995, 2014):
			i_s  = str(i)
			table   = pd+'/processing/zonal_stats_splits_merged.gdb/'+buf+'_'+crashtype+'_'+i_s
			outfile = pd+'/tables/kd_splits/'+buf+'_'+crashtype+'_'+i_s+'_zon.csv'  

			#--first lets make a list of all of the fields in the table
			fields = arcpy.ListFields(table)
			field_names = [field.name for field in fields]

			with open(outfile,'wb') as f:
			    w = csv.writer(f)
			    #--write all field names to the output file
			    w.writerow(field_names)

			    try:

		    	#--now we make the search cursor that will iterate through the rows of the table
				    for row in arcpy.SearchCursor(table):
				        	
				        field_vals = [row.getValue(field.name) for field in fields]
				        w.writerow(field_vals)
				    del row
			    except:
					print 'missing'
			    

			print buf+'_'+crashtype + i_s + " raw export is complete"

print 'export all split geos to csv at:' +  time.strftime('%c') + ' - 1 minute'
for buf in bufs:
	for crashtype in crashtypes:
		table   = pd+'/processing/zonal_stats_splits_merged.gdb/'+buf+'_'+crashtype+'_1995_2013'
		outfile = pd+'/tables/kd_splits/'+buf+'_'+crashtype+'_1995_2013_zon.csv'  

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
		print buf+'_'+crashtype + i_s + " raw export is complete"