import wave
import json
import pika
import requests
import uuid



huburl = "http://localhost:5002"
rabbithost = "192.168.1.93"

# RABBITMQ CONNECTION
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbithost))
channel = connection.channel()
channel.queue_declare(queue='maptickets', durable=True)


def callback(ch, method, properties, body):
    print("[message received]")
    finished = False
    print("[request ticket]")
    print("BODY DECODED: ", body.decode())
    chunk = requests.get(huburl+"/getMapChunkByChunkID/"+body.decode())
    print("[set map]")
    chunk = json.loads(chunk.content.decode())
    print("CHUNK CONTENT: ", chunk)
    print("CHUNK5 CONTENT: ", chunk[5])
    mapdata = json.loads(chunk[5])
    
    wave.map = mapdata
    print("[set entropy tolerance]")
    wave.entropyTolerance = chunk[4]
    print("[set number of tiles]")
    wave.numberOfTiles = (len(mapdata[0]),len(mapdata))
    print("[start algorythm]")
    while not finished:
        if (not finished):
            finished = wave.algorithmStep()
    print("[finished]")
    
    result = requests.post(huburl+"/updateChunkByID", json = json.dumps({"chunkID":body.decode(),"content":wave.map}))
    print("Result: ", result)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
print("WORKER SERVICE")
print("--------------")
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="maptickets", on_message_callback=callback)
channel.start_consuming()
    
    
    