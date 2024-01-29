from pymongo import MongoClient
from bson.objectid import ObjectId
import os

MONGO_NON_ROOT_USERNAME = "mongodb"
MONGO_NON_ROOT_PWD = "mongodb"
MONGO_INITDB_DATABASE = "development"
MONGO_HOST = os.getenv("MONGO_HOST", "products-db")
MONGODB_URL  = f"mongodb://{MONGO_NON_ROOT_USERNAME}:{MONGO_NON_ROOT_PWD}@{MONGO_HOST}:27017/{MONGO_INITDB_DATABASE}"

print ("[INFO] Ok, connecting to mongoDB server. connection timeout is set to 10sec.")
mongoclient = MongoClient(MONGODB_URL, connectTimeoutMS=10000)

# print(dir(mongoclient))

# print(mongoclient.list_database_names())

inv_db = mongoclient['development']

# print(dir(inv_db))
# print(list(inv_db.list_collections()))
product_collection = inv_db["product_collection"]

# print(product_collection.find())

def mocker_prod(name, price, quant):
    p_dict = {
        "_id": ObjectId(),
        "product_name": name,
        "product_price": price,
        "product_available_quantity": quant,
    }
    return p_dict

mock_products = [
    mocker_prod("usb-device", 200, 10),
    mocker_prod("headphone-device", 500, 10),
    mocker_prod("mouse-device", 1199, 10),
    mocker_prod("monitor-device", 220, 10),
    mocker_prod("esp8266-device", 1221, 10),
    mocker_prod("inteli7-device", 233, 10),
    mocker_prod("amd-device", 400, 10),
    mocker_prod("nvidia-device", 200, 10),
    mocker_prod("gpu8900-device", 700, 10),
    mocker_prod("watcher-device", 1000, 10),
    mocker_prod("service-device", 1200, 10),
    mocker_prod("logger-device", 3200, 10),
    mocker_prod("psP-device", 900, 10),
    mocker_prod("tty-device", 1100, 10),
]
if not len(list(product_collection.find())):
    # print(product_collection)
    print ("[INFO] Ok, inserting mock data into MongoDB database.")
    ret = product_collection.insert_many(mock_products)
    print(f"inserted_ids: {ret.inserted_ids}")
else:
    print ("[INFO] MongoDB database collection already filled with mock data.")
    # print(list(product_collection.find()))
    pass