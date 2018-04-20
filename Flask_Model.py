import Buildings
import Crime_Tagging

import plotly.graph_objs as go
import plotly.plotly as py
import plotly.tools as tls
import sqlite3 as sqlite

# Visualization of Famous Criminals
def get_criminals(sort_by="name", order="asc"):
	print("Famous Criminal Table Generation")
	conn = sqlite.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()
	statement = """
	SELECT * FROM Famous
	"""
	cur.execute(statement)
	mega = []
	for i in cur:
		recast = (i[0],i[1],i[2],i[3],i[4],str(i[5]))
		mega.append(recast)
		#print(recast)
	
	if(sort_by=="Name"):
		sort_by = 1
	elif(sort_by=="Nationality"):
		sort_by = 2
	elif(sort_by=="Title"):
		sort_by = 3
	elif(sort_by=="Astro"):
		sort_by = 4
	elif(sort_by=="BirthYear"):
		sort_by = 5

	reverse = ""
	if(order=="asc"):
		reverse = False
	elif(order=="desc"):
		reverse = True

	mega_sorted = sorted(mega, key=lambda x: x[sort_by], reverse=reverse)
	#for i in mega_sorted:
	#	print(i)

	conn.close()
	return(mega_sorted)

# Visualizations with FBI Data
def gen_FBI_graph(year_in="2012"):
	print("FBI Graph Generation")
	# Part I - Database Connection 
	conn=sqlite.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()

	# Part II - Build the graph
	labels = []
	values = []

	miniscule = 0

	statement = "SELECT * FROM FBI WHERE Year="
	statement += "'" + str(year_in) + "'"
	cur.execute(statement)
	for i in cur:
		#print(i)
		if(int(i[5]) >= 1):
			labels.append(i[3])
			values.append(int(i[2]))
		elif(int(i[5]) < 1):
			#print("Less than 1%.")
			miniscule += int(i[2])
	labels.append("Other (Offenses Independently Representing < 1% of Total)")
	values.append(miniscule)

	conn.close()

	trace = go.Pie(labels=labels, values=values)

	# Part III - Ensure proper .plot call is made, correct parameters
	py.plot([trace], filename='basic_pie_chart', auto_open=False)

	# Part IV - Export
	x = tls.get_embed('https://plot.ly/~McCoyDoherty/10/')
	#print(x)
	f = open("plot_export_FBI.html","w")
	f.write(x)
	f.close()
	return(x)

# Visualizations with DPSS Data
# BY DORM
def gen_DPSS_dorm_table(sort_by="Name"):
	print("DPSS By Dorm Trigger")
	conn = sqlite.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()
	statement = """
	SELECT location FROM DPSS
	"""
	
	cur.execute(statement)
	
	Dorm_Incidents = []
	for i in cur:
		if(i[0] in Buildings.All_Dorm_Buildings):
			Dorm_Incidents.append(i)
	#print(len(Dorm_Incidents))

	#for i in Dorm_Incidents:
	#	print(i)

	dorm_dict = Buildings.Dorm_Totals(Dorm_Incidents)

	outbound_dict = {}
	if(sort_by=="Name"):
		print("name")
		outbound_dict = sorted(dorm_dict.items(), key=lambda x: x[0],
			reverse=False)
		#for i in outbound_dict:
		#	print(i)
	elif(sort_by=="Freq"):
		print("freq")
		outbound_dict = sorted(dorm_dict.items(), key=lambda x: x[1],
			reverse=True)
		#for i in outbound_dict:
		#	print(i)

	conn.close()
	return(outbound_dict)

# BY INCIDENT TYPE
def gen_DPSS_type_table_unrefined(sort_by="Descrip"):
	print("DPSS By Type Trigger (Refined)")
	conn = sqlite.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()
	statement = """
	SELECT description, count(description) FROM DPSS 
	GROUP BY Description
	"""

	incident_type_counts = []
	cur.execute(statement)
	for i in cur:
		#print(i)
		if(i[0][0]==" "):
			strip_prespace = (i[0][1:], i[1])
			#print(strip_prespace)
			incident_type_counts.append(strip_prespace)
		else:
			incident_type_counts.append(i)

	conn.close()

	incidents_sorted = []

	if(sort_by=="Descrip"):
		#incidents_sorted = incident_type_counts
		incidents_sorted = sorted(incident_type_counts,
			key=lambda x: x[0][0], reverse=False)
		#for i in incidents_sorted:
		#	print(i)
	# Sorting by incident frequency
	elif(sort_by=="Freq"):
		incidents_sorted = sorted(incident_type_counts,
			key=lambda x: x[1], reverse=True)
	return(incidents_sorted)

def gen_DPSS_type_table_refined(sort_by="Descrip"):
	print("DPSS By Type Trigger (Refined)")
	conn = sqlite.connect("206_Final_Proj_DB.db")
	cur = conn.cursor()
	statement = """
	SELECT description, count(description) FROM DPSS 
	GROUP BY Description
	"""

	incident_type_counts = []
	cur.execute(statement)
	for i in cur:
		#print(i)
		if(i[0][0]==" "):
			strip_prespace = (i[0][1:], i[1])
			#print(strip_prespace)
			incident_type_counts.append(strip_prespace)
		else:
			incident_type_counts.append(i)

	conn.close()

	refine_type_counts = Crime_Tagging.Crime_Totals(unrefined_counts=incident_type_counts)

	incidents_sorted = []
	if(sort_by=="Descrip"):
		#incidents_sorted = incident_type_counts
		incidents_sorted = sorted(refine_type_counts.items(),
			key=lambda x: x[0][0], reverse=False)
		#for i in incidents_sorted:
		#	print(i)
	# Sorting by incident frequency
	elif(sort_by=="Freq"):
		incidents_sorted = sorted(refine_type_counts.items(),
			key=lambda x: x[1], reverse=True)
	return(incidents_sorted)