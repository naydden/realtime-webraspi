from pymongo import MongoClient,errors
import datetime

# global variables for MongoDB host (default port is 27017)
DOMAIN = 'mydb'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
	# try to instantiate a client instance
	client = MongoClient(
		host = [ str(DOMAIN) + ":" + str(PORT) ],
		serverSelectionTimeoutMS = 3000, # 3 second timeout
	)

	# print the version of MongoDB server if connection successful
	print ("server version:", client.server_info()["version"])

	client.drop_database('air_data')
	# creates my db
	#mydb = client["air_data"]
	exit();
	# get the database_names from the MongoClient()
	database_names = client.list_database_names()
	print ("\ndatabases:", database_names)

	# creates a collection
	mycol = mydb["bme680"]
	# checks if collection exists
	print(mydb.list_collection_names())

	mydoc = { "timestamp": datetime.datetime.now().replace(microsecond=0).isoformat(), "temperature": 0, "pressure": 0, "humidity": 0, "airq": 0 }
	mycol.insert_one(mydoc)
	mydoc = { "timestamp": datetime.datetime.now().replace(microsecond=0).isoformat(), "temperature": 1, "pressure": 2, "humidity": 3, "airq": 4 }
	mycol.insert_one(mydoc)

	for x in mycol.find():
		print(x)

except errors.ServerSelectionTimeoutError as err:
	# set the client and DB name list to 'None' and `[]` if exception
	client = None
	database_names = []

	# catch pymongo.errors.ServerSelectionTimeoutError
	print ("pymongo ERROR:", err)

print ("\ndatabases:", database_names)




# client = MongoClient(<<MONGODB URL>>)
# db=client.admin
# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
