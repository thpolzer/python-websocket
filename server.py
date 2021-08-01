from asyncio.tasks import sleep
import websockets
import asyncio
import random as rand
import json


PORT = 49153
print("Server listening on Port " + str(PORT))



async def echo(websocket, path):
    print("A client just connected")
    #async for message in websocket:
    #    print("Received message from client: " + message)
    #    await websocket.send("Pong: " + message)
    while True:
        number = rand.random()
        await websocket.send(str(number))
        await asyncio.sleep(2)

start_server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
websockets.close()