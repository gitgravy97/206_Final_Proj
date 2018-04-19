Final Project Read-Me
SI 206 - Winter 2018

Name 	McCoy Doherty
Uniq	McShaneD

(Note: This looks odd on GitHub's website, maybe revise)
(Although revision would make it look less cool in Sublime)
======================================================================
Overview && Setup
======================================================================
My project uses three data sources. I will start by explaining a bit about
each data source and things to be aware of for each.

1) The FBI's Crime-Data Exploration API
This API requires an API key be passed in to make the requests.
If you go to the following link and scroll slightly down the page,
it will just give you an API key to use.

>>>>>>>>>>>>>>>>>>>>IMPORTANT<<<<<<<<<<<<<<<<<<<<
[ Link: https://crime-data-explorer.fr.cloud.gov/api ]
Create a new file called "FBI_API_Key.py" in the project's main directory
and write a single line of code:
	my_key = ""
where the API key issued to you goes between the quotation marks.
>>>>>>>>>>>>>>>>>>>>>>>END<<<<<<<<<<<<<<<<<<<<<<<


Use: A call is made that retrieves crime data on frequency of different 
categories of criminal infractions, specifically as reported within the
state confines of Michigan.

2) The Famous People (.com)
This is a website that lists famous people and offers facts and overviews
of their stories and lives. To stick with the crime theme, the program 
will scrape a multi-page index of famous criminals and then traverse 
/ crawl through their individual page listings, scraping basic demographic
data about each criminal (as available).
[ Link: https://www.thefamouspeople.com/criminals.php?page=1 ]

3) University of Michigan Department of Public Safety & Security
 - Daily Fire & Crime Incident Log
There is a website onwhich the campus police department discloses reported
incidents relevant to student safety (i.e. fire and crime), likely in efforts
to be compliant with the Clery Act. The page uses javascript to internally
render API calls that show each day's data on request. While I don't know
javascript, I read the page's code and came to understand how I could just
call the API directly with my code.
[ Link: https://www.dpss.umich.edu/content/crime-safety-data/daily-crime-fire-log/ ]

>>>>>>>>>>>>>>>>>>>>IMPORTANT<<<<<<<<<<<<<<<<<<<<
This API has absolutely horrible response times and it has to call each
individual day. I've pulled all of the data for my target range, September
1st of 2015 to March 31st of 2018, and cached it. It took a lot of time
and, sometimes during the middle of the day, my requests would time-out.

This is why I am bundling my cache files into my Github repository.
While my code does have the capacity to reconstitute the cache, it just
honestly isn't advisable. I was geeked about working with this data and 
dealt with the hours waiting but I don't expect the grading / teaching 
staff to.

Feel free to delete
	fame_cache.json
	FBI_cache.json
But I would seriously recommend keeping
	DPSS_cache.json
>>>>>>>>>>>>>>>>>>>>>>>END<<<<<<<<<<<<<<<<<<<<<<<
======================================================================
Running the Project
======================================================================
Once you've cloned the repository, acquired your FBI API key and put
it in the file as instructed above and installed the dependencies from
the requirements.txt file, you should be ready to start running the
project.
	$ python3 Core.py

The first thing that will happen is that the program builds the database
and pulls from the necessary caches as available. It offers the user the
option to drop tables that already appear to exist, rebuilding said tables
as necessary.

The program then switches into Flask and you can open your browser of
choice and go to localhost:5000 to see the homepage for my project.

There are 4 visualization options, which lead to menu pages. From these
menu pages, different specifications for the visualization can be selected.
The visualization will be generated on selecting an option, also offering
the option to kick back to the visualization-options menu or to the
overall project homepage menu.

======================================================================
Visualization Options
======================================================================
1) Famous Criminals - Data Table 		[Just Flask]
2) FBI - Michigan Crime Pie Charts 		[Flask + Plotly]
3) DPSS Dorm Incidents 					[Just Flask]
4) DPSS Incidents by Type 				[Just Flask]

======================================================================
Structural Walkthrough
======================================================================
> > > Core.py < < <
The unifying central file is Core.py, which branches out and uses the
three database manager files to setup the database and its tables,
dropping and regenerating tables as needed. Tables are populated from
cache files, which are reconstituted as necessary.

