
BACKEND_CORS_ORIGINS = 1

API_PREFIX = "/v1"

MONGO_NON_ROOT_USERNAME = "mongodb"
MONGO_NON_ROOT_PWD = "mongodb"
MONGO_INITDB_DATABASE = "development"
MONGODB_URL  = f"mongodb://{MONGO_NON_ROOT_USERNAME}:{MONGO_NON_ROOT_PWD}@localhost:27017/{MONGO_INITDB_DATABASE}"