import asyncio
import websockets
import ssl

host = ""
port = 8765
clients = []

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    "/etc/letsencrypt/live/cits3200api.zachmanson.com/fullchain.pem",
    "/etc/letsencrypt/live/cits3200api.zachmanson.com/privkey.pem"
)

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
    async with websockets.serve(handler, host, port, ssl=ssl_context) as server:
        print(f"Websocket open on {host}:{port}")
        await asyncio.Future()  # run forever
        

if __name__ == "__main__":
    asyncio.run(main())