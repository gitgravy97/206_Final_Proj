#print("DPSS_db_manager.py loaded")
import json
import requests
import sqlite3

def init_DPSS_table():
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()

	statement = """
	SELECT count(*) FROM sqlite_master WHERE type = 'table' 
	AND name = 'DPSS'
	"""
	cur.execute(statement)

	table_exists = -1
	for i in cur:
		if(i[0]==0):
			print("Table \"DPSS\" does not exist")
			table_exists = False
		elif(i[0]>0):
			print("Table \"DPSS\" does exist")
			table_exists = True

	if(table_exists):
		del_table = input("DPSS Table exists. Drop table? yes/no: ")
		if(del_table.lower()=="yes"):
			print("Deleting Table . . .")
			statement = "DROP TABLE 'DPSS';"
			cur.execute(statement)
			print("Building New DPSS Table . . .")
			# # # ! ! ! - CAD_Num not auto-increment, right?
			statement = """						
			CREATE TABLE 'DPSS' (
			'CAD_Num' 	INTEGER PRIMARY KEY,
			'date'			Text,
			'description' 	Text,
			'location' 		Text,
			'address' 		Text,
			'disposition' 	Text,
			'narrative'		Text
			);
			"""
			# # # ! ! ! - CAD_Num not auto-increment, right?
			cur.execute(statement)
		else:
			print("Using Pre-Existing DPSS Table.")
	else:
		print("Building New DPSS Table . . .")
		statement = """
		CREATE TABLE 'DPSS' (
		'CAD_Num' 	INTEGER PRIMARY KEY AUTOINCREMENT,
		'date'			Text,
		'description' 	Text,
		'location' 		Text,
		'address' 		Text,
		'disposition' 	Text,
		'narrative'		Text
		);
		"""
		cur.execute(statement)

	conn.commit()
	conn.close()

# Input date structure is mm/dd/yyyy
def DPSS_cache(input_date):
	try:
		file_ref = open("DPSS_cache.json","r")
		data = file_ref.read()
		DPSS_cache_dict = json.loads(data)
		file_ref.close()
	except:
		DPSS_cache_dict = {}

	request_url = "https://dpss.umich.edu/api/GetCrimeLogCache?date="
	request_url += str(input_date)
	#Example Date - St Patrick's day, 03/17/2018

	if(input_date in DPSS_cache_dict):
		#print("! - Cache Pull - !")
		return(DPSS_cache_dict[input_date])
	else:
		#print("! - Making Web Request - !")
		resp = requests.get(request_url)
		DPSS_cache_dict[input_date] = resp.text
		file_ref = open("DPSS_cache.json","w")
		dumped_data = json.dumps(DPSS_cache_dict, sort_keys = True, indent=4)
		file_ref.write(dumped_data)
		file_ref.close()
		return(DPSS_cache_dict[input_date])

def Investigate_Total_Cached_Incidents():
	file_ref=open("DPSS_cache.json","r")
	data=file_ref.read()
	DPSS_cache_dict = json.loads(data)
	file_ref.close()
	#print(type(DPSS_cache_dict))

	highest_count = 0 
	highest_count_date = ""

	total_count = 0
	for i in DPSS_cache_dict:
		internal = json.loads(DPSS_cache_dict[i])
		#print(str(i) + ": " + str(internal["count"]))
		total_count+= internal["count"]
		if(internal["count"] > highest_count):
			highest_count = internal["count"]
			highest_count_date = i
	
	print("====="*15)
	print("Total Incidents Count: " + str(total_count))
	print("====="*15)
	print("Date of Highest Incident Count: "+str(highest_count_date))
	print("With " + str(highest_count) + " incidents.")
	print("====="*15)

