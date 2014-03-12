import arcpy
import os

folder = 'U:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/blocks/'

arcpy.CreateFileGDB_management("U:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input","census","CURRENT")

def fcs_in_workspace(workspace):
  arcpy.env.workspace = workspace
  for fc in arcpy.ListFeatureClasses():
    yield os.path.join(workspace, fc)
  for ws in arcpy.ListWorkspaces():
    for fc in fcs_in_workspace(os.path.join(workspace, ws)):
        yield fc

fcSet = []
for fc in fcs_in_workspace(folder):
	fcSet.append(fc.encode('ascii', 'ignore'))
	print fc 

print fcSet

arcpy.Merge_management(fcSet, "U:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/census.gdb/blocks_2000")