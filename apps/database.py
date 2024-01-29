from pymongo import MongoClient
import apps.settings as settings

mongoclient = MongoClient(settings.MONGODB_URL)

inv_db = mongoclient['development']