> > > [variable]_db_manager.py < < <
All of the [variable]_db_manager.py files follow relatively similar
structures. They contain functions to be used by the Core.py file.
There's always an init_[variable]_table() function to handle table
establishment and reconstitution as necessary.
There are also functions to handle making requests or scraping data
and functions to handle caching.
There are additionally functions to check if tables are empty and
functions to populate the tables with acquired data.

> > > FB_db_manager.py < < <
(Unique Components)
There are three functions that are unique to this module.
[1] Function "FBI_data_supreme()" calls two functions that add secondary 
attributes to the database, which I will cover in the coming function 
explanations.
(Note on variable names: aug_1 and aug_2 are short for "augmentation_1"
and "augmentation_2")
[2] Function "FBI_data_add_classification(basic_dict)" takes in a
dictionary of crime data that comes from the API call and is about to be
used to populate the FBI table in the database. 
It then reaches to an external file FBI_Class_Lists.py to determine 
which classification, Class 1 or Class 2, a given table row's crime type
belongs to. These classes distinguish types of crime forwhich more or less
detailed data exists, which is something you can research the extent of as
interested.
[3] FBI_data_add_annual_percentage(basic_dict) takes the same dictionary 
as above, and then calculates for each row what that type of crime's
contribution was to the total percent of crime reported that year.

> > > Famous_db_manager.py < < <
(Unique Components)
[1] Class "Criminal" is used to help process the data, and became useful for
debugging purposes.
[2] Function "Famous_Scrape()" builds index URL's and scrapes the index
pages to build a base of URL's for individual criminal pages, which are 
then scraped for basic demographic data as available.

> > > DPSS_db_manager.py < < <
(Unique Components)
The main thing to know here is that Month_Harvester scrapes a month's worth
of data from a specific year, which takes a long time. I use this function
to build what are basically switch-on-off blocks in the form of 
Harvest_20XY functions with optional parameters Q1-Q4, i.e. Quarter 1-4,
which can be toggled on and off (except for 2015) to harvest data in 
chunks but chunks of manageable size // wait-time, months.

I definitely need to go back and add comments and clean up some of this
module in particular.

> > > Flasking.py < < <
This module handles the establishment of the different webpages,
calls functions from the Model module, and pipelines the data into the
Jinja HTML templates for display. 

> > > Flask_Model.py < < <
The functions in this module pull relevant information from the database
by using SQL queries and then either returning the data, in most cases,
or in the case of the FBI pie-chart generator, returns the HTML
code for the plotly offline rendering.
Model.gen_FBI_graph() also writes an external copy of the offline 
plotly html rendering code, should that be desired.
(Filename: "plot_export_FBI.html")

> > > Buildings.py < < <
This module just maps and reduces the variable labels for different
dorm locations in the DPSS reports to singular names.
It also has a function, Dorm_Totals(), which takes a single parameter,
all_dorm_incidents, and then uses dictionary aggregation to count the
incident frequencies for each dorm.

======================================================================
Next Steps
======================================================================
I hope to clean up some of the DPSS_db_manager.py file and include more
comments to make things more understandable, because looking back at it
after having not opened it in a while, it seems to need some clarification.

I plan on dropping the FBI and Famous People components and turning the
project primarily into an application that works with the harvested DPSS
data.

I'll be making it more interactive, implementing some of the GET/POST
stuff we briefly touched at the end of the course, and supporting more
options involving Plotly-In-Flask. Time-V-Frequency plotting will see
a lot of implementation as well.

I work for the University of Michigan Department of Housing and I've
had coworkers and superiors take some interest in what I'm doing and
that's why I chose to work with Flask; I want this to eventually be a 
website application they could access and interact with to see trends.
Additionally, it'd be really cool for crime-fascinated locals or just 
local students in general interested in seeing campus crime data.
(This makes me really glad I went to the Heroku lecture.)

Another feature I want to implement is the ability to insert a date
or range of dates and return all incident reports for that date or
span of dates.

======================================================================
The End
======================================================================