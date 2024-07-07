import requests
from fastapi.logger import logger
from datetime import datetime

# Base URL for the Coinbase API
BASE_URL = "https://api.coinbase.com/api/v3/brokerage"


# Utility function to convert ISO date string to UNIX timestamp
def to_unix_timestamp(date_str: str) -> int:
    # Convert ISO date string to datetime object
    dt = datetime.fromisoformat(date_str)
    # Return the UNIX timestamp
    return int(dt.timestamp())


# Function to fetch all products from the API
def get_products():
    try:
        # Make a GET request to the products endpoint
        response = requests.get(f"{BASE_URL}/market/products")
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Return the products from the JSON response
        return response.json()["products"]
    except Exception as e:
        # Log an error message if an exception occurs
        logger.error(f"Error fetching products: {e}")
        # Reraise the exception
        raise


# Function to fetch the server time from the API
def get_server_time():
    try:
        # Make a GET request to the server time endpoint
        response = requests.get(f"{BASE_URL}/time")
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Return the server time from the JSON response
        return response.json()
    except Exception as e:
        # Log an error message if an exception occurs
        logger.error(f"Error fetching server time: {e}")
        # Reraise the exception
        raise


# Function to fetch the order book for a specific product from the API
def get_product_book(product_id: str):
    try:
        # Make a GET request to the product book endpoint with the product ID as a parameter
        response = requests.get(f"{BASE_URL}/market/product_book", params={"product_id": product_id})
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Get the product book data from the JSON response
        product_book_data = response.json()

        # Adjust the structure to fit the expected schema if needed
        if "pricebook" not in product_book_data:
            product_book_data["pricebook"] = {
                "product_id": product_id,
                "bids": [],
                "asks": [],
                "time": ""
            }

        # Return the adjusted product book data
        return product_book_data
    except Exception as e:
        # Log an error message if an exception occurs
        logger.error(f"Error fetching product book for {product_id}: {e}")
        # Reraise the exception
        raise


# Function to fetch details for a specific product from the API
def get_product(product_id: str):
    try:
        # Make a GET request to the product details endpoint with the product ID in the URL
        response = requests.get(f"{BASE_URL}/market/products/{product_id}")
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Get the product data from the JSON response
        product_data = response.json()

        # Handle missing or unexpected 'future_product_details' by setting it to None if not present
        if "future_product_details" not in product_data:
            product_data["future_product_details"] = None

        # Return the product data
        return product_data
    except Exception as e:
        # Log an error message if an exception occurs
        logger.error(f"Error fetching product {product_id}: {e}")
        # Reraise the exception
        raise


# Function to fetch candle data for a specific product from the API
def get_candles(product_id: str, start: str, end: str, granularity: str = "ONE_HOUR"):
    try:
        # Convert start and end times from ISO format to UNIX timestamps
        start_timestamp = to_unix_timestamp(start)
        end_timestamp = to_unix_timestamp(end)

        # Set the request parameters with the timestamps and granularity
        params = {
            "start": start_timestamp,
            "end": end_timestamp,
            "granularity": granularity
        }
        # Make a GET request to the candles endpoint with the product ID and parameters
        response = requests.get(f"{BASE_URL}/market/products/{product_id}/candles", params=params)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Return the candles data from the JSON response
        return response.json()["candles"]
    except Exception as e:
        # Log an error message if an exception occurs
        logger.error(f"Error fetching candles for {product_id}: {e}")
        # Reraise the exception
        raise


# Function to fetch market trades for a specific product from the API
def get_market_trades(product_id: str):
    try:
        # Make a GET request to the market trades endpoint with the product ID in the URL
        response = requests.get(f"{BASE_URL}/market/products/{product_id}/ticker")
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Return the trades data from the JSON response, defaulting to an empty list if not present
        return response.json().get("trades", [])
    except Exception as e:
        # Log an error message if an exception occurs
        logger.error(f"Error fetching market trades for {product_id}: {e}")
        # Reraise the exception
        raise
