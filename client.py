import websockets
import asyncio
import json

# connects to the server and handles its response
async def listen():
    url = "ws://localhost:49153"

    async with websockets.connect(url) as ws:
        await ws.send("Hello Server")
        while True:
            msg = await ws.recv()
            print(msg)
            await asyncio.sleep(5)
            data = json.loads(msg)
            print(data["root"][0]["fx"])

asyncio.get_event_loop().run_until_complete(listen())