from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List
from ..models.public_data import (
    get_products, get_server_time, get_product_book,
    get_product, get_candles, get_market_trades
)
from ..schemas.public_data import (
    Product, ServerTime, ProductBook, Candle, MarketTrade
)
from publisher import publish_message  # Import the publisher function for RabbitMQ

# Initialize a new router for API endpoints
router = APIRouter()

# Pydantic model for the message to be published to the queue
class Message(BaseModel):
    message: str

# Endpoint to fetch all available products
@router.get("/products", response_model=List[Product])
def fetch_products():
    """
    Retrieve a list of all products.
    
    This endpoint fetches and returns a list of all available products.
    
    Returns:
        List[Product]: A list of product objects.
        
    Raises:
        HTTPException: If an error occurs while fetching the products.
    """
    try:
        products = get_products()  # Call the function to get products
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise an HTTP 500 error if there's an exception

# Endpoint to fetch the current server time
@router.get("/server-time", response_model=ServerTime)
def fetch_server_time():
    """
    Retrieve the current server time.
    
    This endpoint fetches and returns the server's current time.
    
    Returns:
        ServerTime: An object containing the server's time.
        
    Raises:
        HTTPException: If an error occurs while fetching the server time.
    """
    try:
        server_time = get_server_time()  # Call the function to get server time
        return server_time
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise an HTTP 500 error if there's an exception

# Endpoint to fetch the order book for a specific product
@router.get("/product-book/{product_id}", response_model=ProductBook)
def fetch_product_book(product_id: str):
    """
    Retrieve the order book for a specified product.
    
    Args:
        product_id (str): The ID of the product.
        
    Returns:
        ProductBook: An object containing the product's order book details.
        
    Raises:
        HTTPException: If an error occurs while fetching the product book.
    """
    try:
        product_book = get_product_book(product_id)  # Call the function to get the product order book
        return product_book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise an HTTP 500 error if there's an exception

# Endpoint to fetch details for a specific product
@router.get("/product/{product_id}", response_model=Product)
def fetch_product(product_id: str):
    """
    Retrieve details for a specified product.
    
    Args:
        product_id (str): The ID of the product.
        
    Returns:
        Product: An object containing the product details.
        
    Raises:
        HTTPException: If an error occurs while fetching the product details.
    """
    try:
        product = get_product(product_id)  # Call the function to get product details
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise an HTTP 500 error if there's an exception

# Endpoint to fetch candle data for a specific product
@router.get("/candles/{product_id}", response_model=List[Candle])
def fetch_candles(
        product_id: str,
        start: str = Query(..., description="Start timestamp in ISO format"),  # Required start timestamp
        end: str = Query(..., description="End timestamp in ISO format"),  # Required end timestamp
        granularity: str = Query("ONE_HOUR", description="Granularity of the candles")  # Optional granularity parameter with a default value
):
    """
    Retrieve candle data for a specified product within a time range.
    
    Args:
        product_id (str): The ID of the product.
        start (str): The start timestamp in ISO format.
        end (str): The end timestamp in ISO format.
        granularity (str): The granularity of the candles (default is "ONE_HOUR").
        
    Returns:
        List[Candle]: A list of candle objects.
        
    Raises:
        HTTPException: If an error occurs while fetching the candle data.
    """
    try:
        candles = get_candles(product_id, start, end, granularity)  # Call the function to get candles data
        return candles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise an HTTP 500 error if there's an exception

# Endpoint to fetch market trades for a specific product
@router.get("/market-trades/{product_id}", response_model=List[MarketTrade])
def fetch_market_trades(product_id: str):
    """
    Retrieve market trades for a specified product.
    
    Args:
        product_id (str): The ID of the product.
        
    Returns:
        List[MarketTrade]: A list of market trade objects.
        
    Raises:
        HTTPException: If an error occurs while fetching the market trades.
    """
    try:
        market_trades = get_market_trades(product_id)  # Call the function to get market trades
        return market_trades
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise an HTTP 500 error if there's an exception

# Endpoint to publish a message to a RabbitMQ queue
@router.post("/publish/{queue_name}")
def publish_to_queue(queue_name: str, message: Message):
    """
    Publish a message to a specified RabbitMQ queue.
    
    Args:
        queue_name (str): The name of the queue.
        message (Message): The message to be published.
        
    Returns:
        dict: A dictionary indicating the status of the operation.
        
    Raises:
        HTTPException: If an error occurs while publishing the message.
    """
    try:
        publish_message(queue_name, message.message)  # Call the function to publish a message
        return {"status": "Message published"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Raise an HTTP 500 error if there's an exception
