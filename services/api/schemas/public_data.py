from pydantic import BaseModel
from typing import List, Optional, Union


# Model for Server Time
class ServerTime(BaseModel):
    iso: str  # ISO formatted date-time string
    epochSeconds: str  # Epoch time in seconds as a string
    epochMillis: str  # Epoch time in milliseconds as a string


# Model for entries in the Product Book (bids and asks)
class ProductBookEntry(BaseModel):
    price: str  # Price of the bid or ask
    size: str  # Size of the bid or ask


# Model for the Price Book inside the Product Book
class ProductBookPriceBook(BaseModel):
    product_id: str  # ID of the product
    bids: List[ProductBookEntry]  # List of bids
    asks: List[ProductBookEntry]  # List of asks
    time: str  # Timestamp of the price book


# Model for the Product Book, which contains the Price Book
class ProductBook(BaseModel):
    pricebook: ProductBookPriceBook  # Nested Price Book


# Model for FCM Trading Session Details
class FCMTradingSessionDetails(BaseModel):
    is_session_open: Optional[bool]  # Whether the session is open
    open_time: Optional[str]  # Opening time of the session
    close_time: Optional[str]  # Closing time of the session


# Model for Perpetual Details
class PerpetualDetails(BaseModel):
    open_interest: Optional[str]  # Open interest for perpetual contracts
    funding_rate: Optional[str]  # Funding rate for perpetual contracts
    funding_time: Optional[str]  # Funding time for perpetual contracts


# Model for Future Product Details
class FutureProductDetails(BaseModel):
    venue: Optional[str]  # Venue of the future product
    contract_code: Optional[str]  # Contract code of the future product
    contract_expiry: Optional[str]  # Expiry date of the contract
    contract_size: Optional[str]  # Size of the contract
    contract_root_unit: Optional[str]  # Root unit of the contract
    group_description: Optional[str]  # Description of the group
    contract_expiry_timezone: Optional[str]  # Timezone of the contract expiry
    group_short_description: Optional[str]  # Short description of the group
    risk_managed_by: Optional[str]  # Entity managing the risk
    contract_expiry_type: Optional[str]  # Type of contract expiry
    perpetual_details: Optional[PerpetualDetails]  # Perpetual details (if any)
    contract_display_name: Optional[str]  # Display name of the contract


# Model for Product Details
class Product(BaseModel):
    product_id: str  # ID of the product
    price: str  # Current price of the product
    price_percentage_change_24h: str  # Percentage price change in the last 24 hours
    volume_24h: str  # Volume in the last 24 hours
    volume_percentage_change_24h: str  # Percentage volume change in the last 24 hours
    base_increment: str  # Base increment of the product
    quote_increment: str  # Quote increment of the product
    quote_min_size: str  # Minimum quote size
    quote_max_size: str  # Maximum quote size
    base_min_size: str  # Minimum base size
    base_max_size: str  # Maximum base size
    base_name: str  # Name of the base currency
    quote_name: str  # Name of the quote currency
    watched: bool  # Whether the product is being watched
    is_disabled: bool  # Whether the product is disabled
    new: bool  # Whether the product is new
    status: str  # Status of the product
    cancel_only: bool  # Whether the product is cancel-only
    limit_only: bool  # Whether the product is limit-only
    post_only: bool  # Whether the product is post-only
    trading_disabled: bool  # Whether trading is disabled for the product
    auction_mode: bool  # Whether the product is in auction mode
    product_type: str  # Type of the product
    quote_currency_id: str  # ID of the quote currency
    base_currency_id: str  # ID of the base currency
    fcm_trading_session_details: Optional[FCMTradingSessionDetails]  # FCM trading session details (if any)
    mid_market_price: Optional[str]  # Mid-market price (if any)
    alias: Optional[str]  # Alias of the product (if any)
    alias_to: Optional[List[str]]  # List of aliases for the product
    base_display_symbol: str  # Display symbol of the base currency
    quote_display_symbol: str  # Display symbol of the quote currency
    view_only: bool  # Whether the product is view-only
    price_increment: str  # Price increment of the product
    future_product_details: Optional[Union[FutureProductDetails, dict]] = None  # Future product details (if any)
    display_name: str  # Display name of the product
    product_venue: str  # Venue of the product
    approximate_quote_24h_volume: str  # Approximate quote volume in the last 24 hours


# Model for Candles (OHLCV data)
class Candle(BaseModel):
    start: str  # Start time of the candle
    low: str  # Low price during the candle period
    high: str  # High price during the candle period
    open: str  # Opening price of the candle
    close: str  # Closing price of the candle
    volume: str  # Volume during the candle period


# Model for Market Trades
class MarketTrade(BaseModel):
    trade_id: str  # ID of the trade
    product_id: str  # ID of the product
    price: str  # Price at which the trade occurred
    size: str  # Size of the trade
    time: str  # Time at which the trade occurred
    side: str  # Side of the trade (buy/sell)
    bid: str  # Bid price at the time of the trade
    ask: str  # Ask price at the time of the trade
