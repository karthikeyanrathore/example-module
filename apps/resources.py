from fastapi import Response
from fastapi import APIRouter


healthcheck_router = APIRouter()
product_router = APIRouter()


@healthcheck_router.get("/")
def health_check():
    return Response("OK", status_code=200)

@product_router.get("/")
def products():
    return Response("prod", status_code=200)
