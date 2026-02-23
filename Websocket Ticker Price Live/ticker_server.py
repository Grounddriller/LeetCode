import json                                   # Used to convert Python dict <-> JSON text
from fastapi import FastAPI, WebSocket        # FastAPI tools to create WebSocket server
import websockets                             # Allows our SERVER to connect to OKX via WebSocket

# Create FastAPI application instance
app = FastAPI()

# Public OKX WebSocket endpoint (no API key required)
OKX_WS = "wss://ws.okx.com:8443/ws/v5/public"


# Define a WebSocket route.
# Example client connection:
# ws://127.0.0.1:8000/ws/btcusdt
@app.websocket("/ws/{symbol}")
async def ws_proxy(client_ws: WebSocket, symbol: str):

    # Accept the WebSocket connection from YOUR client
    await client_ws.accept()

    # Convert symbol format to match OKX requirements.
    # OKX uses format like BTC-USDT
    symbol = symbol.upper()                   # btcusdt -> BTCUSDT

    # Convert BTCUSDT -> BTC-USDT
    if symbol.endswith("USDT") and "-" not in symbol:
        symbol = f"{symbol[:-4]}-USDT"

    # Now your server connects TO OKX as a WebSocket client
    async with websockets.connect(OKX_WS) as okx_ws:

        # Send a subscription message to OKX
        # This tells OKX:
        # "Send me live ticker updates for this instrument"
        await okx_ws.send(json.dumps({
            "op": "subscribe",
            "args": [{
                "channel": "tickers",         # We want live ticker data
                "instId": symbol              # Example: BTC-USDT
            }]
        }))

        # Infinite loop: continuously receive updates from OKX
        while True:

            # Wait for next WebSocket message from OKX
            raw_msg = await okx_ws.recv()

            # Convert JSON text into Python dictionary
            data = json.loads(raw_msg)

            # OKX first sends subscription confirmation.
            # Skip anything that doesn't contain ticker data.
            if "data" not in data:
                continue

            # Extract first ticker object
            ticker = data["data"][0]

            # Build simplified JSON to send to YOUR client
            simplified = {
                "symbol": ticker["instId"],        # Trading pair (BTC-USDT)
                "price": ticker["last"],           # Last traded price per 1 BTC
                "trade_time_ms": int(ticker["ts"]) # Timestamp in milliseconds
            }

            # Send simplified ticker to connected client
            await client_ws.send_text(json.dumps(simplified))

# Run the server: python -m uvicorn ticker_server:app