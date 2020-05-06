# DistributedBirding
Tool for planning distributed birding events using eBird data

### TL;DR SETUP
- Replace the Contacts.csv file in data/external with your own contacts file.
- Run all cells in the Jupyter notebook, DistributedBirding.ipynb.

### How to Use

When a distributed team is running a Big Day event, the goal is to find as many
species of birds as possible in a 24 hour period. Using the files output by
this tool, you can see where to concentrate your efforts for maximum effect.

Using the __my5mr-uniques.csv__ and __my5mr-limited.csv__ files, each team member 
can see birds that only they or 3 or fewer team members have a probability
of finding. This is because the species have been seen by others in the past
14 days in these locations according to the eBird data.

With the interactive map in __my5mr-map_NAME.html__, each person can see their 
5MR along with markers for each hotspot. The markers are color-coded so that
**lightgrey** is the bottom third for quantity of species, 
**lightcyan** is the middle and **cornflowerblue** is the top third. Hovering
over a marker shows the name of the hotspot, and clicking on it shows the
species count at that location.

To get the best possible coverage over the combined 5MRs, you can use
the _my5mr-unique-hotspots.csv_ file to see hotspots that are unique to you.
This may mean that you will see species that no one else will.

### INPUTS

The only required input is a spreadsheet of birding contacts. For each person,
either an address or latitude/longitude is required to determine their 5MR.
The tool can read CSV or Excel files. 

Replace the Contacts.csv file in data/external with your own contacts file.
Several examples can be found in the SampleInputs directory.

### OUTPUTS

The bulk of the output from this tool is found in the reports directory. There
are interactive maps in HTML format, and spreadsheets with various data in
CSV format. 

#### Personalized Files  
- my5mr-DATE_NAME.csv: Contains the observations for the last 14 days in the 5MR for NAME    
- my5mr-map_NAME.html: An interactive map of each 5MR circle with 
hotspots and counts. View with Chrome, Safari or other browser.  
  

#### Common Files  
- my5mr-team_circles.html: An interactive map with 5MR circles for all participants.
View with Chrome, Safari or other browser.  
- my5mr-hotspots.csv: A list of hotspots in their 5MR for each person    
- my5mr-limited.csv: A list of all species that only appear in 3 or less individual 5MRs    
- my5mr-unique-hotspots.csv: For each person, a list of hotspots that are unique 
to you (i.e. in no one else's 5MR)
- my5mr-uniques.csv: Contains a list of species for each person that was only 
seen in their 5MR  


## Region Codes
The region codes used by eBird look something like "US-CA-085"
 (Santa Clara County, CA USA). These can be handled automatically by the code, at 
 least in the US.   
 
If you need to find your region code manually, follow these steps:
- Go to https://ebird.org/explore  
- Enter your county in the search field for "Explore Regions"  
- When the page opens, look at the URL. Your region is after "region/" and 
before "?", e.g. for US-CA-085 the url would be 
https://ebird.org/region/US-CA-085?yr=all.

The code will look at all of the 5MRs for all of the partipants, and intersect
those with the counties for the US. For each county that intersects, the eBird
region code is found and added to the list for hotspots, observations, etc.

If you would like to restrict the list of counties, you can manually enter 
region codes in the Parameters file, found in data/external. An example is
found in SampleInputs/Parameters-Regions.csv.

## Resource Usage
There are two services to be aware of as you run this code. The first is a
geolocation service Nominatim. Each lookup is delayed by one second to avoid
hitting the server too hard. In addition, there is a local cache in 
data/interim/GeolocationCache.csv to avoid re-querying for an address. See their 
terms of usage for more information, found 
[here](https://operations.osmfoundation.org/policies/nominatim/).

The other service is eBird, and we try to limit the calls we make although we
do not cache this information currently.
