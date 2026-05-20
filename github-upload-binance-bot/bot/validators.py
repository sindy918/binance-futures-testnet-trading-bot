import os
import logging

def validate_env():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    if not api_key or not api_secret:
        logging.error("API credentials are missing. Please create a .env file.")
        raise ValueError("API credentials are missing. Please create a .env file.")
    return api_key, api_secret

def validate_order_args(order_type, side, quantity, price):
    order_type = order_type.upper()
    side = side.upper()
    
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")
    
    if side not in ["BUY", "SELL"]:
        raise ValueError("Order side must be BUY or SELL.")
        
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
        
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price is required and must be greater than 0 for LIMIT orders.")
