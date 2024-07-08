import requests
from fastapi.logger import logger
from datetime import datetime

# Base URL for the Coinbase API
BASE_URL = "https://api.coinbase.com/api/v3/brokerage"


# Utility function to convert ISO date string to UNIX timestamp
def to_unix_timestamp(date_str: str) -> int:
    """
    Convert an ISO 8601 formatted date string to a UNIX timestamp.
    
    Args:
        date_str (str): The date string in ISO 8601 format.
        
    Returns:
        int: The UNIX timestamp corresponding to the date string.
    """
    dt = datetime.fromisoformat(date_str)  # Convert ISO date string to datetime object
    return int(dt.timestamp())  # Return the UNIX timestamp


# Function to fetch all products from the API
def get_products():
    """
    Retrieve all products from the Coinbase API.
    
    Returns:
        list: A list of product objects.
        
    Raises:
        Exception: If an error occurs while fetching the products.
    """
    try:
        response = requests.get(f"{BASE_URL}/market/products")  # Make a GET request to the products endpoint
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response.json()["products"]  # Return the products from the JSON response
    except Exception as e:
        logger.error(f"Error fetching products: {e}")  # Log an error message if an exception occurs
        raise  # Reraise the exception


# Function to fetch the server time from the API
def get_server_time():
    """
    Retrieve the current server time from the Coinbase API.
    
    Returns:
        dict: An object containing the server's current time.
        
    Raises:
        Exception: If an error occurs while fetching the server time.
    """
    try:
        response = requests.get(f"{BASE_URL}/time")  # Make a GET request to the server time endpoint
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response.json()  # Return the server time from the JSON response
    except Exception as e:
        logger.error(f"Error fetching server time: {e}")  # Log an error message if an exception occurs
        raise  # Reraise the exception


# Function to fetch the order book for a specific product from the API
def get_product_book(product_id: str):
    """
    Retrieve the order book for a specified product from the Coinbase API.
    
    Args:
        product_id (str): The ID of the product.
        
    Returns:
        dict: An object containing the product's order book details.
        
    Raises:
        Exception: If an error occurs while fetching the product book.
    """
    try:
        response = requests.get(f"{BASE_URL}/market/product_book", params={"product_id": product_id})
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        product_book_data = response.json()  # Get the product book data from the JSON response

        # Adjust the structure to fit the expected schema if needed
        if "pricebook" not in product_book_data:
            product_book_data["pricebook"] = {
                "product_id": product_id,
                "bids": [],
                "asks": [],
                "time": ""
            }

        return product_book_data  # Return the adjusted product book data
    except Exception as e:
        logger.error(f"Error fetching product book for {product_id}: {e}")  # Log an error message if an exception occurs
        raise  # Reraise the exception


# Function to fetch details for a specific product from the API
def get_product(product_id: str):
    """
    Retrieve details for a specified product from the Coinbase API.
    
    Args:
        product_id (str): The ID of the product.
        
    Returns:
        dict: An object containing the product details.
        
    Raises:
        Exception: If an error occurs while fetching the product details.
    """
    try:
        response = requests.get(f"{BASE_URL}/market/products/{product_id}")
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        product_data = response.json()  # Get the product data from the JSON response

        # Handle missing or unexpected 'future_product_details' by setting it to None if not present
        if "future_product_details" not in product_data:
            product_data["future_product_details"] = None

        return product_data  # Return the product data
    except Exception as e:
        logger.error(f"Error fetching product {product_id}: {e}")  # Log an error message if an exception occurs
        raise  # Reraise the exception


# Function to fetch candle data for a specific product from the API
def get_candles(product_id: str, start: str, end: str, granularity: str = "ONE_HOUR"):
    """
    Retrieve candle data for a specified product within a time range from the Coinbase API.
    
    Args:
        product_id (str): The ID of the product.
        start (str): The start timestamp in ISO format.
        end (str): The end timestamp in ISO format.
        granularity (str): The granularity of the candles (default is "ONE_HOUR").
        
    Returns:
        list: A list of candle objects.
        
    Raises:
        Exception: If an error occurs while fetching the candle data.
    """
    try:
        start_timestamp = to_unix_timestamp(start)  # Convert start time from ISO format to UNIX timestamp
        end_timestamp = to_unix_timestamp(end)  # Convert end time from ISO format to UNIX timestamp

        params = {
            "start": start_timestamp,
            "end": end_timestamp,
            "granularity": granularity
        }
        response = requests.get(f"{BASE_URL}/market/products/{product_id}/candles", params=params)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response.json()["candles"]  # Return the candles data from the JSON response
    except Exception as e:
        logger.error(f"Error fetching candles for {product_id}: {e}")  # Log an error message if an exception occurs
        raise  # Reraise the exception


# Function to fetch market trades for a specific product from the API
def get_market_trades(product_id: str):
    """
    Retrieve market trades for a specified product from the Coinbase API.
    
    Args:
        product_id (str): The ID of the product.
        
    Returns:
        list: A list of market trade objects.
        
    Raises:
        Exception: If an error occurs while fetching the market trades.
    """
    try:
        response = requests.get(f"{BASE_URL}/market/products/{product_id}/ticker")
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        return response.json().get("trades", [])  # Return the trades data from the JSON response, defaulting to an empty list if not present
    except Exception as e:
        logger.error(f"Error fetching market trades for {product_id}: {e}")  # Log an error message if an exception occurs
        raise  # Reraise the exception
