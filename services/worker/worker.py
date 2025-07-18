import wave
import json
import pika
import requests
import uuid
from datetime import datetime


# WORKER SERVICE

# URLs
huburl = "http://wfchub:5002"
timekeeperurl = "http://wfctimekeeper:6002"
rabbithost = "wfcrabbit"

# RABBITMQ CONNECTION
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbithost, heartbeat=28800))
channel = connection.channel()
channel.queue_declare(queue='maptickets', durable=True)




def sendChunkTimes(mapID, chunkID, startTime, endTime, chunkDuration):
    print("Sending Times to Time Keeper...")
    result = requests.post(timekeeperurl+"/saveChunkTime", json = json.dumps({"mapID":mapID, "chunkID":chunkID, "startTime":startTime.isoformat(), "endTime":endTime.isoformat(), "chunkDuration":chunkDuration}))
    print("Done")
    print("")
    

def callback(ch, method, properties, body):
    print("[message received]")
    finished = False
    print("[request ticket]")
    chunk = requests.get(huburl+"/getMapChunkByChunkID/"+body.decode())
    print("[set map]")
    chunk = json.loads(chunk.content.decode())
    mapID = chunk[0]
    chunkID = chunk[1]
    mapdata = json.loads(chunk[5])

    startTime = datetime.now()
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
    
    endTime = datetime.now()
    # calculate chunkDuration
    chunkDuration = int((endTime - startTime).total_seconds()*1000)
    # send chunk times to timekeeper
    sendChunkTimes(mapID, chunkID, startTime, endTime, chunkDuration)
    try:
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except:
        print("Couldn't ack the request")
    
    
print("WORKER SERVICE")
print("--------------")
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="maptickets", on_message_callback=callback)
channel.start_consuming()
    
    
    
