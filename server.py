from asyncio.tasks import sleep
import websockets
import asyncio
import random as rand
import json

fx = {"EUR":1+rand.random(), "GBP":1+rand.random()}
al = {"EUR":1-rand.random(), "GBP":1-rand.random()}
metadata = {"size":826401, "date":"2021-08-02"}
data = {"root":[{"fx":fx,"al":al},{"metadata": metadata}]}
data_string = json.dumps(data)


PORT = 49153
print("Server listening on Port " + str(PORT))



async def echo(websocket, path):
    print("A client just connected")
    #async for message in websocket:
    #    print("Received message from client: " + message)
    #    await websocket.send("Pong: " + message)
    while True:
        data["root"][0]["fx"] = {"EUR":1+rand.random(), "GBP":1+rand.random()}
        data["root"][0]["al"] = {"EUR":1-rand.random(), "GBP":1-rand.random()}
        data_string = json.dumps(data)
        #number = rand.random()
        await websocket.send(str(data_string))
        await asyncio.sleep(2)

start_server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
websockets.close()