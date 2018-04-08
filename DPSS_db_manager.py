#print("DPSS_db_manager.py loaded")
import sqlite3

def init_DPSS_table_prime():
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

if(__name__=="__main__"):
	print("DPSS_db_manager as __main__")