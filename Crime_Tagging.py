# Crime_Tagging.py
# List of tags that, if found in a crime's narrative listing, will
# be used to associate it with a type of crime

# Writing these in mixed-case so will need .upper()//.lower() casting
# in later implementation, but oh well, easier to look at

# https://www.accuracyproject.org/PoliceAbbreviationsandAcronyms-US.html

"""
Relevant Abbreviations
AOA = Assist Outside Agency
CSC = Criminal Sexual Conduct
MDOP = Malicious Destruction of Property
MIP = Minor in Possession
UDAA = Unauthorized Driving Away of Automobile
UIP = Urinating in Public
VCSA = Violation of Controlled Substances Act

Relevant Terms
Burglary = Breaking into a building and stealing things
	Residential Burglary: Burglarizing a home
	Nonresidential Burglary: Burglarizing a non-home entity
Larceny = Theft
Non-Residential Burglary 
"""

def Crime_Totals(unrefined_counts):
	totals_dict = {
		# Health / Safety
		"Fire-Related":0,
		"Health / Safety Check-Ins":0,
		"Medical":0,
		"Missing Person Report":0,
		"Suicide":0,
		# Other
		"Assist Other Agency":0,
		"Bias / Hate Incident":0,
		"Civil Demonstration":0,
		"Death Investigation":0,
		"Domestic Incidents":0,
		"Ordinance Violation":0,
		"Stadium Rule Violation":0,
		"Suspicion Reports":0,
		"Vehicle Incidents":0,
		# Minor Infractions
		"Disorderly Conduct":0,
		"Embezzlement":0,
		"Noise Complaints":0,
		"Skateboarders":0,
		# Criminal Possessions
		"Possession (All Types)":0,
		"Drug Possession":0,
		"Fake ID Possession":0,
		"Minor in Possession":0,
		"Alcohol-Related Incidents":0,
		"Weapon Possession":0,
		# Criminal - NonPossession
		"Arson":0,
		"Assault":0,
		"Breaking & Entering":0,
		"Burglary":0,
		"Extortion":0,
		"Fraud":0,
		"Harassment / Intimidation":0,
		"Obstruction of Justice":0,
		"Robbery":0,
		"Sexual Crimes":0,
		"Stalking":0,
		"Theft":0,
		"Threats Issued":0,
		"Trespassing":0,
		"Destruction of Property":0,
		"Public Urination":0,
		"Resisting Arrest":0
	}

	for row in unrefined_counts:
		# Health & Safety
		for term in Fire_Related:
			if(term.upper() in row[0]):
				totals_dict["Fire-Related"] += row[1]
		for term in Health_and_Safety:
			if(term.upper() in row[0]):
				totals_dict["Health / Safety Check-Ins"] += row[1]
		for term in Medical:
			if(term.upper() in row[0]):
				totals_dict["Medical"] += row[1]
		for term in Missing_Person:
			if(term.upper() in row[0]):
				totals_dict["Missing Person Report"] += row[1]
		for term in Suicide:
			if(term.upper() in row[0]):
				totals_dict["Suicide"] += row[1]

		# Other
		for term in Assist_Agency:
			if(term.upper() in row[0]):
				totals_dict["Assist Other Agency"] += row[1]
		for term in Bias_Hate:
			if(term.upper() in row[0]):
				totals_dict["Bias / Hate Incident"] += row[1]
		for term in Civil_Demonstration:
			if(term.upper() in row[0]):
				totals_dict["Civil Demonstration"] += row[1]
		for term in Death_Investigation:
			if(term.upper() in row[0]):
				totals_dict["Death Investigation"] += row[1]
		for term in Domestic_Incidents:
			if(term.upper() in row[0]):
				totals_dict["Domestic Incidents"] += row[1]
		for term in Ordinance_Violation:
			if(term.upper() in row[0]):
				totals_dict["Ordinance Violation"] += row[1]
		for term in Stadium_Rule_Violation:
			if(term.upper() in row[0]):
				totals_dict["Stadium Rule Violation"] += row[1]
		for term in Suspicion:
			if(term.upper() in row[0]):
				totals_dict["Suspicion Reports"] += row[1]
		for term in Vehicular:
			if(term.upper() in row[0]):
				totals_dict["Vehicle Incidents"] += row[1]

		# Minor Infractions
		for term in Disorderly_Conduct:
			if(term.upper() in row[0]):
				totals_dict["Disorderly Conduct"] += row[1]
		for term in Embezzlement:
			if(term.upper() in row[0]):
				totals_dict["Embezzlement"] += row[1]
		for term in Noise_Complaint:
			if(term.upper() in row[0]):
				totals_dict["Noise Complaints"] += row[1]
		for term in Skateboarders:
			if(term.upper() in row[0]):
				totals_dict["Skateboarders"] += row[1]

		# Criminal Possession
		for term in All_Possession:
			if(term.upper() in row[0]):
				totals_dict["Possession (All Types)"] += row[1]
		for term in Drugs:
			if(term.upper() in row[0]):
				totals_dict["Drug Possession"] += row[1]
		for term in Fake_ID:
			if(term.upper() in row[0]):
				totals_dict["Fake ID Possession"] += row[1]
		for term in MIP:
			if(term.upper() in row[0]):
				totals_dict["Minor in Possession"] += row[1]
		for term in Alcohol:
			if(term.upper() in row[0]):
				totals_dict["Alcohol-Related Incidents"] += row[1]
		for term in Weapons:
			if(term.upper() in row[0]):
				totals_dict["Weapon Possession"] += row[1]

		# Criminal Non-Possession
		for term in Arson:
			if(term.upper() in row[0]):
				totals_dict["Arson"] += row[1]
		for term in Assault:
			if(term.upper() in row[0]):
				totals_dict["Assault"] += row[1]
		for term in Breaking_and_Entering:
			if(term.upper() in row[0]):
				totals_dict["Breaking & Entering"] += row[1]
		for term in Burglary:
			if(term.upper() in row[0]):
				totals_dict["Burglary"] += row[1]
		for term in Extortion:
			if(term.upper() in row[0]):
				totals_dict["Extortion"] += row[1]
		for term in Fraud:
			if(term.upper() in row[0]):
				totals_dict["Fraud"] += row[1]
		for term in Harassment_Intimidation:
			if(term.upper() in row[0]):
				totals_dict["Harassment / Intimidation"] += row[1]
		for term in Obstruction:
			if(term.upper() in row[0]):
				totals_dict["Obstruction of Justice"] += row[1]
		for term in Robbery:
			if(term.upper() in row[0]):
				totals_dict["Robbery"] += row[1]
		for term in Sex_Crimes:
			if(term.upper() in row[0]):
				totals_dict["Sexual Crimes"] += row[1]
		for term in Stalking:
			if(term.upper() in row[0]):
				totals_dict["Stalking"] += row[1]
		for term in Theft:
			if(term.upper() in row[0]):
				totals_dict["Theft"] += row[1]
		for term in Threat:
			if(term.upper() in row[0]):
				totals_dict["Threats Issued"] += row[1]
		for term in Trespass:
			if(term.upper() in row[0]):
				totals_dict["Trespassing"] += row[1]
		for term in Property_Dmg:
			if(term.upper() in row[0]):
				totals_dict["Destruction of Property"] += row[1]
		for term in Public_Urination:
			if(term.upper() in row[0]):
				totals_dict["Public Urination"] += row[1]
		for term in Resisting_Arrest:
			if(term.upper() in row[0]):
				totals_dict["Resisting Arrest"] += row[1]

	#print("Refined Total Counts:")
	sorted_by_label = sorted(totals_dict.items(), key=lambda x: x[0], reverse=False)
	#for i in sorted_by_label:
	#	print(i)
	return(totals_dict)

