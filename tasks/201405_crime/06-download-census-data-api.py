import urllib2
import json
import csv
import sys, re, time
import shutil

pause = 1

proj_path = '/Users/danielmsheehan/GIS/201405_crime/'
pp = proj_path
pd = pp + 'data'

totpop = ["P0010001"]

variabletypelist   =[ totpop ]
variabletypelistnm =['totpop']

for topic, topicnm in zip(variabletypelist, variabletypelistnm):
	#----
	print 'OKAY NOW RUN THE API GRABS'

	print 'get '+topicnm+' vars'
	allcensusvars   = ','.join(topic)
	censusapipreurl = "http://api.census.gov/data/2010/sf1?key="
	censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
	gettxt          = "&get="
	forgeog         = "&for=tract:*"
	instate         = "&in=state:36"
	url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
	print url
	data = urllib2.urlopen(url).read()
	data = json.loads(data)
	fname = pd+"/input/census/sf1/working/sf1_2010_tract_st36_"+topicnm+".csv"
	with open(fname,'wb') as outf:
	    outcsv = csv.writer(outf)
	    outcsv.writerows(data)
	shutil.copy2(pd+"/input/census/sf1/working/sf1_2010_tract_st36_"+topicnm+".csv", pd+"/tables/census/sf1_2010_tract_st36_"+topicnm+".csv")
	time.sleep(pause)
	#----
