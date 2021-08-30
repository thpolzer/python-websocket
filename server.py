from asyncio.tasks import sleep
import websockets
import asyncio
import random as rand
import json
import datetime

fx = {"EUR":1+rand.random(), "GBP":1+rand.random()}
al = {"EUR":1-rand.random(), "GBP":1-rand.random()}
metadata = {"size":826401, "timestamp":str(datetime.datetime.now())}
data = {"root":[{"fx":fx,"al":al},{"metadata": metadata}]}
data_string = json.dumps(data)


PORT = 49153
print("Server listening on Port " + str(PORT))



async def echo(websocket, path):
    print("client connected")
    while True:
        data["root"][0]["fx"] = {"EUR":1+rand.random(), "GBP":1+rand.random()}
        data["root"][0]["al"] = {"EUR":1-rand.random(), "GBP":1-rand.random()}
        data["root"][1]["metadata"]["timestamp"] = str(datetime.datetime.now())
        data_string = json.dumps(data)
        print(data)
        await websocket.send(str(data_string))
        await asyncio.sleep(0.1)

start_server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
websockets.close()