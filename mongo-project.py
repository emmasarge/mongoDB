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

def show_menu():
    print("Option 1: add a record")
    print("Option 2: find a record by name")
    print("Option 3: edit a record")
    print("Option 4: delete a record")
    print("Option 5: exit the menu")

    option = input("Enter an option: ")
    return option


def get_record():
    first = input("enter first name: ")
    last = input("enter last name: ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("error in access")

    if not doc:
        print("")
        print("error no results found")

    return doc



def add_record():
    print("")
    first = input("enter first name: ")
    last = input("enter last name: ")
    dob = input("enter birthdate: ")
    gender = input("enter gender: ")
    nationality = input("enter  nationality: ")
    occupation = input("enter occupation: ")
    hair_color = input("enter hair color: ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "nationality": nationality,
        "occupation": occupation,
        "hair_color": hair_color

    }

    try:
        coll.insert(new_doc)
        print("")
        print("document inserted")
    except:
        print("error accessing database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ":" + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v, in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v
        try:
            coll.update_one(doc, {"$set" : update_doc})
            print("")
            print("document updated")
        except:
            print("error accessing database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ":" + v.capitalize())
        
        print("")
        confirmation = input("is this the document you would like to delete permananently? \n Y or N >")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("document DELETED")
            except:
                print("error accessing the database")

        else:
            print("document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid options")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()






