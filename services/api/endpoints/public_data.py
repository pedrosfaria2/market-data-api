from fastapi import APIRouter, HTTPException, Query
from ..models.public_data import (
    get_products, get_server_time, get_product_book,
    get_product, get_candles, get_market_trades
)
from ..schemas.public_data import (
    Product, ServerTime, ProductBook, Candle, MarketTrade
)
from typing import List

# Create a new router for API endpoints
router = APIRouter()


# Endpoint to fetch all products
@router.get("/products", response_model=List[Product])
def fetch_products():
    try:
        # Call the function to get products
        products = get_products()
        return products
    except Exception as e:
        # Raise an HTTP 500 error if there's an exception
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to fetch the server time
@router.get("/server-time", response_model=ServerTime)
def fetch_server_time():
    try:
        # Call the function to get server time
        server_time = get_server_time()
        return server_time
    except Exception as e:
        # Raise an HTTP 500 error if there's an exception
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to fetch the order book for a specific product
@router.get("/product-book/{product_id}", response_model=ProductBook)
def fetch_product_book(product_id: str):
    try:
        # Call the function to get the product order book
        product_book = get_product_book(product_id)
        return product_book
    except Exception as e:
        # Raise an HTTP 500 error if there's an exception
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to fetch details for a specific product
@router.get("/product/{product_id}", response_model=Product)
def fetch_product(product_id: str):
    try:
        # Call the function to get product details
        product = get_product(product_id)
        return product
    except Exception as e:
        # Raise an HTTP 500 error if there's an exception
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to fetch candles data for a specific product
@router.get("/candles/{product_id}", response_model=List[Candle])
def fetch_candles(
        product_id: str,
        start: str = Query(..., description="Start timestamp in ISO format"),  # Required start timestamp
        end: str = Query(..., description="End timestamp in ISO format"),  # Required end timestamp
        granularity: str = Query("ONE_HOUR", description="Granularity of the candles")
        # Optional granularity parameter with a default value
):
    try:
        # Call the function to get candles data
        candles = get_candles(product_id, start, end, granularity)
        return candles
    except Exception as e:
        # Raise an HTTP 500 error if there's an exception
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint to fetch market trades for a specific product
@router.get("/market-trades/{product_id}", response_model=List[MarketTrade])
def fetch_market_trades(product_id: str):
    try:
        # Call the function to get market trades
        market_trades = get_market_trades(product_id)
        return market_trades
    except Exception as e:
        # Raise an HTTP 500 error if there's an exception
        raise HTTPException(status_code=500, detail=str(e))
