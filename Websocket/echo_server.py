# echo_server.py

import asyncio              # Handles async execution (non-blocking)
import websockets           # WebSocket protocol library


# This function runs for EACH connected client
async def echo(websocket):
    print("Client connected")

    try:
        # This loop waits for messages from the client forever
        async for message in websocket:

            # Print what the server received
            print("Received:", message)

            # Send the SAME message back to the client (echo)
            await websocket.send(message)

            print("Echoed back:", message)

    # This happens when the client disconnects
    except websockets.ConnectionClosed:
        print("Client disconnected")


# Main function to start the server
async def main():
    # Start the WebSocket server
    # - echo = function that handles connections
    # - localhost = local machine only
    # - 8765 = port number
    server = await websockets.serve(echo, "localhost", 8765)

    print("Echo server running on ws://localhost:8765")

    # Keep the server alive forever
    await server.wait_closed()


# Start the asyncio event loop
asyncio.run(main())
