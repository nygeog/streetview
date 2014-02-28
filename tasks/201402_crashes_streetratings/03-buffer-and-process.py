import arcpy, csv
prjdir = 'V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data'

inpdir = prjdir + '/input'
prodir = prjdir + '/processing'
tabdir = prjdir + '/tables'
int_xy = inpdir + '/rated_intersections/rated_intersections.shp'
int_r_buf = inpdir + '/rated_intersections/r'

buf_dist = ['30','60','90'] #meters
crash_ty = ['bik_inj','bik_kil','ped_inj','ped_kil']

for bufdist in buf_dist:
	arcpy.Buffer_analysis(int_xy, int_r_buf+bufdist+'.shp', bufdist + ' Meters')

for bufdist in buf_dist:
	arcpy.Dissolve_management(int_r_buf+bufdist+'.shp', int_r_buf+bufdist+'_dis.shp', 'segmid')
for bufdist in buf_dist:
	arcpy.AddField_management(int_r_buf+bufdist+'_dis.shp', 'segmidtext','TEXT')
for bufdist in buf_dist:
	arcpy.CalculateField_management(int_r_buf+bufdist+'_dis.shp', 'segmidtext','"t"+str(!segmid!)','PYTHON_9.3')


#SPLIT ALL DELETE THIS CODE!!!! DNU DNU
# arcpy.Split_analysis("r90_dis","r90_dis","segmidtext","V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/processing/r90_split.gdb","#")
# arcpy.Split_analysis("r60_dis","r60_dis","segmidtext","V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/processing/r60_split.gdb","#")
# arcpy.Split_analysis("r30_dis","r30_dis","segmidtext","V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/processing/r30_split.gdb","#")

#Intersect1Input,Dissolve,EraseSourcewithDissolveasErase,Splittheintersectbyfeatures(split on itseflt ), run erase fc and alsop all the split feautres
for bufdist in buf_dist:
	arcpy.Intersect_analysis(int_r_buf+bufdist+'_dis.shp',int_r_buf+bufdist+'_dis_intself.shp',"ALL","#","INPUT")
for bufdist in buf_dist:
	arcpy.Dissolve_management(int_r_buf+bufdist+'_dis_intself.shp', int_r_buf+bufdist+'_dis_intself_dis.shp')
for bufdist in buf_dist:
	arcpy.Erase_analysis(int_r_buf+bufdist+'_dis.shp', int_r_buf+bufdist+'_dis_intself_dis.shp', int_r_buf+bufdist+'_dis_erase_ov.shp')
for bufdist in buf_dist:
	arcpy.Split_analysis(int_r_buf+bufdist+'_dis_intself.shp',int_r_buf+bufdist+'_dis_intself.shp',"segmidtext",inpdir + '/rated_intersections/r'+bufdist+'.gdb/',"#")




#for regular simple geo buffers counts

for bufdist in buf_dist:
	arcpy.DeleteField_management(int_r_buf+bufdist+'.shp', "segmid")

for bufdist in buf_dist:
	for crashty in crash_ty:
		arcpy.Intersect_analysis(inpdir+'/crashes/crashes.gdb/crashes_'+crashty+' #;'+inpdir+'/rated_intersections/r'+bufdist+'.shp #',prodir+'/crash_rat_int.gdb/r'+bufdist+'_'+crashty+'_int',"ALL","#","INPUT")






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