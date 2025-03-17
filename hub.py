import mysql.connector
import uuid
import json
from flask import Flask, request
from kafka import KafkaProducer



# GLOBAL VARIABLES
database = None
dbCursor = None
sqlInsert = "INSERT INTO mapchunks (mapID, chunkID, locationX, locationY, entropyTolerance, content, computed) VALUES (%s, %s, %s, %s, %s, %s, %s);"
sqlGetByTicketID = "SELECT * FROM mapchunks WHERE chunkID = %s;"
sqlUpdateChunk = "UPDATE mapchunks SET content = %s, computed = 1 WHERE chunkID = %s;"

# KAFKA PRODUCER FOR MAPTICKETS
producer = KafkaProducer(bootstrap_servers = ["192.168.1.87:9092"],value_serializer=lambda v: json.dumps(v).encode("utf-8"))

# HUB SERVICE

app = Flask(__name__)

@app.route("/")
def showHome():
    return "HUB SERVICE FOR SAVING MAPCHUNKS"


@app.route("/saveChunk", methods=["POST"])
def saveChunk():
    data = json.loads(request.json)
    valuesToInsert = (data["mapID"], data["chunkID"], data["locX"], data["locY"], data["entropyTolerance"], data["content"], False)
    dbCursor.execute(sqlInsert, valuesToInsert)
    database.commit()
    print(dbCursor.rowcount)
    print("saved chunk in db")
    return "done"
    
@app.route("/updateChunkByID", methods=["POST"])
def updateChunk():
    data = json.loads(request.json)
    valuesToInsert = (data["content"], data["chunkID"])
    dbCursor.execute(sqlUpdateChunk, valuesToInsert)
    database.commit()
    return "done"


@app.route("/saveChunks", methods=["POST"])
def saveChunks():
    data = json.loads(request.json)
    valuesToInsert = []
    for chunk in data:
        valuesToInsert.append((chunk["mapID"], chunk["chunkID"], chunk["locX"], chunk["locY"], data["entropyTolerance"], json.dumps(chunk["content"]), False))
        # CREATE MAPTICKET
        producer.send("maptickets", chunk["chunkID"])
        producer.flush()
    dbCursor.executemany(sqlInsert, valuesToInsert)
    database.commit()
    print(dbCursor.rowcount)
    print("saved set of chunks in db")
    return "done"

@app.route("/getMapChunkByChunkID/<uuid:ID>", methods=["GET"])
def getMapChunkByChunkID(ID):
    dbCursor.execute(sqlGetByTicketID, (str(ID),))
    result = dbCursor.fetchone()
    print("RESULT: ", result)
    return json.dumps(result)


database = mysql.connector.connect(host="192.168.1.87", database="maps", user="root", password="root")
dbCursor = database.cursor()



#result = dbCursor.fetchall()
#print("Result: ", result)