# Inputs : mm, yyyy
def Month_Harvester(month, year, silent=True):
	# Data goes back to Dec 31st, 1999
	years = [2000, 2001, 2002, 2004, 2005, 2006, 2007,
	2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
	2016, 2017, 2018]
	LeapYears = [2000, 2004, 2008, 2012, 2016, 2020]
	Month_Lengths = {"01":31, "02":28, "03":31,
	"04":30, "05":31, "06":30, "07":31, "08":31,
	"09":30, "10":31, "11":30, "12":31}
	Month_Codes = ["01","02","03","04","05","06",
	"07","08","09","10","11","12"]
	#print(len(Month_Lengths))

	month_date_codes = []
	base = Gen_Less_Dates()
	for i in base:		# Len(i) == 10
		if(i[6:10]==year):
			if(i[0:2]==month):
				#print(i[0:2] + " " + i[3:5] + " " + i[6:10])
				month_date_codes.append(i)
	
	for i in month_date_codes:
		if(silent==False):
			print("Pulling data from: " + str(i))
		DPSS_cache(input_date=i)

# Exceeds scope of current project, but it's an option for future use
def Gen_All_Dates():
	# Data goes back to Dec 31st, 1999
	years = [2000, 2001, 2002, 2004, 2005, 2006, 2007,
	2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
	2016, 2017, 2018]
	LeapYears = [2000, 2004, 2008, 2012, 2016, 2020]
	Month_Lengths = {"01":31, "02":28, "03":31,
	"04":30, "05":31, "06":30, "07":31, "08":31,
	"09":30, "10":31, "11":30, "12":31}
	Month_Codes = ["01","02","03","04","05","06",
	"07","08","09","10","11","12"]
	#print(len(Month_Lengths))

	all_dates = ["12/31/1999"]
	for i in years:
		if(i not in LeapYears):
			for j in Month_Codes:
				for k in range(Month_Lengths[j]):
					date = str(j) + "/" + str(k+1) + "/" + str(i)
					#print(date)
					all_dates.append(str(date))
			#print("xxxxx")
		elif(i in LeapYears):
			for j in Month_Codes:
				if(j=="02"):
					for k in range(29):
						date = str(j) + "/" + str(k+1) + "/" + str(i)
						#print(date)
						all_dates.append(str(date))
				else:
					for k in range(Month_Lengths[j]):
						date = str(j) + "/" + str(k+1) + "/" + str(i)
						#print(date)
						all_dates.append(str(date))
			#print("xxxxx")
	#print(all_dates)
	#print(len(all_dates))
	return(all_dates)

# Theoretically to build base from scratch, take the output,
# loop calls through it, and plug away
def Gen_Less_Dates():
	years = [2015, 2016, 2017, 2018]
	LeapYears = [2000, 2004, 2008, 2012, 2016, 2020]
	Month_Lengths = {"01":31, "02":28, "03":31,
	"04":30, "05":31, "06":30, "07":31, "08":31,
	"09":30, "10":31, "11":30, "12":31}
	Month_Codes = ["01","02","03","04","05","06",
	"07","08","09","10","11","12"]
	#print(len(Month_Lengths))

	all_dates = ["12/31/1999"]
	# "Wait, why k<9?" - because we're adding +1 since range(x) goes
	# from 0 to x instead of 1 to x
	for i in years:
		if(i not in LeapYears):
			for j in Month_Codes:
				for k in range(Month_Lengths[j]):
					if(k < 9):
						date = str(j) + "/0" + str(k+1) + "/" + str(i)
						#print(date)
						all_dates.append(str(date))
					else:
						date = str(j) + "/" + str(k+1) + "/" + str(i)
						#print(date)
						all_dates.append(str(date))						
			#print("xxxxx")
		elif(i in LeapYears):
			for j in Month_Codes:
				if(j=="02"):
					for k in range(29):
						if(k < 9):
							date = str(j) + "/0" + str(k+1) + "/" + str(i)
							#print(date)
							all_dates.append(str(date))
						else:
							date = str(j) + "/" + str(k+1) + "/" + str(i)
							#print(date)
							all_dates.append(str(date))
				else:
					for k in range(Month_Lengths[j]):
						if(k < 9):
							date = str(j) + "/0" + str(k+1) + "/" + str(i)
							#print(date)
							all_dates.append(str(date))
						else:
							date = str(j) + "/" + str(k+1) + "/" + str(i)
							#print(date)
							all_dates.append(str(date))
	return(all_dates)	
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# This could just be a Harvest(year) function but I prefer this
# organization because API calls can be long and breaking things
# up and being able to easily comment-in comment-out months
# and such is just comfortable for now
def Harvest_2015():
	# Starting Welcome Week, as interest is mainly midyear
	# i.e. post-move-in, on-campus crime reporting
	print("Harvesting 2015 (Sept-Dec)")
	Month_Harvester(month="09",year="2015")
	Month_Harvester(month="10",year="2015")
	Month_Harvester(month="11",year="2015")
	Month_Harvester(month="12",year="2015")

