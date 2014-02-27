import arcpy, csv
prjdir = 'V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data'

inpdir = prjdir + '/input'
prodir = prjdir + '/processing'
tabdir = prjdir + '/tables'
int_xy = inpdir + '/rated_intersections/rated_intersections.shp'
int_r_buf = inpdir + '/rated_intersections/r'

buf_dist = ['30','60','90'] #meters
crash_ty = ['bik_inj','bik_kil','ped_inj','ped_kil']

# for bufdist in buf_dist:
# 	arcpy.Buffer_analysis(int_xy, int_r_buf+bufdist, bufdist + ' Meters')

# for bufdist in buf_dist:
# 	for crashty in crash_ty:
# 		arcpy.Intersect_analysis(inpdir+'/crashes/crashes.gdb/crashes_'+crashty+' #;'+inpdir+'/rated_intersections/r'+bufdist+'.shp #',prodir+'/crash_rat_int.gdb/r'+bufdist+'_'+crashty+'_int',"ALL","#","INPUT

#----- Export all tables to csvs
print 'export all geos to csv at:' +  time.strftime('%c') + ' - 1 minute'
for bufdist in buf_dist:
	for crashty in crash_ty:
		table   = prodir+'/crash_rat_int.gdb/r'+bufdist+'_'+crashty+'_int'
		outfile = tabdir+'/rated_intersections_crashes_int/r'+bufdist+'_'+crashty+'_int_raw.csv'      

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
		print bufdist+'_'+crashty + " raw export is complete"