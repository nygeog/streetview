import pandas as pd
import csv
import urllib2
import json
import sys, re, time

proj_path = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/'
pp = proj_path
pd = pp + 'data'

infile = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/data/processing/just_blocks_2000.csv'

# reader = csv.reader(infile)
# for row in reader:
# 	print row

cr = csv.reader(open(infile,"rb"))
tractIDlist = []
statelist = []
countylist= []
tractlist = []

pauser = .01

for row in cr:    
    
    state = str(row)[2:4]
    county= str(row)[4:7]
    tract = str(row)[7:13]
    tractID = str(row)[2:17]

    tractIDlist.append(tractID)
    statelist.append(state)
    countylist.append(county)
    tractlist.append(tract)
    
print tractIDlist
print statelist
print countylist
print tractlist

#from Mike
#Percentage of racial and ethnic groups (N.H. black, N.H. white, and Latino mainly). 
#I can't remember if SF-1 has any data on owner-occupancy or vacancy rates.
#But racial composition is the most important.

#-----census 2010 Pop, Race, Hispanic
listofcensusvars= [
#Population
"P001001",
#Race
"P003001",
"P003002",
"P003003",
"P003004",
"P003005",
"P003006",
"P003007",
"P003008",
"P003009",
#Hispanic
"P004001",
"P004002",
"P004003",
"P004004",
"P004005",
"P004006",
"P004007",
"P004008",
"P004009",
"P004010",
"P004011",
"AREALAND",
"AREAWATR"
]

for state, county, tract in zip(statelist, countylist, tractlist):
	print 'state ' + state + ' county ' + county + ' tract ' + tract
		
	censusapipreurl = "http://api.census.gov/data/2000/sf1?key="
	censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
	gettxt          = "&get="
	allcensusvars   = ','.join(listofcensusvars)
	forgeog         = "&for=block:*"
	instate         = "&in=state:"+state+"+county:"+county+"+tract:"+tract

	url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
	print url

	data = urllib2.urlopen(url).read()
	data = json.loads(data)

	fname = pd+"/input/census/census/"+state+county+tract+"_pop_race_hisp_census_2000_block.csv"
	with open(fname,'wb') as outf:
	    outcsv = csv.writer(outf)
	    outcsv.writerows(data)

	time.sleep(pauser)  

#-----census 2010 Housing Units	
listofcensusvars= [
#TotalHousingUnits
"H001001",
#OccupancyStatus
"H003001",
"H003002",
"H003003",
#Tenure
"H004001",
"H004002",
"H004003",
#VacancyStatus
"H005001",
"H005002",
"H005003",
"H005004",
"H005005",
"H005006",
"H005007",
]

for state, county, tract in zip(statelist, countylist, tractlist):
	print 'state ' + state + ' county ' + county + ' tract ' + tract
		
	censusapipreurl = "http://api.census.gov/data/2000/sf1?key="
	censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
	gettxt          = "&get="
	allcensusvars   = ','.join(listofcensusvars)
	forgeog         = "&for=block:*"
	instate         = "&in=state:"+state+"+county:"+county+"+tract:"+tract

	url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
	print url

	data = urllib2.urlopen(url).read()
	data = json.loads(data)

	fname = pd+"/input/census/census/"+state+county+tract+"_housing_census_2000_block.csv"
	with open(fname,'wb') as outf:
	    outcsv = csv.writer(outf)
	    outcsv.writerows(data)

	time.sleep(pauser)  