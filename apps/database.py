from pymongo import MongoClient
import apps.settings as settings

mongoclient = MongoClient(settings.MONGODB_URL, connectTimeoutMS=10000)

inv_db = mongoclient['development']
