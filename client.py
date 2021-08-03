import websockets
import asyncio
import json
from kafka import KafkaProducer
import datetime

# setting KafkaProducer
producer = KafkaProducer(bootstrap_servers=['hadoopserver:9092'], \
    value_serializer=lambda m: json.dumps(m).encode('ascii'))


# connects to the server and handles its response
async def listen():
    url = "ws://localhost:49153"
    now = datetime.datetime.now()
    diff = datetime.timedelta(seconds=5)
    async with websockets.connect(url) as ws:
        await ws.send("Hello Server")
        while True:
            msg = await ws.recv()

            # send data to Kafka in 5 sec time interval
            if  datetime.datetime.now() >= (now + diff):
                print(msg)
                print (datetime.datetime.now())

                # extract data from json into python dictionary
                data = json.loads(msg)

                # filter data
                fxdata = {"fx":{'EUR': data["root"][0]["fx"]["EUR"], \
                    'GBP':data["root"][0]["fx"]["GBP"],\
                        'timestamp':data["root"][1]["metadata"]["timestamp"]}}
                aludata = {"alu":{'EUR': data["root"][0]["al"]["EUR"], \
                    'GBP':data["root"][0]["al"]["GBP"],\
                        'timestamp':data["root"][1]["metadata"]["timestamp"]}}
                
                # send data to Kafka topic 
                producer.send('fx-rates', fxdata).get()

                # update 5 sec time interval
                now = datetime.datetime.now()
            

asyncio.get_event_loop().run_until_complete(listen())