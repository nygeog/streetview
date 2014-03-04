from qgis.analysis import QgsZonalStatistics

proj_path = "V:/GIS/projects/streetview/tasks/201402_crashes_streetratings/"
pp = proj_path
pd = pp + 'data'

kd = '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/processing/kd/crashes_bik_inj_1995_2013_kd.img'
infc = '/Volumes/Echo/GIS/projects/streetview/tasks/201402_crashes_streetratings/data/input/rated_intersections/r30.shp'
#specify polygon shapefile vector
polygonLayer = QgsVectorLayer(infc, 'zonepolygons', "ogr") 

# specify raster filename
rasterFilePath = kd #'F:/temp/zonalstat/raster1.tif'

# usage - QgsZonalStatistics (QgsVectorLayer *polygonLayer, const QString &rasterFile, const QString &attributePrefix="", int rasterBand=1)
zoneStat = QgsZonalStatistics (polygonLayer, rasterFilePath, 'pre-', 1)
zoneStat.calculateStatistics(None)