# Health & Safety
Fire_Related = ["Fire", "Gas", "Smoke"]
Health_and_Safety = ["Health & Safety", "Health And Safety",
	"Health & Safety", "Safety Hazard"]
Medical = ["Ambulance", "Emergenc Dept", "Emergency Dept",
	"Medical", "Personal Injury"]
Missing_Person = ["Missing Person"]
Suicide = ["Suicide"]

# Other
Assist_Agency = ["AOA", "Assist Other", "Assist Outside LE Agency"]
Bias_Hate = ["Bias","Hate"]
Civil_Demonstration = ["Demonstration"]
Death_Investigation = ["Death"]
Domestic_Incidents = ["Domest", "Family"]
Ordinance_Violation = ["Ordinance Violation", "Regents Ordinance"]
Stadium_Rule_Violation = ["Stadium"]
Suspicion = ["Potentially Violent Person", "Suspicious"]
Vehicular = ["Carjacking", "Crash", "Motor", "Operating While",
	"OWI", "Traffic", "UDAA", "Vehicle"]

# Minor Infractions
Disorderly_Conduct = ["Disorderly"]
Embezzlement = ["Embezzle"]
Noise_Complaint = ["Noise"]
Skateboarders = ["SkateBrd", "Skateboard"]

# Criminal - Possession of Naught Things and Scandalous Goods, lol
All_Possession = ["Drug", "Fake ID", "False ID", "Marijuana", 
	"MIP", "Minor In Possession", "Possession", "VCSA", "Weapon"]

Drugs = ["Drug","Marijuana","VCSA"]
Fake_ID = ["Fake ID", "False ID"]
MIP = ["MIP", "Minor In Possession"]
Alcohol = ["Alcohol", "MIP", "Minor In Possession"]
Weapons = ["Weapon"]

# Criminal - Non-Possession
Arson = ["Arson"]
Assault = ["Assault", "Battery", "Domestic Violence"]
Breaking_and_Entering = ["Home Invasion","Illegal Entry" "Unlawful Entry"]
Burglary = ["Burglary"]
Extortion = ["Extort"]
Fraud = ["Fraud"]
Harassment_Intimidation = ["Harassment", "Intimidat"]
Obstruction = ["Obstruct"]
Robbery = ["Robbery"]
Sex_Crimes = ["CSC","Indecent Exposure", "Sex"]
Stalking = ["Stalk"]
Theft = ["Larceny"]
Threat = ["Threat"]
Trespass = ["Trespass"]
Property_Dmg = ["Damage to Police Property","Damage to Property",
	"MDOP", "Property Damage", "Vandalism"]
Public_Urination = ["UIP"] 
Resisting_Arrest = ["Resisting Officer", "Resisting Police", "R&O"]