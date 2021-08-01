import websockets
import asyncio

# connects to the server and handles its response
async def listen():
    url = "ws://localhost:49153"

    async with websockets.connect(url) as ws:
        await ws.send("Hello Server")
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())
print("Scheisse")