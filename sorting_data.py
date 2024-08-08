from pymongo import MongoClient                
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll=mydb["dbtable"]

mydoc=mycoll.find().sort('name',1)  #ascending   #sorting data in aplhabetical order
mydoc=mycoll.find().sort('name',-1)  #descending 
for x in mydoc:
    print(x)
