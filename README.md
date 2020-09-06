# Scrapy_Splash_template
A template to scrap a website with Js render content.

## Setup

To set up this project you will need find and replace functionality
###### Intellji or pycharm:
edit -> find -> replace in path
##Step 1:
Find all \<projectName> and replace with the project name

##Step 2 (If using mongoDB)
If using mongodb
search for #mongoDB or \<MongoDBsettings> in settings file,
in the commented section their is all the variables needed to establish a connection to mongodb 
<br>
Then activate the pipeline by searching \<MongoDBPipeLine>
and add it to the list of pipeline also found by searching for 
\<MongoDBPipeLine>
 <br>
Ensure mongodb Service is running if localhost
##Step 3 (If running Splash)
Look for the comment section of code labeled as \<Splash> uncommented this out
 <br>
then run the command below for splash service 
 <br>
docker run -p 8050:8050 scrapinghub/splash
