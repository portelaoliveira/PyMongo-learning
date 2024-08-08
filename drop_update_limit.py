from pymongo import MongoClient                
democlient = MongoClient()
myclient = MongoClient('localhost',27017)
mydb = myclient["demo"]
mycoll=mydb["dbtable"]



#mycoll.drop()   #drop collection
democlient.drop_database("demo")   #for droping the db
print(myclient.list_database_names())


#myquery = { "name": "Peter" }
#newvalues = { "$set": { "name":"abhishek" } }

#mycoll.update_one(myquery, newvalues)#update single query/record
#mycoll.update_many(myquery, newvalues)  #updating many records even using regex
#for x in mycoll.find().limit(3):    #limit used for how much data needed to be shown
 #   print(x)

