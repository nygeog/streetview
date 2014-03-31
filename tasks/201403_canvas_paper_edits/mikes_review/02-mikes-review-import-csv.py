import arcpy 

in_rows  = 'V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/streets_right_40_feet_blocks_2000_final.csv'
out_path = 'V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/mikes_review.gdb'
out_name = 'streets_right_40_feet_blocks_2000_final'

arcpy.TableToTable_conversion(in_rows, out_path, out_name)

in_rows  = 'V:/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/mikes_review/NationalSample.csv'
out_name = 'nationalsample'

arcpy.TableToTable_conversion(in_rows, out_path, out_name)