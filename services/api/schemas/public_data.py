from pydantic import BaseModel
from typing import List, Optional, Dict

class ServerTime(BaseModel):
    iso: str
    epochSeconds: str
    epochMillis: str

class ProductBookEntry(BaseModel):
    price: str
    size: str

class ProductBook(BaseModel):
    product_id: str
    bids: List[ProductBookEntry]
    asks: List[ProductBookEntry]
    time: str

class FCMTradingSessionDetails(BaseModel):
    is_session_open: Optional[bool]
    open_time: Optional[str]
    close_time: Optional[str]

class PerpetualDetails(BaseModel):
    open_interest: Optional[str]
    funding_rate: Optional[str]
    funding_time: Optional[str]

class FutureProductDetails(BaseModel):
    venue: Optional[str]
    contract_code: Optional[str]
    contract_expiry: Optional[str]
    contract_size: Optional[str]
    contract_root_unit: Optional[str]
    group_description: Optional[str]
    contract_expiry_timezone: Optional[str]
    group_short_description: Optional[str]
    risk_managed_by: Optional[str]
    contract_expiry_type: Optional[str]
    perpetual_details: Optional[PerpetualDetails]
    contract_display_name: Optional[str]

class Product(BaseModel):
    product_id: str
    price: str
    price_percentage_change_24h: str
    volume_24h: str
    volume_percentage_change_24h: str
    base_increment: str
    quote_increment: str
    quote_min_size: str
    quote_max_size: str
    base_min_size: str
    base_max_size: str
    base_name: str
    quote_name: str
    watched: bool
    is_disabled: bool
    new: bool
    status: str
    cancel_only: bool
    limit_only: bool
    post_only: bool
    trading_disabled: bool
    auction_mode: bool
    product_type: str
    quote_currency_id: str
    base_currency_id: str
    fcm_trading_session_details: Optional[FCMTradingSessionDetails]
    mid_market_price: Optional[str]
    alias: str
    alias_to: List[str]
    base_display_symbol: str
    quote_display_symbol: str
    view_only: bool
    price_increment: str
    future_product_details: Optional[FutureProductDetails]
    display_name: str
    product_venue: str
    approximate_quote_24h_volume: str

class Candle(BaseModel):
    start: str
    low: str
    high: str
    open: str
    close: str
    volume: str

class MarketTrade(BaseModel):
    trade_id: str
    product_id: str
    price: str
    size: str
    time: str
    side: str
    bid: str
    ask: str
