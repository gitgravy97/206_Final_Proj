#print("Famous_db_manager.py loaded")
import json
import requests
import sqlite3
from bs4 import BeautifulSoup

try:
	file_ref = open("fame_cache.json","r")
	data = file_ref.read()
	fame_cache_dict = json.loads(data)
	file_ref.close()
except:
	fame_cache_dict = {}

class Criminal():
	def __init__(self, name, nation, b_year, astro, why_fame):
		self.name = name
		self.nation = nation
		self.birth_year = b_year
		self.astro = astro
		self.fame_cause = why_fame
	def __str__(self):
		crim_string = str(self.name) + " " + str(self.nation) + " "
		crim_string += str(self.birth_year) + " " + str(self.astro)
		crim_string += " " + str(self.fame_cause)
		return(crim_string)

def init_Famous_table():
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()

	statement = """
	SELECT count(*) FROM sqlite_master WHERE type = 'table' 
	AND name = 'Famous'
	"""
	cur.execute(statement)

	table_exists = -1
	for i in cur:
		if(i[0]==0):
			print("Table \"Famous\" does not exist")
			table_exists = False
		elif(i[0]>0):
			print("Table \"Famous\" does exist")
			table_exists = True

	if(table_exists):
		del_table = input("Famous Table exists. Drop table? yes/no: ")
		if(del_table.lower()=="yes"):
			print("Deleting Table . . .")
			statement = "DROP TABLE 'Famous';"
			cur.execute(statement)
			print("Building New Famous Table . . .")
			statement = """
			CREATE TABLE 'Famous' (
			'ID' 	INTEGER PRIMARY KEY AUTOINCREMENT,
			'name'			Text,
			'nationality' 	Text,
			'fame_cause' 	Text,
			'sun_sign' 		Text,
			'birth_year' 	Integer
			);
			"""
			cur.execute(statement)
		else:
			print("Using Pre-Existing Famous Table.")
	else:
		print("Building New Famous Table . . .")
		statement = """
		CREATE TABLE 'Famous' (
		'ID' 	INTEGER PRIMARY KEY AUTOINCREMENT,
		'name'			Text,
		'nationality' 	Text,
		'fame_cause' 	Text,
		'sun_sign' 		Text,
		'birth_year' 	Integer
		);
		"""
		cur.execute(statement)

	conn.commit()
	conn.close()

# Returns True if empty, False otherwise
def Famous_table_empty_check():
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()
	statement = "SELECT Count(*) FROM Famous"
	cur.execute(statement)
	check = cur.fetchone()
	if(str(check[0])=="0"):
		print("Table \"Famous\" is empty.")
		return(True)
	else:
		print("Table \"Famous\" not empty.")
		return(False)

def Famous_table_populate():
	crim_list = Famous_Scrape()
	#for i in crim_list:
	#	print(i)
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()

	for i in crim_list:
		insert = """
			INSERT INTO Famous (name, nationality, fame_cause, sun_sign, birth_year)
			VALUES (?,?,?,?,?)
		"""
		params = (i.name, i.nation, i.fame_cause, i.astro, i.birth_year)
		cur.execute(insert, params)

	conn.commit()
	conn.close()

def Famous_Cache(fame_url):
	#print(fame_cache_dict.keys())
	if(fame_url in fame_cache_dict):
		# print("! - Cache Pull - !")
		return(fame_cache_dict[fame_url])
	else:
		# print("! - Making Web Request - !")
		# print("TO ")
		# print(fame_url)
		resp = requests.get(fame_url)
		fame_cache_dict[fame_url] = resp.text
		file_ref = open("fame_cache.json","w")
		dumped_data = json.dumps(fame_cache_dict, sort_keys = True, indent=4)
		file_ref.write(dumped_data)
		file_ref.close()
		return(fame_cache_dict[fame_url])

# Returns a list of "Criminal" objects
def Famous_Scrape():
	# Part I : Establish a base of criminal page URL's
	criminal_page_urls = []

	# Note : Index only has two pages
	for i in [1,2]:
		index = "https://www.thefamouspeople.com/criminals.php?page="
		index += str(i)
		#print(index)
		index_page_soup = BeautifulSoup(Famous_Cache(index),"html.parser")
		#print(type(index_page_soup))
		#print(index_page_soup)
		index_elems = index_page_soup.find_all(class_="btn btn-primary btn-sm btn-block btn-block-margin")
		#print(len(index_elems))
	
	
		for i in index_elems:
			#print(i.text)
			# Reason: URL's stored seem to be prepended by "//"
			criminal_page_urls.append(i["href"][2:])
	#print(criminal_page_urls)
	#print(len(criminal_page_urls))

	print("===="*16)
	
	# Part II : Iterate the biography page URL's and scrape data
	# and then build Criminal objects to populate criminal_list
	
	criminal_list = []

	"""
	NOTE - For full range, in the below loop use criminal_page_urls
	To speed things up, you can use a temporary list splite like 
	as is commented-out below
	However, doing so seems to overwrite things so you actually lose
	cached pages that weren't used in the last run
	"""

	#temp_list = criminal_page_urls[0:2]
	Counter = 0
	for i in criminal_page_urls:
		temp_url = "http://" + str(i)
		#print(temp)
		cache_it = Famous_Cache(temp_url)
		temp_soup = BeautifulSoup(cache_it,"html.parser")
		
		iter_name = ""
		iter_fame_reason = ""
		iter_nation = ""
		iter_birth = ""
		iter_astro = ""
		
		# Part II-A) Get Name
		header = temp_soup.find("h1")
		header_txt = header.text
		ridge = header_txt.find("Biography")
		iter_name = header_txt[0:ridge].strip()
		#print(iter_name)

		# Part II-B, II-C, II-D, II-E) Collect other field data
		found = temp_soup.find_all(class_="quickfactsdata")
		for i in found:
			if("Famous as" in i.text):
				#print("Famous as:")
				iter_fame_reason = i.text[10:].strip()
				#print(iter_fame_reason)
			elif("Nationality" in i.text):
				#print("Nationality:")
				iter_nation = i.text[13:].strip()
				#print(iter_nation)
			elif("Birthday" in i.text):
				#print("Birthyear:")
				iter_birth = i.text[-4:].strip()
				#print(iter_birth)
			# ENSURE to include the : to avoid getting "Born In:[location]"
			elif("Born:" in i.text):
				iter_birth = i.text[5:].strip()
				#print(iter_name)
				#print(iter_birth)
			elif("Sun Sign" in i.text):
				#print("Sun Sign:")
				iter_astro = i.text[9:].strip()
				#print(iter_astro)
		
		# Part II-F) Consolidate into an object
		New_Crim = Criminal(name=iter_name, nation=iter_nation, 
			b_year=iter_birth, astro=iter_astro, why_fame=iter_fame_reason)
		criminal_list.append(New_Crim)
		#print("xxxxx"*14)
		Counter = Counter + 1
		print(str(Counter) + " criminals loaded.")

	#for i in criminal_list:
	#	print(i)
	
	return(criminal_list)

if(__name__=="__main__"):
	print("Famous_db_manager as __main__")