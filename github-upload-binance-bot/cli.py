import os
import argparse
import sys
from dotenv import load_dotenv
from bot.logging_config import setup_logging
from bot.validators import validate_env, validate_order_args
from bot.client import BinanceClient
from bot.orders import place_order

# Load environment variables
load_dotenv()

# Setup logging
setup_logging()

def main():
    try:
        # Validate environment variables
        api_key, api_secret = validate_env()
    except ValueError:
        sys.exit(1)

    base_url = os.getenv("BINANCE_BASE_URL", "https://testnet.binancefuture.com")

    # Command line argument parser
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True, help="Order type (MARKET or LIMIT)")
    parser.add_argument("--symbol", default="BTCUSDT", help="Trading pair (default: BTCUSDT)")
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True, help="Order side (BUY or SELL)")
    parser.add_argument("--qty", type=float, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price for LIMIT orders")

    args = parser.parse_args()

    try:
        # Validate order inputs
        validate_order_args(args.type, args.side, args.qty, args.price)
    except ValueError as e:
        print(f"Validation Error: {str(e)}")
        sys.exit(1)

    # Initialize client
    client = BinanceClient(api_key, api_secret, base_url)

    # Place order
    place_order(
        client=client,
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.qty,
        price=args.price
    )

if __name__ == "__main__":
    main()
