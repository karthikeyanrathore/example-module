from fastapi import APIRouter
from apps.resources import healthcheck_router, product_router

api_router = APIRouter()

api_router.include_router(healthcheck_router, )
api_router.include_router(product_router, prefix="/products")

