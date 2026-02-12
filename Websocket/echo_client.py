# echo_client.py

import asyncio
import websockets


async def run_client():
    # Address of the echo server
    uri = "ws://localhost:8765"

    # Open a persistent WebSocket connection
    async with websockets.connect(uri) as websocket:

        # Send a few messages
        for msg in ["hello", "websockets", "echo test"]:
            print("Sending:", msg)

            # Send message to server
            await websocket.send(msg)

            # Wait for the echoed response
            response = await websocket.recv()
            print("Received:", response)


# Start the client
asyncio.run(run_client())
