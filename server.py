import asyncio
import websockets

port = 8765
clients = []


async def handler(websocket):
    clients.append(websocket)
    print(f"Client connected: {websocket.remote_address}")
    print(f"{len(clients)} connections")
    async for message in websocket:
        # websockets.broadcast(clients, message)
        for i, client in enumerate(clients):
            try:
                await client.send(message)
            except websockets.exceptions.ConnectionClosed:
                del clients[i]
                print(f"Client disconnected: {websocket.remote_address}")
                print(f"{len(clients)} connections")

async def main():
    async with websockets.unix_serve(handler, "localhost", port) as server:
        print(f"Websocket open on port {port}")
        await asyncio.Future()  # run forever
        

if __name__ == "__main__":
    asyncio.run(main())