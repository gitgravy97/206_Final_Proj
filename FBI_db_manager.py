#print("FBI_db_manager.py loaded")

import json
import requests
import sqlite3

# Exterior text file containing FBI API Key for HTTP Verification
import FBI_API_Key

def init_FBI_table():
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()

	statement = """
	SELECT count(*) FROM sqlite_master WHERE type = 'table' 
	AND name = 'FBI'
	"""
	cur.execute(statement)

	table_exists = -1
	for i in cur:
		if(i[0]==0):
			print("Table \"FBI\" does not exist")
			table_exists = False
		elif(i[0]>0):
			print("Table \"FBI\" does exist")
			table_exists = True

	if(table_exists):
		del_table = input("FBI Table exists. Drop table? yes/no: ")
		if(del_table.lower()=="yes"):
			print("Deleting Table . . .")
			statement = "DROP TABLE 'FBI';"
			cur.execute(statement)
			print("Building New FBI Table . . .")
			statement = """						
				CREATE TABLE 'FBI' (
				'ID' 	INTEGER PRIMARY KEY AUTOINCREMENT,
				'year' 			Integer,
				'frequency'		Integer,
				'offense' 			Text,
				'classification'	Text,
				'perc_of_year'	Integer
			);
			"""
			cur.execute(statement)
		else:
			print("Using Pre-Existing FBI Table.")
	else:
		print("Building New FBI Table . . .")
		statement = """
			CREATE TABLE 'FBI' (
			'ID' 	INTEGER PRIMARY KEY AUTOINCREMENT,
			'year' 			Integer,
			'frequency'		Integer,
			'offense' 			Text,
			'classification'	Text,
			'perc_of_year'	Integer
		);
		"""
		cur.execute(statement)
	conn.commit()
	conn.close()

def FBI_requests():
	response = FBI_cache()
	#print(response)
	#print(response.text)
	data_dict = json.loads(response)
	print("Total Entries: "+str(len(data_dict["results"])))

	relevant_yrs = []
	for i in data_dict["results"]:
		if((int(i["year"])>=2012) and (i["count"] != None)):
			relevant_yrs.append(i)
	#print(relevant_yrs)
	#print(len(relevant_yrs))

	# We've trimmed out older data and data without counts
	# because counts are absolutely the purpose of this and a
	# None value tells us nothing of value other than that they
	# weren't reporting that kind of crime yet under that category
	return(relevant_yrs)

def FBI_cache():
	try:
		file_ref = open("FBI_cache.json","r")
		data = file_ref.read()
		FBI_cache_dict = json.loads(data)
		file_ref.close()
	except:
		FBI_cache_dict = {}

	#print(FBI_API_Key.my_key)
	req_url = "https://api.usa.gov/crime/fbi/ucr/offenses/count/"
	req_url += "states/mi/offense_name?page=1&per_page=10&output=json&"
	req_url += "api_key="
	
	complete_req_url = req_url + str(FBI_API_Key.my_key)
	response = requests.get(complete_req_url)

	if(req_url in FBI_cache_dict):
		#print("! - Cache Pull - !")
		return(FBI_cache_dict[req_url])
	else:
		#print("! - Making Web Request - !")
		resp = requests.get(complete_req_url)
		FBI_cache_dict[req_url] = resp.text
		file_ref = open("FBI_cache.json","w")
		dumped_data = json.dumps(FBI_cache_dict, sort_keys = True, indent=4)
		file_ref.write(dumped_data)
		file_ref.close()
		return(FBI_cache_dict[req_url])

def FBI_table_empty_check():
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()
	statement = "SELECT Count(*) FROM FBI"
	cur.execute(statement)
	check = cur.fetchone()
	if(str(check[0])=="0"):
		print("Table \"FBI\" is empty.")
		return(True)
	else:
		print("Table \"FBI\" not empty.")
		return(False)

def FBI_table_populate():
	crime_since_2012 = FBI_requests()
	#for i in crime_since_2012:
	#	print(i)
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()

	for i in crime_since_2012:
		insert = """
			INSERT INTO FBI (year, offense, frequency)
			VALUES (?, ?, ?)
		"""
		params = (i["year"], i["offense_name"], i["count"])
		cur.execute(insert, params)
	conn.commit()
	conn.close()

def FBI_table_substantiate_classification():
	# Look at field "offense"
	# These will need to map to two separate, mutually-exclusive lists
	# Lists to map to will need to be hard-coded
	# Once mapped as a List A crime or a List B crime, insert a value
	# for that row under the "classification" field
	pass

def FBI_table_substantiate_annual_percentage():
	# Look at fields "frequency" and "year"
	# For each row, find frequency of that row
	# Find total frequency for the year of that row
	# Divide frequency of that item by frequency for the year
	# Insert it the percentage value into the row under
	# the "perc_or_year" field
	crime_since_2012 = FBI_requests()
	freqs = {2012:0, 2013:0, 2014:0, 2015:0, 2016:0}
	print(freqs)
	for i in crime_since_2012:
		freqs[int(i["year"])] += i["count"]
	print(freqs)
	for i in crime_since_2012:
		if(i["year"]=="2012"):
			print(i["offense_name"])
			value = int(i["count"])/freqs[int(i["year"])]
			adjusted_value = round((value*100),4)
			print(adjusted_value)


if(__name__=="__main__"):
	print("FBI_db_manager as __main__")
	if(FBI_table_empty_check()):
		FBI_table_populate()
	print("X"*75)
	FBI_data_substantiate_annual_percentage()