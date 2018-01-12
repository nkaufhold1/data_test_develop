# Contains only properties listed from 2016 [DateListed]
# Contains only properties that contain the word "and" in the Description field
# CSV ordered by DateListed
# Required fields:
# MlsId
# MlsName
# DateListed
# StreetAddress
# Price
# Bedrooms
# Bathrooms
# Appliances (all sub-nodes comma joined)
# Rooms (all sub-nodes comma joined)
# Description (the first 200 characters)

import xml.etree.ElementTree as ET
import urllib2 as url
import pandas as pd

BOOJ_URL = 'http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml'

data = url.urlopen (BOOJ_URL).read()

data_root = ET.fromstring(data)

def get_mlsid():
    mlsidList = []
    for listing in data_root.findall('Listing'):
	    for listDetails in listing.findall('ListingDetails'):
		    mlsid = listDetails.find('MlsId').text
		    mlsidList.append(mlsid)
    return mlsidList

#mlsid check
#mlsid = get_mlsid()
#print(mlsid)

def get_mlsname():
    mlsNameList = []
    for listing in data_root.findall('Listing'):
	    for listDetails in listing.findall('ListingDetails'):
		    mlsName = listDetails.find('MlsName').text
		    mlsNameList.append(mlsName)
    return mlsNameList

#mlsname check
# mlsname = get_mlsname()
# print(mlsname)

def get_dates():
    dateList = []
    for listing in data_root.findall('Listing'):
	    for listDetails in listing.findall('ListingDetails'):
		    date = listDetails.find('DateListed').text
		    dateList.append(date)
    return dateList

#dates check
# dates = get_dates()
# print(dates)

def get_address():
	addyList = []
	for listing in data_root.findall('Listing'):
	    for location in listing.findall('Location'):
		    addy = location.find('StreetAddress').text
		    addyList.append(addy)
	return addyList

#address check
# address = get_address()
# print(address)


def get_price():
    priceList = []
    for listing in data_root.findall('Listing'):
	    for listDetails in listing.findall('ListingDetails'):
		    price = listDetails.find('MlsId').text
		    priceList.append(price)
    return priceList

#price check
# price = get_price()
# print(price)

def get_bedrooms():
	bedroomsList = []
	for listing in data_root.findall('Listing'):
		for basicDetails in listing.findall('BasicDetails'):
		    bedrooms = basicDetails.find('Bedrooms').text
		    bedroomsList.append(bedrooms)
	return bedroomsList

#bedrooms check
# bedrooms = get_bedrooms()
# print(bedrooms)

def get_bathrooms():
	#Create a list of the sum total of all different bathroom types and return a string
	#in order to remain consistent with data type
	totalBathroomsList = []
	for listing in data_root.findall('Listing'):
		for basicDetails in listing.findall('BasicDetails'):
			if(type(basicDetails.find('Bathrooms').text) == type(None)):
				bathrooms = 0
			else:
			    bathrooms = basicDetails.find('Bathrooms').text
			if(type(basicDetails.find('FullBathrooms').text) == type(None)):
				fullBathrooms = 0
			else:
			    fullBathrooms = basicDetails.find('FullBathrooms').text
			if(type(basicDetails.find('HalfBathrooms').text) == type(None)):
				halfBathrooms = 0
			else:
				halfBathrooms = basicDetails.find('HalfBathrooms').text
			if(type(basicDetails.find('ThreeQuarterBathrooms').text) == type(None)):
				threeQuarterBathrooms = 0
			else:
				threeQuarterBathrooms = basicDetails.find('ThreeQuarterBathrooms').text
			bathroomSum = int(bathrooms) + int(fullBathrooms) + int(halfBathrooms) + int(threeQuarterBathrooms)
			bathroomSum = str(bathroomSum)
			totalBathroomsList.append(bathroomSum)
	return totalBathroomsList

#bathrooms check
# bathrooms = get_bathrooms()
# print(bathrooms)

def get_appliances():
	applianceList = []
	appliancesList = []
	for i in range(0,len(data_root)):
		for j in range(0, len(data_root[i])):
			if('RichDetails' in str(data_root[i][j])):
				for k in range(0, len(data_root[i][j])):
					if('Appliances' in str(data_root[i][j][k])):
						for l in range(0, len(data_root[i][j][k])):
							applianceList.append(data_root[i][j][k][l].text)						
		appliancesList.append(applianceList)
		applianceList = []
	return appliancesList

#appliances check
# appliances = get_appliances()
# print(appliances)

def get_rooms():
	roomList = []
	roomsList = []
	for i in range(0,len(data_root)):
		for j in range(0, len(data_root[i])):
			if('RichDetails' in str(data_root[i][j])):
				for k in range(0, len(data_root[i][j])):
					if('Rooms' in str(data_root[i][j][k])):
						for l in range(0, len(data_root[i][j][k])):
							roomList.append(data_root[i][j][k][l].text)						
		roomsList.append(roomList)
		roomList = []
	return roomsList

#rooms check
# rooms = get_rooms()
# print(rooms)

def get_description():
	descList = []
	for listing in data_root.findall('Listing'):
	    for basicDetails in listing.findall('BasicDetails'):
		    description = basicDetails.find('Description').text
		    descList.append(description)
	return descList

#description check
# description = get_description()
# print(description[0:5])

def run_code():
	#Here collect all of the data into lists
	MlsId = get_mlsid()
	MlsName = get_mlsname()
	DateListed = get_dates()
	StreetAddress = get_address()
	Price = get_price()
	Bedrooms = get_bedrooms()
	Bathrooms = get_bathrooms()
	Appliances = get_appliances()
	Rooms = get_rooms()
	Description = get_description()

	#Create labels to use for the data frame and csv file
	labels = ['MlsId', 'MlsName', 'DateListed', 'StreetAddress', 'Price', 
			  'Bedrooms', 'Bathrooms', 'Appliances', 'Rooms', 'Description']

	#Set up data into a dictionary that will be placed into the data frame
	dataDictionary = {'MlsId':MlsId, 'MlsName':MlsName, 'DateListed':DateListed, 'StreetAddress':StreetAddress, 
					  'Price':Price, 'Bedrooms':Bedrooms, 'Bathrooms':Bathrooms, 'Appliances':Appliances, 
					  'Rooms':Rooms, 'Description':Description}

	#Create data frame from above dictionary
	df = pd.DataFrame(data = dataDictionary)

	#Create a copy of the data frame to be manipulated which is standard for Pandas
	df_copy = df

	#Get rid of rows that do not contain 'and' in the description and also get rid of rows that
	#are not dated with '2016'
	for i in df_copy.index:
		if('and' not in df_copy['Description'].loc[i] or '2016' not in df_copy['DateListed'].loc[i]):
			df_copy = df_copy.drop(df.index[i])

	# #Truncate the description down to 200 characters.
	for item in df_copy.index:
		df_copy['Description'].loc[item] = df_copy['Description'].loc[item][0:200]

	#Sort by datelisted most recent first
	df_copy = df_copy.sort_values(by = 'DateListed', ascending = False)

	#Reset the index and drop original
	df_copy = df_copy.reset_index(drop = True)
	print(df_copy)

	#Create a csv file
	csvFilename = "boojDataCodeTest.csv"
	file = open(csvFilename, "w")
	df_copy.to_csv(csvFilename, columns = labels)
	file.close()

run_code()







