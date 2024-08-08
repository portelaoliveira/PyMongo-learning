from pymongo import MongoClient  # finding data

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll=mydb["dbtable"]


#x=mycoll.find_one()   #for finding single occurences in collection/table
for x in mycoll.find(): #for finding all occurences in collection
    print(x)
