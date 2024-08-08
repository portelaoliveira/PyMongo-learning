from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
print(myclient.list_database_names())
