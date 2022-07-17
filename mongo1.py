import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
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