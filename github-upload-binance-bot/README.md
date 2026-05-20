# Binance Futures Testnet Trading Bot

A simple Python CLI tool to interact with the Binance Futures Testnet API and execute MARKET and LIMIT orders safely.

## Project Structure
```text
trading_bot/
  bot/
    __init__.py
    client.py
    orders.py
    validators.py
    logging_config.py
  cli.py
  README.md
  requirements.txt
  .env.example
  .gitignore
  logs/trading_bot.log
```

## Setup Instructions

1. Clone the repository.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the `.env.example` file to `.env` and fill in your Binance Testnet API credentials:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and modify the values:
   ```env
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_API_SECRET=your_testnet_api_secret_here
   BINANCE_BASE_URL=https://testnet.binancefuture.com
   ```

## Usage

All commands are run using `cli.py` with custom arguments.

### 1. Place a MARKET BUY Order
To place a MARKET order to BUY `0.001` BTC:
```bash
python cli.py --type MARKET --symbol BTCUSDT --side BUY --qty 0.001
```

### 2. Place a LIMIT BUY Order
To place a LIMIT order to BUY `0.002` BTC at a price of `30000.0`:
*(Note: Binance Futures Testnet requires a minimum order notional of 50 USDT, meaning Price × Quantity must be at least 50 USDT.)*
```bash
python cli.py --type LIMIT --symbol BTCUSDT --side BUY --qty 0.002 --price 30000.0
```

### 3. Check Logs
All request logs are securely stored in `logs/trading_bot.log`.
```bash
tail -n 20 logs/trading_bot.log  # On Windows: Get-Content logs/trading_bot.log -Tail 20
```
