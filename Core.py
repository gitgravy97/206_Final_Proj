import DPSS_db_manager as DPSS_DB
import Famous_db_manager as FAME_DB
import FBI_db_manager as FBI_DB

# import json
# import sqlite3

# Stack Overflow: Apparently double-import risk isn't that bad for Python
# and it just pulls a cached version if a module has already been imported
# So maybe just import modules in the external files but, if needed, don't 
# worry about or avoid importing in Core.py as well

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
	print(". . . . . "*5)	
	DPSS_DB.init_DPSS_table()
	if(DPSS_DB.DPSS_table_empty_check()):
		DPSS_DB.DPSS_table_populate()
	
	print(". . . . . "*5)
	FAME_DB.init_Famous_table()
	if(FAME_DB.Famous_table_empty_check()):
		FAME_DB.Famous_table_populate()
	
	print(". . . . . "*5)
	FBI_DB.init_FBI_table()
	if(FBI_DB.FBI_table_empty_check()):
		FBI_DB.FBI_table_populate()

if(__name__=="__main__"):
	print("Core.py as __main__")
	init_database()