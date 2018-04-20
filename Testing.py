# General Modules
import json
import sqlite3
import unittest
# From X Import Y
from bs4 import BeautifulSoup
# Database Manager Modules
import DPSS_db_manager as DPSS_DBM 
import Famous_db_manager as Fame_DBM
import FBI_db_manager as FBI_DBM 
# Reference Modules
import Buildings
import Crime_Tagging
import FBI_Class_Lists

class Test_Fame(unittest.TestCase):
	def test_Criminal_Class(self):
		smooth_Criminal = Fame_DBM.Criminal(name="Michael", nation="USA",
			b_year="7777", astro="capricorn", why_fame="Smooth")
		self.assertEqual(smooth_Criminal.name, "Michael")
		self.assertEqual(smooth_Criminal.nation, "USA")
		self.assertEqual(smooth_Criminal.birth_year, "7777")
		self.assertEqual(smooth_Criminal.astro, "capricorn")
		self.assertEqual(smooth_Criminal.fame_cause, "Smooth")

	def test_Fame_cache(self):
		x = Fame_DBM.Famous_Cache(fame_url=
			"http://www.thefamouspeople.com/profiles/abu-bakar-bashir-3480.php")
		self.assertEqual(type(x), str)
		y = BeautifulSoup(x, 'html.parser')
		
		iter_name = ""
		iter_fame_reason = ""
		iter_nation = ""
		iter_birth = ""
		iter_astro = ""
		
		# Part II-A) Get Name
		header = y.find("h1")
		header_txt = header.text
		ridge = header_txt.find("Biography")
		iter_name = header_txt[0:ridge].strip()
		#print(iter_name)

		# Part II-B, II-C, II-D, II-E) Collect other field data
		found = y.find_all(class_="quickfactsdata")
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
		Crim = Fame_DBM.Criminal(name=iter_name, nation=iter_nation, 
			b_year=iter_birth, astro=iter_astro, why_fame=iter_fame_reason)
		# print(Crim)
		self.assertEqual(Crim.name, "Abu Bakar Bashir")
		self.assertEqual(Crim.nation, "Indonesian")
		self.assertEqual(Crim.birth_year, "1938")
		self.assertEqual(Crim.astro, "Leo")
		self.assertEqual(Crim.fame_cause, "Cleric")
		self.assertEqual(str(Crim), "Abu Bakar Bashir Indonesian 1938 Leo Cleric")

	def test_Fame_from_DB(self):
		conn = sqlite3.connect("206_Final_Proj_DB.db")
		cur = conn.cursor()

		statement = """
		SELECT *
		FROM Famous
		WHERE name="Abu Bakar Bashir"
		"""
		cur.execute(statement)
		pull = cur.fetchone()
		# print(pull)
		self.assertEqual(type(pull), tuple)
		self.assertEqual(len(pull), 6)
		self.assertEqual(type(pull[0]), int)
		self.assertEqual(pull[0], 108)
		self.assertEqual(type(pull[1]), str)
		self.assertEqual(pull[1], "Abu Bakar Bashir")
		self.assertEqual(type(pull[2]), str)
		self.assertEqual(pull[2], "Indonesian")
		self.assertEqual(type(pull[3]), str)
		self.assertEqual(pull[3], "Cleric")
		self.assertEqual(type(pull[4]), str)
		self.assertEqual(pull[4], "Leo")
		self.assertEqual(type(pull[5]), int)
		self.assertEqual(pull[5], 1938)

		conn.close()

