import DPSS_db_manager as DPSS_DB
import Famous_db_manager as FAME_DB
import FBI_db_manager as FBI_DB

import Flasking
# import json
# import sqlite3

print("Core.py")

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
	print(". . . . . "*5)

if(__name__=="__main__"):
	print("Core.py as __main__")
	init_database()

	#gen_graphs()

	Flasking.run_it()