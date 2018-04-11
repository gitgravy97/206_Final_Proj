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