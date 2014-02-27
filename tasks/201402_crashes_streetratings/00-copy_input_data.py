import time, datetime, csv, sys, traceback
# import arcpy
# from arcpy import env
# env.overwriteOutput = True
import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

copyanything('/Users/danielmsheehan/Dropbox/GIS/Data/Municipal/USA/New_York/New_York_City/Crashes/crashes.gdb', '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/input/crashes/crashes.gdb')

