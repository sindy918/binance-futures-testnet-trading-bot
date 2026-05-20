import logging
from bot.client import BinanceClient

def place_order(client: BinanceClient, symbol, side, order_type, quantity, price=None, time_in_force="GTC"):
    endpoint = "/fapi/v1/order"
    
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity
    }
    
    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = time_in_force

    logging.info(f"Sending {order_type.upper()} order for {symbol.upper()} | Side: {side.upper()} | Qty: {quantity} | Price: {price}")
    
    response = client.send_signed_request("POST", endpoint, params)
    
    if response.status_code == 200:
        logging.info("Order successfully placed!")
        logging.info(f"Response: {response.json()}")
        return response.json()
    else:
        logging.error(f"Error placing order: HTTP {response.status_code}")
        logging.error(f"Response: {response.text}")
        return None
