import re, urllib, time, zipfile, os

download_location = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/input/blocks/'

stop_time = 3

state_fips = ["01","02","04","05","06","08","09","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","44","45","46","47","48","49","50","51","53","54","55","56","72"]

for i in state_fips:
	url = 'http://www2.census.gov/geo/tiger/TIGER2010/TABBLOCK/2000/tl_2010_'+i+'_tabblock00.zip'
	outzip = download_location + 'tl_2010_'+i+'_tabblock00.zip'
	print 'downloading... ' + url
	urllib.urlretrieve(url, outzip)
	print 'unzipping... ' + outzip
	zipfile.ZipFile(outzip).extractall(download_location)
	#os.remove(download_location+outzip)
	#print "Deleting... " + stfi + "'s ZIP file"

	#wait 3 seconds in case network connection is slow
	time.sleep(stop_time)