class Test_FBI(unittest.TestCase):
	def test_data_and_aug_values(self):
		#temp_dict = {"year": "1995", "count": 3970, "offense_name": "Aggravated Assault"}
		x = FBI_DBM.FBI_data_supreme()
		#print(x)

		assert(len(x) == 236)
		for i in x:
			assert(len(i) == 5)

		# Year counting below will be inequal as the state of Michigan
		# has gradually been adding a few categories a year to reporting

		# I filter out "None" data, so there should be less than the 64
		# total categories actually represented in the below counts for
		# each year for Michigan
		year_2012_counter = 0
		for i in x:
			if(i["year"]=="2012"):
				year_2012_counter +=1
		assert(year_2012_counter == 44)
		
		year_2016_counter = 0
		for i in x:
			if(i["year"]=="2016"):
				year_2016_counter +=1
		assert(year_2016_counter == 51)

		for i in x:
			if(i["year"]=="2016"):
				if(i["offense_name"]=="Wire Fraud"):
					assert(i["count"]==1098)
					assert(i["classification"]==2)
					assert(i["annual_perc"]==0.2065)

	def test_FBI_cache(self):
		cache_diggity = FBI_DBM.FBI_cache()
		loaded = json.loads(cache_diggity)
		# print(len(loaded["results"]))
		assert(len(loaded["results"])==1664)

		# Year counting should be 64/year constant
		year_2012_counter = 0
		for i in loaded["results"]:
			if(i["year"]=="2012"):
				year_2012_counter +=1
		assert(year_2012_counter == 64)
		
		year_2016_counter = 0
		for i in loaded["results"]:
			if(i["year"]=="2016"):
				year_2016_counter +=1
		assert(year_2016_counter == 64)

	def test_FBI_from_DB(self):
		conn = sqlite3.connect("206_Final_Proj_DB.db")
		cur = conn.cursor()

		statement = """
		SELECT *
		FROM FBI
		WHERE year="2012"
		"""
		cur.execute(statement)
		
		pull = cur.fetchone()
		assert(pull[0]==1)
		assert(pull[1]==2012)
		assert(pull[2]==24505)
		assert(pull[3]=="Aggravated Assault")
		assert(pull[4]==1)
		assert(pull[5]==4.1548)

		pull = cur.fetchone()
		assert(pull[0]==2)
		assert(pull[1]==2012)
		assert(pull[2]==58120)
		assert(pull[3]=="All Other Larceny")
		assert(pull[4]==1)
		assert(pull[5]==9.8541)

		pull = cur.fetchone()
		assert(pull[0]==3)
		assert(pull[1]==2012)
		assert(pull[2]==2411)
		assert(pull[3]=="Arson")
		assert(pull[4]==1)
		assert(pull[5]==0.4088)

		conn.close()

class Test_DPSS(unittest.TestCase):
	def test_DPSS_cache(self):
		total = DPSS_DBM.Investigate_Total_Cached_Incidents()
		assert(total == 141)
		date = DPSS_DBM.DPSS_cache(input_date="01/19/2017")
		date_loaded = json.loads(date)
		assert(type(date_loaded)==dict)
		assert(date_loaded["count"]==15)

	def test_DPSS_from_DB(self):
		conn = sqlite3.connect("206_Final_Proj_DB.db")
		cur = conn.cursor()

		statement = """
		SELECT *
		FROM DPSS
		WHERE CAD_Num=1700065509
		"""
		cur.execute(statement)
		
		pull = cur.fetchone()
		assert(pull[0]==2177)
		assert(pull[1]==1700065509)
		assert(pull[2]=="2017-07-24 12:42:00.0")
		assert(pull[3]=="WALKAWAY PATIENT OR CLIENT")
		assert(pull[4]=="UNIVERSITY HOSPITAL")
		assert(pull[5]=="1500 E MEDICAL CENTER DR")
		assert(pull[6]=="ASSISTANCE PROVIDED")
		assert("kayak" in pull[7])

		# Uncomment the following line to learn the epic and inspirational
		# story of Kayak Man, the hero Ann Arbor deserves.

		#print(pull[7])

		conn.close()

class Test_FBI_Classing(unittest.TestCase):
	def test_listing(self):
		assert("Aggravated Assault" in FBI_Class_Lists.class_i)
		assert("Negligent Manslaughter" in FBI_Class_Lists.class_i)
		assert("Animal Cruelty" in FBI_Class_Lists.class_ii)
		assert("Wire Fraud" in FBI_Class_Lists.class_ii)

# Note: Below class may not be implemented at the time of project submission
# because the map-and-reduce-to-specific-crimes part of the project isn't really
# something that was ever in the proposal and is more for project efforts moving
# forward, so it might not be a fully-fledged thing in this project's life as a
# 206 project as much as it will be as a summer project
class Test_CrimeTagging(unittest.TestCase):
	def test1(self):
		pass

if __name__=="__main__":
	unittest.main()