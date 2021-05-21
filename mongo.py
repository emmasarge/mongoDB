import os
import pymongo
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebs"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to mONGO: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()

# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]
# coll.insert_many(new_docs)

for doc in documents:
    print(doc)
