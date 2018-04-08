import DPSS_db_manager as DPSS_DB
import Famous_db_manager as FAME_DB
import FBI_db_manager as FBI_DB

# import json
# import sqlite3

# Stack Overflow: Apparently double-import risk isn't that bad for Python
# and it just pulls a cached version if a module has already been imported


print("Core.py")
"""
try:
	conn = sqlite3.connect("206_Final_Proj_DB.db")
	print("Database loaded")
except Error as e:
	print("Error in loading database")
	print(e)
"""

def init_database():	
	DPSS_DB.init_DPSS_table_prime()
	FAME_DB.init_Famous_table_prime()
	# Only call FAME_DB.Famous_Scrape if db is empty
	#FAME_DB.Famous_Scrape()
	if(FAME_DB.Famous_table_empty_check()):
		FAME_DB.Famous_populate()


if(__name__=="__main__"):
	print("Core.py as __main__")
	init_database()