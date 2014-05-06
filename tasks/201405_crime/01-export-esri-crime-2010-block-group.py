import arcpy, time, datetime, csv, sys, traceback, os
from arcpy import env
env.overwriteOutput = True

gdb = 'W:/GIS/Data/Esri/CrimeIndexData2010/Data/BGCrimeIndex2010.gdb/'
odr = 'V:/GIS/projects/streetview/tasks/201405_crime/data/tables/'

item = 'CRIME10_BG'

table   = gdb + item
outfile = odr + item.lower() + "_raw.csv"      

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