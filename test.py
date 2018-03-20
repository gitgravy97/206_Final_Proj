import json
import requests
import webbrowser

try:
	print("Cache Found")
	"""
	file_ref = open("DPSS_Cache.json","r")
	data = file_ref.read()
	DPSS_Cache_Dict = json.load(data)
	file_ref.close()
	"""
	with open("DPSS_Cache.json") as data_file:
		DPSS_Cache_Dict = json.load(data_file)
	# print(DPSS_Cache_Dict)
	print("Cache Loaded")
except:
	print("Cache Not Found")
	DPSS_Cache_Dict = {}
	print("Cache Dictionary Established")

def cache_dpss_log(date_string_in):
	# "mm/dd/yyyy"
	date_string = date_string_in
	print((date_string in DPSS_Cache_Dict))
	if(date_string in DPSS_Cache_Dict):
		print("Pulling DPSS Log Data from cache.")
		return(DPSS_Cache_Dict[date_string])
	else:
		print("CURRENT CACHE")
		print(DPSS_Cache_Dict)
		base_url_dpss_req = "https://dpss.umich.edu/api/GetCrimeLogCache?date="
		dpss_dated_url = base_url_dpss_req + date_string
		response = requests.get(dpss_dated_url)
		print("Requesting DPSS Log Data from " + date_string + ".")

		DPSS_Cache_Dict[date_string] = response.text
		file_ref = open("DPSS_Cache.json","w")
		dumped_data = json.dumps(DPSS_Cache_Dict, sort_keys=True, indent=4)
		file_ref.write(dumped_data)
		file_ref.close()
		return(DPSS_Cache_Dict[date_string])

"""
BDay21_req_dict = cache_dpss_log("01/19/2018")
print(BDay21_req_dict)
"""

"""
Days in each month

January 31		||	May 31 		||	September 30
February 28/29	|| 	June 30		|| 	October 31
March 31 		|| 	July 31		|| 	November 30
April 30		|| 	August 31	|| 	December 31

Relevant Leap Years
2000	2004	2008	2012	2016
"""
"""
req_date = input("Date? (mm/dd/yyyy) ")
pulled_data = cache_dpss_log(req_date)
print(pulled_data)
full_url= "https://dpss.umich.edu/api/GetCrimeLogCache?date=" + str(req_date)
webbrowser.open(url=full_url)
"""

"""
FebList = ["02/01/2018","02/02/2018","02/03/2018","02/04/2018","02/05/2018",
"02/06/2018","02/07/2018","02/08/2018","02/09/2018","02/10/2018",
"02/11/2018","02/12/2018","02/13/2018","02/14/2018","02/15/2018",
"02/16/2018","02/17/2018","02/18/2018","02/19/2018","02/20/2018",
"02/21/2018","02/22/2018","02/23/2018","02/24/2018","02/25/2018",
"02/16/2018","02/27/2018","02/28/2018",]
for i in FebList:
	that_day_data = cache_dpss_log(i)
	for j in that_day_data:
		desc = j["data"]["description"]
		loc = j["location"]
		print(str(description) + " at " + str(loc))
		print("."*65)
	print("="*65)
"""

data = cache_dpss_log("02/01/2018")
data_dict = json.loads(data)
print("="*65)
for i in data_dict["data"]:
	print(i)
	print("."*75)
"""
r1 = requests.get("https://www.dpss.umich.edu/content/crime-safety-data/daily-crime-fire-log/#")
r2 = requests.get("https://dpss.umich.edu/api/GetCrimeLogCache")

print(r1.text)
print("="*50)
print(r2.text)
"""

#s1 = json.loads(r1.text)
#s2 = json.loads(r2.text)

#print(s1)
#print("="*50)
#print(s2)