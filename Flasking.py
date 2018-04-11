from flask import Flask, render_template
import Flask_Model as Model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>McCoy's SI 206 Final Project!</h1>
        <ul>
            <li><a href="/Vis-1"> Visualization I: Famous Criminals - Data Table </a></li>
            <li><a href="/Vis-2"> Visualization II: FBI Pie Charts </a></li>
            <li><a href="/Vis-3"> Visualization III </a></li>
            <li><a href="/Vis-4"> Visualization IV </a></li>
        </ul>
    '''

# This could be done in less lineswith GET/POST division
# would be harder for me to navigate and I'm just not
# comfortable enough working with GET/POST division yet.
@app.route('/Vis-1/')
def V1_Menu():
	return(render_template("Vis-1-Menu.html"))

@app.route('/Vis-1/Name')
def V1_Name():
	crims = Model.get_criminals(sort_by="Name")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/Nationality')
def V1_Nationality():
	crims = Model.get_criminals(sort_by="Nationality")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/Title')
def V1_Title():
	crims = Model.get_criminals(sort_by="Title")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/Astro')
def V1_Astro():
	crims = Model.get_criminals(sort_by="Astro", order="asc")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/BirthYear')
def V1_BirthYear():
	crims = Model.get_criminals(sort_by="BirthYear", order="desc")
	return(render_template("fame_crims.html",fame_ppl=crims))

######################################################################

@app.route('/Vis-2/')
def V2_Menu():
	return(render_template("Vis-2-Menu.html"))

@app.route('/Vis-2/yr=2012')
def V2_2012():
	print("V2 triggered (year=2012)")
	pie = Model.gen_FBI_graph(year_in="2012")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2012"))

@app.route('/Vis-2/yr=2013')
def V2_2013():
	print("V2 triggered (year=2013)")
	pie = Model.gen_FBI_graph(year_in="2013")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2013"))

@app.route('/Vis-2/yr=2014')
def V2_2014():
	print("V2 triggered (year=2014)")
	pie = Model.gen_FBI_graph(year_in="2014")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2014"))

@app.route('/Vis-2/yr=2015')
def V2_2015():
	print("V2 triggered (year=2015)")
	pie = Model.gen_FBI_graph(year_in="2015")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2015"))

@app.route('/Vis-2/yr=2016')
def V2_2016():
	print("V2 triggered (year=2016)")
	pie = Model.gen_FBI_graph(year_in="2016")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2016"))

######################################################################

@app.route('/Vis-3')
def V3():
	return("v3 temp placeholder")

######################################################################

@app.route('/Vis-4')
def V4():
	return("v4 temp placeholder")

######################################################################

def run_it():
	app.run()