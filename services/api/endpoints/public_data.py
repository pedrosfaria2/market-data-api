from fastapi import APIRouter, HTTPException
from ..models.public_data import (
    get_products, get_server_time, get_product_book,
    get_product, get_candles, get_market_trades
)
from ..schemas.public_data import (
    Product, ServerTime, ProductBook, Candle, MarketTrade
)
from typing import List

router = APIRouter()

@router.get("/products", response_model=List[Product])
def fetch_products():
    try:
        products = get_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/server-time", response_model=ServerTime)
def fetch_server_time():
    try:
        server_time = get_server_time()
        return server_time
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/product-book/{product_id}", response_model=ProductBook)
def fetch_product_book(product_id: str):
    try:
        product_book = get_product_book(product_id)
        return product_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/product/{product_id}", response_model=Product)
def fetch_product(product_id: str):
    try:
        product = get_product(product_id)
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/candles/{product_id}", response_model=List[Candle])
def fetch_candles(product_id: str, start: int = None, end: int = None, granularity: str = "ONE_HOUR"):
    try:
        candles = get_candles(product_id, start, end, granularity)
        return candles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/market-trades/{product_id}", response_model=List[MarketTrade])
def fetch_market_trades(product_id: str):
    try:
        market_trades = get_market_trades(product_id)
        return market_trades
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
