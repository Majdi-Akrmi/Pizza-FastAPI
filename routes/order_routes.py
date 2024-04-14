from fastapi import APIRouter

order_router = APIRouter(
    prefix = '/order',
    tags = ['order']
)

@order_router.get('/')
async def orders():
    return {"message": "Orders"}