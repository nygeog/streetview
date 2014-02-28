import arcpy, os, sys, string
from arcpy import env
arcpy.CheckOutExtension("spatial")
env.overwriteOutput = True

proj_path = "V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/"
pp = proj_path
pd = pp + 'data'

def CreateDirectory(DBF_dir):
    if not os.path.exists(DBF_dir):
        os.mkdir(DBF_dir)
        print "created directory {0}".format(DBF_dir)
        
def ZonalStasAsTable(fc,DBF_dir,raster,zoneField):
    
    for row in arcpy.SearchCursor(fc):
        lyr = "Zone_{0}_lyr".format(row.OBJECTID)
        tempTable = DBF_dir + os.sep + "zone_{0}.dbf".format(row.OBJECTID)
        arcpy.MakeFeatureLayer_management(fc, lyr, "\"OBJECTID\" = {0}".format(row.OBJECTID))
        print "Creating layer {0}".format(lyr)
        out_layer = DBF_dir + os.sep + lyr + ".lyr"
        arcpy.SaveToLayerFile_management(lyr, out_layer, "ABSOLUTE")
        print "Saved layer file"
        arcpy.gp.ZonalStatisticsAsTable_sa(out_layer, zoneField, raster, tempTable, "DATA", "ALL")                             
        print "Populating zonal stats for {0}".format(lyr)
    del row, lyr
        
def MergeTables(DBF_dir,zstat_table):
    arcpy.env.workspace = DBF_dir
    tableList = arcpy.ListTables()      
    arcpy.Merge_management(tableList,zstat_table)
    print "Merged tables. Final zonalstat table {0} created. Located at {1}".format(zstat_table,DBF_dir)
    del tableList


if __name__ == "__main__":
    print 'zonal stats runs - 1 hour'
    bufs = ['r30','r60','r90']
    crashtypes = ['bik_inj','bik_kil','ped_inj','ped_kil']
    siyears     = range(1995, 2014)
    alyears     = ['1995_2013']
    years       = alyears + siyears
    for buf in bufs:
        for crashtype in crashtypes:
            for i in years:
                i_s  = str(i)
                inFeature   = pd+'/input/rated_intersections/buffers.gdb/'+buf
                inRaster    = pd+'/processing/kd/crashes_'+crashtype+'_'+i_s+'_kd.img'
                ZoneID      = 'svsuid'
                WorkSpace   = pd+'/kd_ws'


                ws = WorkSpace
                DBF_dir = ws + os.sep + 'kd_dbf/'
                fc = inFeature
                raster = inRaster
                zoneField = ZoneID
                zstat_table = DBF_dir + os.sep + buf + '_' +crashtype + '_' + i_s + '_kd_zon_n.dbf'

                CreateDirectory(DBF_dir)
                ZonalStasAsTable(fc,DBF_dir,raster,zoneField)
                MergeTables(DBF_dir,zstat_table)


