import mysql.connector
import uuid
import json
from flask import Flask, request
import pika




# GLOBAL VARIABLES
dbhost = "192.168.1.93"
sqlInsert = "INSERT INTO mapchunks (mapID, chunkID, locationX, locationY, entropyTolerance, content, computed) VALUES (%s, %s, %s, %s, %s, %s, %s);"
sqlGetByTicketID = "SELECT * FROM mapchunks WHERE chunkID = %s;"
sqlUpdateChunk = "UPDATE mapchunks SET content = %s, computed = 1 WHERE chunkID = %s;"
sqlMapByID = "SELECT locationX,locationY,content FROM mapchunks WHERE mapID = %s;"

# RABBITMQ CONNECTION
connection = pika.BlockingConnection(pika.ConnectionParameters(host=dbhost))
channel = connection.channel()
channel.queue_declare(queue='maptickets', durable=True)





# HUB SERVICE

app = Flask(__name__)

@app.route("/")
def showHome():
    return "HUB SERVICE FOR SAVING MAPCHUNKS"


@app.route("/saveChunk", methods=["POST"])
def saveChunk():
    database = mysql.connector.connect(host=dbhost, database="maps", user="root", password="root")
    dbCursor = database.cursor()
    data = json.loads(request.json)
    valuesToInsert = (data["mapID"], data["chunkID"], data["locX"], data["locY"], data["entropyTolerance"], data["content"], False)
    dbCursor.execute(sqlInsert, valuesToInsert)
    database.commit()
    print(dbCursor.rowcount)
    print("saved chunk in db")
    database.disconnect()
    return "done"
    
@app.route("/updateChunkByID", methods=["POST"])
def updateChunk():
    database = mysql.connector.connect(host=dbhost, database="maps", user="root", password="root")
    dbCursor = database.cursor()
    data = json.loads(request.json)
    valuesToInsert = (json.dumps(data["content"]), data["chunkID"])
    dbCursor.execute(sqlUpdateChunk, valuesToInsert)
    database.commit()
    database.disconnect()
    return "done"


@app.route("/saveChunks", methods=["POST"])
def saveChunks():
    # DB CONNECTION
    database = mysql.connector.connect(host=dbhost, database="maps", user="root", password="root")
    dbCursor = database.cursor()
    data = json.loads(request.json)
    valuesToInsert = []
    for chunk in data:
        valuesToInsert.append((chunk["mapID"], chunk["chunkID"], chunk["locX"], chunk["locY"], chunk["entropyTolerance"], json.dumps(chunk["content"]), False))
        message = chunk["chunkID"]
        channel.basic_publish(exchange='', routing_key='maptickets', body=message, properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))
    dbCursor.executemany(sqlInsert, valuesToInsert)
    database.commit()
    database.disconnect()
    print(dbCursor.rowcount)
    print("saved set of chunks in db")
    return "done"

@app.route("/getMapChunkByChunkID/<uuid:ID>", methods=["GET"])
def getMapChunkByChunkID(ID):
    database = mysql.connector.connect(host=dbhost, database="maps", user="root", password="root")
    dbCursor = database.cursor()
    dbCursor.execute(sqlGetByTicketID, (str(ID),))
    result = dbCursor.fetchone()
    print("RESULT: ", result)
    database.disconnect()
    return json.dumps(result)

@app.route("/getMapByID/<uuid:ID>", methods=["GET"])
def getMapByID(ID):
    database = mysql.connector.connect(host=dbhost, database="maps", user="root", password="root")
    dbCursor = database.cursor()
    dbCursor.execute(sqlMapByID, (str(ID),))
    result = dbCursor.fetchall()
    print("len(result): ", len(result))
    content = []
    for chunk in result:
        content.append(json.loads(chunk[2]))
    sizeX = len(content[0][0])
    sizeY = len(content[0])
    print("sizeX: ", sizeX)
    print("sizeY: ", sizeY)
    
    maxLocX = -1
    maxLocY = -1
    for chunk in result:
        if (chunk[0] > maxLocX):
            maxLocX = chunk[0]
        if (chunk[1] > maxLocY):
            maxLocY = chunk[1]
    fullMap = []
    for y in range (0,(maxLocY+1)*sizeY):
        temp = []
        for x in range (0,(maxLocX+1)*sizeX):
            temp.append(0)
        fullMap.append(temp)
    print("fullmap: ", fullMap)
    for i,chunk in enumerate(result):
        for y in range (0,sizeY):
            for x in range (0, sizeX):
                fullMap[chunk[1]*sizeY+y][chunk[0]*sizeX+x] = content[i][y][x]
    print("FULLMAP: ", fullMap)
    return fullMap