# Toggle quarters in actual function call
def Harvest_2016(Q1=False,Q2=False,Q3=False,Q4=False):
	print("Harvesting 2016")

	if(Q1):
		Month_Harvester(month="01",year="2016", silent=True)
		Month_Harvester(month="02",year="2016", silent=True)
		Month_Harvester(month="03",year="2016", silent=True)
	if(Q2):
		Month_Harvester(month="04",year="2016", silent=True)
		Month_Harvester(month="05",year="2016", silent=True)
		Month_Harvester(month="06",year="2016", silent=True)
	if(Q3):
		Month_Harvester(month="07",year="2016", silent=True)
		Month_Harvester(month="08",year="2016", silent=True)
		Month_Harvester(month="09",year="2016", silent=True)
	if(Q4):
		Month_Harvester(month="10",year="2016", silent=True)
		Month_Harvester(month="11",year="2016", silent=True)
		Month_Harvester(month="12",year="2016", silent=True)

# Toggle quarters in actual function call
def Harvest_2017(Q1=False,Q2=False,Q3=False,Q4=False):
	print("Harvesting 2017")
	if(Q1):
		Month_Harvester(month="01", year="2017", silent=True)
		Month_Harvester(month="02", year="2017", silent=True)
		Month_Harvester(month="03", year="2017", silent=True)
	if(Q2):
		Month_Harvester(month="04", year="2017", silent=True)
		Month_Harvester(month="05", year="2017", silent=True)
		Month_Harvester(month="06", year="2017", silent=True)
	if(Q3):
		Month_Harvester(month="07", year="2017", silent=True)
		Month_Harvester(month="08", year="2017", silent=True)
		Month_Harvester(month="09", year="2017", silent=True)
	if(Q4):
		Month_Harvester(month="10", year="2017", silent=True)
		Month_Harvester(month="11", year="2017", silent=True)
		Month_Harvester(month="12", year="2017", silent=True)

def Harvest_2018(Q1=False,Q2=False,Q3=False,Q4=False):
	print("Harvesting 2018")
	if(Q1):
		Month_Harvester(month="01",year="2018", silent=False)
		Month_Harvester(month="02",year="2018", silent=False)
		Month_Harvester(month="03",year="2018", silent=False)
	if(Q2):
		pass
		#Month_Harvester(month="04",year="2015")

def DPSS_table_empty_check():
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()
	statement = "SELECT Count(*) FROM DPSS"
	cur.execute(statement)
	check = cur.fetchone()
	if(str(check[0])=="0"):
		print("Table \"DPSS\" is empty.")
		return(True)
	else:
		print("Table \"DPSS\" not empty.")
		return(False)

def DPSS_table_populate():
	pass

if(__name__=="__main__"):
	print("DPSS_db_manager as __main__")
	#print(DPSS_cache("03/17/2018"))
	#DPSS_cache("09/01/2015")
	# Had hardcoded through 09/30/2015
	Investigate_Total_Cached_Incidents()
	#Harvest_2015()
	#Harvest_2016(Q1=False,Q2=False,Q3=False,Q4=False)
	#Harvest_2017(Q1=True,Q2=True,Q3=True,Q4=True)
	#Harvest_2018(Q1=True, Q2=False, Q3=False, Q4=False)
