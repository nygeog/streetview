import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

out_path = 'V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/nationalsample.gdb'

in_rows  = 'V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/_original/NationalSample.csv'
out_name = 'nationalsample'

arcpy.TableToTable_conversion(in_rows, out_path, out_name)

inxytable = "V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/nationalsample.gdb/nationalsample"
outlinefc = "V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/nationalsample.gdb/nationalsample_street_segments"

arcpy.XYToLine_management(inxytable,outlinefc,"startlon","startlat","endlon","endlat","GEODESIC","segid","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision")

outbuffer = "V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/intersect_streets_census_blocks.gdb/streets_right_buffer_40_ft"
arcpy.Buffer_analysis(outlinefc,outbuffer,"40 Feet","RIGHT","FLAT","NONE","#")

outcentroid = "V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/intersect_streets_census_blocks.gdb/streets_right_buffer_40_ft_centroid"
arcpy.FeatureToPoint_management(outbuffer,outcentroid,"INSIDE")

blocks = 'V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census.gdb/blocks_2000'
infeatures = [outcentroid, blocks]
outfeature = "V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/intersect_streets_census_blocks.gdb/streets_right_40_feet_blocks_2000_select"
arcpy.Intersect_analysis(infeatures,outfeature,"ALL","#","INPUT")

arcpy.ExportXYv_stats(outfeature,"segid;STATEFP00;COUNTYFP00;TRACTCE00;BLOCKCE00;BLKIDFP00;ALAND00;AWATER00","COMMA","V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/misc/list_of_blocks.csv","ADD_FIELD_NAMES")


