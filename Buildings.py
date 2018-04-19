# Buildings.py

# Functions for mapping and reducing the variable location inputs
# from the DPSS data

def Dorm_Totals(all_dorm_incidents):
	totals_dict = {
		"Alice Lloyd":0,
		"Baits":0,
		"Barbour":0,
		"Bursley":0,
		"Business Admin Exec Dorm":0,
		"Couzens":0,
		"East Quad":0,
		"Fletcher":0,
		"Helen Newberry":0,
		"Lawyers Club":0,
		"Markley":0,
		"Martha Cook":0,
		"Mosher Jordan":0,
		"Munger":0,
		"North Quad":0,
		"Northwood":0,
		"Oxford":0,
		"South Quad":0,
		"Stockwell":0,
		"West Quad":0
	}

	for i in all_dorm_incidents:
		if(i[0] in Alice_Lloyd):
			totals_dict["Alice Lloyd"] +=1
		elif(i[0] in Baits):
			totals_dict["Baits"] +=1
		elif(i[0] in Barbour):
			totals_dict["Barbour"] +=1
		elif(i[0] in Bursley):
			totals_dict["Bursley"] +=1
		elif(i[0] in Business):
			totals_dict["Business Admin Exec Dorm"] +=1

		elif(i[0] in Couzens):
			totals_dict["Couzens"] +=1
		elif(i[0] in East_Quad):
			totals_dict["East Quad"] +=1
		elif(i[0] in Fletcher):
			totals_dict["Fletcher"] +=1	
		elif(i[0] in Helen_Newberry):
			totals_dict["Helen Newberry"] +=1
		elif(i[0] in Lawyers_Club):
			totals_dict["Lawyers Club"] +=1

		elif(i[0] in Markley):
			totals_dict["Markley"] +=1
		elif(i[0] in Martha_Cook):
			totals_dict["Martha Cook"] +=1
		elif(i[0] in Mosher_Jordan):
			totals_dict["Mosher Jordan"] +=1	
		elif(i[0] in Munger):
			totals_dict["Munger"] +=1
		elif(i[0] in North_Quad):
			totals_dict["North Quad"] +=1

		elif(i[0] in Northwood):
			totals_dict["Northwood"] +=1
		elif(i[0] in Oxford):
			totals_dict["Oxford"] +=1
		elif(i[0] in South_Quad):
			totals_dict["South Quad"] +=1	
		elif(i[0] in Stockwell):
			totals_dict["Stockwell"] +=1
		elif(i[0] in West_Quad):
			totals_dict["West Quad"] +=1

	#print(totals_dict)
	
	"""
	sort_by_name = sorted(totals_dict.items(), key=lambda x: x[0],
		reverse=False)
	for i in sort_by_name:
		print(i)

	print("====="*15)
	

	sort_by_frequency = sorted(totals_dict.items(), key=lambda x: x[1],
		reverse=True)
	for i in sort_by_frequency:
		print(i)
	"""

	return(totals_dict)

# Alternative Structure: (Implement for summertime)
"""
	Alice Lloyd = {
		"Count":0,
		"Names":["LLOYD ALICE CROCKER HALL", "ALICE LLOYD",
			"ALICE LLOYD RES HALL", "ALICE LLOYD RESIDENCE HALL"]
	}
"""

Alice_Lloyd = [
	"LLOYD ALICE CROCKER HALL",
	"ALICE LLOYD",
	"ALICE LLOYD RES HALL",
	"ALICE LLOYD RESIDENCE HALL"
]

Baits = [
	"BAITS VERA II COMAN HOUSE",
	"BAITS VERA II CONGER HOUSE",
	"BAITS VERA II ZIWET HOUSE",
	"BAITS VERA II THIEME HOUSE",
	"BAITS VERA II ",
	"BAITS VERA II CROSS HOUSE",
	"BAITS VERA I EATON HOUSE",
	"BAITS VERA I STANLEY HOUSE",
	"BAITS/ ZIWET HOUSE"
]

Barbour = [
	"BARBOUR BETSY HOUSE",
	"BETSY BARBOUR",
	"BETSY BARBOUR RES HALL",
	"BETSY BARBOUR RESIDENCE HALL"
]

Bursley = [
	"BURSLEY JOSEPH A & MARGUERITE K HALL",
	"BURSLEY HALL"
]

