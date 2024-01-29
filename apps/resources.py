from fastapi import Response
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Body
from bson.objectid import ObjectId


from apps.database import inv_db

healthcheck_router = APIRouter()
product_router = APIRouter()
order_router = APIRouter()

def transform_products(device):
    tp_dict = {
        "product_id": str(device["_id"]),
        "product_name": str(device["product_name"]),
        "product_price": int(device["product_price"]),
        "product_available_quantity": int(device["product_available_quantity"]),
    }
    return tp_dict

@healthcheck_router.get("/")
def health_check():
    return Response("OK", status_code=200)

@product_router.get("/")
def products(offset:int =0, limit: int=20, min_price:int =None, max_price:int =None):
    pipe_include, match_pipeline = {}, {}
    # print(list(inv_db.product_collection.find()))
    if min_price:
        pipe_include["$gte"] = int(min_price)
    if max_price:
        pipe_include["$lte"] = int(max_price)
    if pipe_include:
        match_pipeline = { "$match": { "product_price":  pipe_include} }
    
    aggr = inv_db.product_collection.aggregate
    if match_pipeline:
        inv_products = aggr([match_pipeline, {"$skip": int(offset) }, { "$limit": int(limit) }])
    else:
        inv_products = aggr([{"$skip": int(offset) }, { "$limit": int(limit) }])
    data = []
    for device in inv_products:
        data.append(transform_products(device))
    
    total_records = int(inv_db.product_collection.count_documents({}))
    next_offset = offset + limit if total_records > offset + limit else None
    prev_offset = offset - limit if offset > 0 else None
    pag_metadata = {
        "limit": limit,
        "nextOffset":next_offset,
        "prevOffset":prev_offset,
        "total":total_records,
    }
    return JSONResponse(content={"data": (data), "page": pag_metadata}, status_code=200)

@order_router.post("/") #TODO  take payload via BaseModel .
def order_product(payload= Body(None)):
    if not payload:
        return Response("Bad Payload", status_code=404)

    prods = payload['items']
    added_amount = 0
    for prod in prods:
        # use find_one
        is_prod_exists = inv_db.product_collection.find({"_id": ObjectId(str(prod["productId"]))})
        try:
            device = next(is_prod_exists)
            if (device["product_available_quantity"] < int(prod["boughtQuantity"])):
                return JSONResponse(
                    {"message": f"quantity of product:{device['product_name']} to buy exceeds available quantity in inventory "}, 
                    status_code=404
                )
            added_amount += (int(prod["boughtQuantity"]) * device["product_price"])
            # update inventory
            device["product_available_quantity"] = device["product_available_quantity"] - int(prod["boughtQuantity"])
            inv_db.product_collection.update_one(
                {"_id": ObjectId(str(prod["productId"]))},
                {"$set": device},
                upsert=False
            )
        except StopIteration:
            raise
    
    order_collect = inv_db["order_collection"]
    doc_payload_insert = {
        "items": prods,
        "total_amount": added_amount,
        "user_address": payload["user_address"],
    }
    ret = order_collect.insert_one(doc_payload_insert)
    data = doc_payload_insert.copy()
    del data["_id"]
    # print(ret.inserted_id)
    data["createdOn"] = str(ret.inserted_id)
    # print(data)
    return JSONResponse(content={"data": data, "message": "successful created new order."}, status_code=200)