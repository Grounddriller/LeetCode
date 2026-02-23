import asyncio
import json
import time
import websockets

# Connect to YOUR FastAPI WebSocket server
# Tracking the ticker price of BTC-USDT aka the live value for 1 Bitcoin in USDT now
SERVER_URL = "ws://127.0.0.1:8000/ws/btcusdt"


async def main():
    # Open WebSocket connection to your local server
    async with websockets.connect(SERVER_URL) as ws:

        last_print_second = None  # Tracks the last second we printed

        while True:
            # Wait for next message from server
            msg = await ws.recv()

            # Convert JSON string into Python dictionary
            data = json.loads(msg)

            # Extract values
            symbol = data["symbol"]
            price = float(data["price"])
            trade_time_ms = data["trade_time_ms"]

            # Convert milliseconds -> whole second
            trade_second = int(trade_time_ms / 1000)

            # Only print once per second
            if trade_second != last_print_second:
                last_print_second = trade_second

                readable_time = time.strftime(
                    "%H:%M:%S",
                    time.localtime(trade_second)
                )

                print(f"[{readable_time}] {symbol} {price}")


# Start async event loop
asyncio.run(main())

# Run the client: python ticker_client.py