Business = [
	"BUSINESS ADMIN EXECUTIVE DORM"
]

Couzens = [
	"COUZENS HALL"
]

East_Quad = [
	"EAST QUADRANGLE",
	"EAST QUAD"
]

Fletcher = [
	"FLETCHER HALL"
]

Helen_Newberry = [
	"NEWBERRY HELEN H RESIDENCE",
	"NEWBERRY HALL",
	"HELEN NEWBERRY"
]

Lawyers_Club = [
	"LAWYERS CLUB AND MUNGER CHARLES T RESIDENCES"
]

Markley = [
	"MARKLEY MARY BUTLER HALL",
	"MARKLEY",
	"MARKLEY RES HALL",
	"MARKLEY RESIDENCE HALL",
	"MARY MARKLEY RESIDENCE HALL"
]

Martha_Cook = [
	"COOK MARTHA BUILDING",
	"MARTHA COOK",
	"MARTHA COOK RES HALL"
]

Mosher_Jordan = [
	"MOSHER ELIZA M HALL & JORDAN MYRA B HALL",
	"MOSHER JORDAN",
	"MOSHER JORDAN RES HALL"
]

Munger = [
	"MUNGER GRADUATE RESIDENCES",
	"MUNGER",
	"MUNGER GRAD RES."
]

# Should total ~119
North_Quad = [
	"NORTH QUADRANGLE RESIDENTIAL AND ACADEMIC COMPLEX",
	"NORTH QUAD"
]

Northwood = [
	"NORTHWOOD V APT ",
	"NORTHWOOD II APTS ",
	"NORTHWOOD III APTS ",
	"NORTHWOOD V APT",
	"NORTHWOOD APTS",
	"NORTHWOOD III APTS",
	"NORTHWOOD ",
	"NORTHWOOD I APTS ",
	"NORTHWOOD V ",
	"NORTHWOOD II APTS",
	"NORTHWOOD IV APT",
	"NORTHWOOD COMMUNITY CENTER",
	"NORTHWOOD II ",
	"NORTHWOOD IV APT ",
	"CRAM PLACE COMMUNITY CENTER",
	"NORTHWOOD APARTMENTS",
	"NORTHWOOD I ",
	"NORTHWOOD I APTS",
	"NORTHWOOD V",
	"NORTHWOOD V APTS",
	"NORTHWOOD",
	"NORTHWOOD COMM APTS",
	"NORTHWOOD COMMUNITY APARTMENTS",
	"NORTHWOOD I SVC BUILDING 450",
	"NORTHWOOD I0",
	"NORTHWOOD III",
	"NORTHWOOD III ",
	"NORTHWOOD V APT 2328"
]

Oxford = [
	"OH LAUREL HARPER SEELEY HALL",
	"OH ARTHUR AND HAZEL VANDENBERG HALL",
	"OH MARY ALICE AND LILLIAN GODDARD HALL",
	"OH JULIA ESTHER EMANUEL RESIDENCE",
	"OXFORD VANDENBERG",
	"OH ADELIA CHEEVER RESIDENCE",
	"OH GEDDES RESIDENCE",
	"OH PAMELA NOBLE RESIDENCE",
	"OXFORD GODDARD",
	"OXFORD HOUSING",
	"OXFORD GEDDES",
	"OXFORD RESIDENCES"
]

South_Quad = [
	"SOUTH QUADRANGLE",
	"SOUTH QUAD"
]

Stockwell = [
	"STOCKWELL MADELON LOUISA HALL",
	"STOCKWELL",
	"STOCKWELL RES HALL",
	"STOCKWELL RESIDENCE HALL"
]

West_Quad = [
	"WEST QUADRANGLE",
	"WEST QUAD",
	"WEST QUAD RES HALL"
]

######################################################################
All_Dorm_Sectors = [
	Alice_Lloyd, Baits, Barbour, Bursley, Business,
	Couzens, East_Quad, Fletcher, Helen_Newberry,
	Lawyers_Club, Markley, Martha_Cook, Mosher_Jordan,
	Munger, North_Quad, Northwood, Oxford, 
	South_Quad, Stockwell, West_Quad
]

All_Dorm_Buildings = []
for i in All_Dorm_Sectors:
	for j in i:
		All_Dorm_Buildings.append(j)
######################################################################
