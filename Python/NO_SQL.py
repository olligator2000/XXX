
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://porshina1992:Qq1111111111@cluster0.h5gxg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client["scool"]
print(db)

students = db["students"]

# students.insert_one({ "name": "Alice", "age": 25, "profession": "Engineer" })
# students.insert_many([{ "name": "Mike", "age": 21, "profession": "Engineer" },
#                      { "name": "Bob", "age": 23, "profession": "Engineer" },
#                      { "name": "Jone", "age": 24, "profession": "Engineer" }])
for i in students.find():
    print(i)

students.update_many({ "name": "Alice" }, { "$set": { "age": 27 } })