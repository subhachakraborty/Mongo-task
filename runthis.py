from main import mongo

if __name__ == "__main__":
    # This is Mongodb connection Url
    uri = "mongodb+srv://subha_mongo:L7L1VBZqYTPDJ68C@test.wel9t.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    obj = mongo(uri, "ORDERED", "mongodb", "sample")
    # Csv file Insertion Into Mongodb
    obj.list_to_db("carbon_nanotubes.csv")
    # Single value Insert
    obj.insert({"name": "John", "address": "Highway 37"})
    # Bulk insert
    obj.bulk_insert([
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Amy", "address": "Apple st 652"}])
    # obj.find(all=True)
    # Find a value
    obj.find(value={"name": "Hannah", "address": "Mountain 21"})
    # Delete a document
    obj.delete({"name": "Amy"})
    # Update a document
    obj.update({"name": "Amy"}, {"$set": {"name": "namechanged"}})
    # obj.deleteall()
