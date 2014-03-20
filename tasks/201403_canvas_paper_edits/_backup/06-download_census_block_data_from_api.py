import urllib2
import json
import csv
import sys, re, time

proj_path = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/'
pp = proj_path
pd = pp + 'data'

pauser = .01

print 'downloading census block data for each tract in each nyc county - 15 minutes'



for county, tracts in zip(counties, tracts_county):
	for tract in tracts:

		#-----census 2010 Pop, Race, Hispanic

		listofcensusvars= [
		#Population
		"P0010001",
		#Race
		"P0030001",
		"P0030002",
		"P0030003",
		"P0030004",
		"P0030005",
		"P0030006",
		"P0030007",
		"P0030008",
		#Hispanic
		"P0040001",
		"P0040002",
		"P0040003"
		]

		censusapipreurl = "http://api.census.gov/data/2010/sf1?key="
		censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
		gettxt          = "&get="
		allcensusvars   = ','.join(listofcensusvars)
		forgeog         = "&for=block:*"
		instate         = "&in=state:36+county:"+county+"+tract:"+tract

		url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
		print url

		data = urllib2.urlopen(url).read()
		data = json.loads(data)

		fname = pd+"/input/census/census/census_2010_block_st36_"+county+tract+"_pop_race_hisp.csv"
		with open(fname,'wb') as outf:
		    outcsv = csv.writer(outf)
		    outcsv.writerows(data)

		time.sleep(pauser)    

		#-----census 2010 SexByAge

		listofcensusvars= [
		#SexByAge
		"P0120001",
		"P0120002",
		"P0120003",
		"P0120004",
		"P0120005",
		"P0120006",
		"P0120007",
		"P0120008",
		"P0120009",
		"P0120010",
		"P0120011",
		"P0120012",
		"P0120013",
		"P0120014",
		"P0120015",
		"P0120016",
		"P0120017",
		"P0120018",
		"P0120019",
		"P0120020",
		"P0120021",
		"P0120022",
		"P0120023",
		"P0120024",
		"P0120025",
		"P0120026",
		"P0120027",
		"P0120028",
		"P0120029",
		"P0120030",
		"P0120031",
		"P0120032",
		"P0120033",
		"P0120034",
		"P0120035",
		"P0120036",
		"P0120037",
		"P0120038",
		"P0120039",
		"P0120040",
		"P0120041",
		"P0120042",
		"P0120043",
		"P0120044",
		"P0120045",
		"P0120046",
		"P0120047",
		"P0120048",
		"P0120049"
		]

		censusapipreurl = "http://api.census.gov/data/2010/sf1?key="
		censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
		gettxt          = "&get="
		allcensusvars   = ','.join(listofcensusvars)
		forgeog         = "&for=block:*"
		instate         = "&in=state:36+county:"+county+"+tract:"+tract

		url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
		print url

		data = urllib2.urlopen(url).read()
		data = json.loads(data)

		fname = pd+"/input/census/census/census_2010_block_st36_"+county+tract+"_sex_by_age.csv"
		with open(fname,'wb') as outf:
		    outcsv = csv.writer(outf)
		    outcsv.writerows(data)

		time.sleep(pauser)  
 
		#-----census 2010 Housing Units

		listofcensusvars= [
		#TotalHousingUnits
		"H00010001",
		#OccupancyStatus
		"H0030001",
		"H0030002",
		"H0030003",
		#Tenure
		"H0040001",
		"H0040002",
		"H0040003",
		"H0040004",
		#VacancyStatus
		"H0050001",
		"H0050002",
		"H0050003",
		"H0050004",
		"H0050005",
		"H0050006",
		"H0050007",
		"H0050008"
		]

		censusapipreurl = "http://api.census.gov/data/2010/sf1?key="
		censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
		gettxt          = "&get="
		allcensusvars   = ','.join(listofcensusvars)
		forgeog         = "&for=block:*"
		instate         = "&in=state:36+county:"+county+"+tract:"+tract

		url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
		print url

		data = urllib2.urlopen(url).read()
		data = json.loads(data)

		fname = pd+"/input/census/census/census_2010_block_st36_"+county+tract+"_housing.csv"
		with open(fname,'wb') as outf:
		    outcsv = csv.writer(outf)
		    outcsv.writerows(data)

		time.sleep(pauser)  


