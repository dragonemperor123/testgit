import pymongo



client = pymongo.MongoClient("mongodb+srv://Adwait:Darkmatter!1@cluster0.g1q8onc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d ={
    "name":"Adwait",
    "email":"adwaitls123@gmail.com",
    "surname":"sawant"

}

db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)