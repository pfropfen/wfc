import wave
import json
from kafka import KafkaConsumer
import requests
import uuid



huburl = "http://localhost:5002"



# KAFKA CONSUMER
print("create consumer..")
consumer = KafkaConsumer(bootstrap_servers = ["192.168.1.87:9092"], value_deserializer=json.loads)
print("subscribe topic..")
consumer.subscribe("maptickets")
print("start listening..")

while True:
    finished = False
    data = next(consumer)
    print("received: ", data)
    chunk = requests.get(huburl+"/getMapChunkByChunkID/"+data.value)
    wave.map = chunk[5]
    wave.entropyTolerance = chunk[4]
    wave.numberOfTiles = (len(chunk[5][0]),len(chunk[5]))
    highestEntropy = 9
    while not finished:
        if (not finished):
            finished = wave.algorithmStep(highestEntropy)
    result = requests.post(huburl+"/updateChunkByID", json.dumps({"chunkID":data.value,"content":wave.map}))
    print("Result: ", result)
    
    
    