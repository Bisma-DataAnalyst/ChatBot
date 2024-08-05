import asyncio
import websockets

async def handle_websocket(websocket, path):
    print("Client connected")
    try:
        # Receive messages from the client indefinitely
        async for message in websocket:
            print(f"Received message: {message}")
            # Echo the received message back to the client
            await websocket.send(f"You sent: {message}")
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected")

async def start_server():
    # Create a WebSocket server listening on localhost and port 8765
    async with websockets.serve(handle_websocket, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        # Keep the server running indefinitely
        await asyncio.Future()

# Run the WebSocket server
asyncio.run(start_server())
asyncio.run(start_server())