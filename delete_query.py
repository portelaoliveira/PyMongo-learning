from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll=mydb["dbtable"]


myquery={"name":{"$regex":"^S"}}
myquery={"name":"Sandy"}

mydoc=mycoll.delete_many(myquery)  #deleting multiple records using regex
mydoc=mycoll.delete_one(myquery)   #deleting specific single record
for y in mycoll.find():
    print(y)

