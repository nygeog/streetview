# Street View associating rated streets with Crashes (CrashStat & CrashMapper)


This project takes a set of inspected street segments, using the point of the start of the street segment as the intersection to be rated. Then the point is buffered at 30, 60 and 90 meters.

Using these buffers, simple count intersects were done for crashes involving bicyclists or pedestrians that result in injury or a fatality. The years of this crash data is from 1995 to 2013 (August). 


# Data Dictionary

### Simple Counts (Radial buffers intersected with Crash points):

symbol *** for ['r30', 'r60', 'r90'] Radial Buffers at 30, 60 and 90 Meters. 

symbol ###### for ['bikinj','bikkil','pedinj','pedkil'] Crashes with bicyclist involved with injuries, Crashes with bicyclist involved with fatalities, Crashes with pedestrian involved with injuries and Crashes with pedestrian involved with fatalities.

symbol ^^^^ for years 1995-2013 - including all years sum '1995_2013'. 


### Tasks to do

Update pedestrain proxy. up to 2009 for ALR. res dens. lu mix. 
Is ALR a raster or vector layer? 


### Projection Information:
All data is projected to NAD83 State Plane (Feet) New York Long Island. 

NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet
WKID: 2263 Authority: EPSG

Projection: Lambert_Conformal_Conic
False_Easting: 984250.0
False_Northing: 0.0
Central_Meridian: -74.0
Standard_Parallel_1: 40.66666666666666
Standard_Parallel_2: 41.03333333333333
Latitude_Of_Origin: 40.16666666666666
Linear Unit: Foot_US (0.3048006096012192)

Geographic Coordinate System: GCS_North_American_1983
Angular Unit: Degree (0.0174532925199433)
Prime Meridian: Greenwich (0.0)
Datum: D_North_American_1983
  Spheroid: GRS_1980
    Semimajor Axis: 6378137.0
    Semiminor Axis: 6356752.314140356
    Inverse Flattening: 298.257222101
