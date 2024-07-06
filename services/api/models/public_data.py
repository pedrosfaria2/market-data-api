import requests
from fastapi.logger import logger

BASE_URL = "https://api.coinbase.com/api/v3/brokerage"

def get_products():
    try:
        response = requests.get(f"{BASE_URL}/market/products")
        response.raise_for_status()
        return response.json()["products"]
    except Exception as e:
        logger.error(f"Error fetching products: {e}")
        raise

def get_server_time():
    try:
        response = requests.get(f"{BASE_URL}/time")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error fetching server time: {e}")
        raise

def get_product_book(product_id: str):
    try:
        response = requests.get(f"{BASE_URL}/market/product_book", params={"product_id": product_id})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error fetching product book for {product_id}: {e}")
        raise

def get_product(product_id: str):
    try:
        response = requests.get(f"{BASE_URL}/market/products/{product_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error fetching product {product_id}: {e}")
        raise

def get_candles(product_id: str, start: int = None, end: int = None, granularity: str = "ONE_HOUR"):
    try:
        params = {
            "granularity": granularity
        }
        if start:
            params["start"] = start
        if end:
            params["end"] = end
        response = requests.get(f"{BASE_URL}/market/products/{product_id}/candles", params=params)
        response.raise_for_status()
        return response.json()["candles"]
    except Exception as e:
        logger.error(f"Error fetching candles for {product_id}: {e}")
        raise

def get_market_trades(product_id: str):
    try:
        response = requests.get(f"{BASE_URL}/market/products/{product_id}/ticker")
        response.raise_for_status()
        return response.json().get("trades", [])
    except Exception as e:
        logger.error(f"Error fetching market trades for {product_id}: {e}")
        raise
