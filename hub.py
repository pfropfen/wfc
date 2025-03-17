import mysql.connector
import uuid
import json
from flask import Flask, request



# GLOBAL VARIABLES
database = None
dbCursor = None
sqlCommand = "INSERT INTO mapchunks (mapID, chunkID, locationX, locationY, content) VALUES (%s, %s, %s, %s, %s);"

# HUB SERVICE

app = Flask(__name__)

@app.route("/")
def showHome():
    return "HUB SERVICE FOR SAVING MAPCHUNKS"


@app.route("/saveChunk", methods=["POST"])
def saveChunk():
    data = json.loads(request.json)
    valuesToInsert = (data["mapID"], data["chunkID"], data["locX"], data["locY"], data["content"])
    dbCursor.execute(sqlCommand, valuesToInsert)
    database.commit()
    print(dbCursor.rowcount)
    print("saved chunk in db")
    return "done"
    
    


@app.route("/saveChunks", methods=["POST"])
def saveChunks():
    data = json.loads(request.json)
    valuesToInsert = []
    for chunk in data:
        valuesToInsert.append((chunk["mapID"], chunk["chunkID"], chunk["locX"], chunk["locY"], json.dumps(chunk["content"])))
    dbCursor.executemany(sqlCommand, valuesToInsert)
    database.commit()
    print(dbCursor.rowcount)
    print("saved set of chunks in db")
    return "done"



database = mysql.connector.connect(host="192.168.1.87", database="maps", user="root", password="root")
dbCursor = database.cursor()



#result = dbCursor.fetchall()
#print("Result: ", result)


