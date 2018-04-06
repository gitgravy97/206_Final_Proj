import DPSS_db_manager
import Famous_db_manager
import FBI_db_manager

import json
import sqlite3
# Stack Overflow: Apparently double-import risk isn't that bad for Python
# and it just pulls a cached version if a module has already been imported

print("Core.py")

def init_database():
	try:
		conn = sqlite3.connect("206_Final_Proj_DB")
	except Error as e:
		print(e)
	cur = conn.cursor()


if(__name__=="__main__"):
	print("Core.py as __main__")
	init_database()