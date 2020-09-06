import os
print("Ensure scrapy, splash and docker are installed")
projectName = input("What is the name of the project")



# Find all <projectName> and replace with input
# In intellji or pycharm edit -> find -> replace in path
# Find : <ProjectName> with your project name

# If using mongodb
# search for #mongoDB or <MongoDBsettings>
# in settings file contain connection data to mongodb uncomment and replace with used variables
# The activate the pipeline
# find by searching
#<MongodbPipeline>
# Make sure mongoDB is running

# then run the command below
os.system('docker run -p 8050:8050 scrapinghub/splash')
# init splash

