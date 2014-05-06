import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

gdb = 'V:/GIS/projects/streetview/tasks/201405_crime/data/input/crime/esri.gdb/'
odr = 'V:/GIS/projects/streetview/tasks/201405_crime/data/tables/'

item = 'crime2010_bg'

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