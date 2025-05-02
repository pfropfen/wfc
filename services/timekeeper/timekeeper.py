import mysql.connector
import uuid
import json
import requests
from flask import Flask, request
from datetime import datetime


# GLOBAL VARIABLES
timedbhost = "timedb"
dbhost = "wfcdb"
sqlMapInsert = "INSERT INTO mapTimes (mapID, mapSize, chunkCount, numberOfWorkers, startTime, endTime, totalDuration) VALUES (%s, %s, %s, %s, %s, %s, %s);"
sqlChunkInsert = "INSERT INTO chunkTimes (mapID, chunkID, startTime, endTime, chunkDuration) VALUES (%s, %s, %s, %s, %s);"
sqlGetMapStartTime = "SELECT startTime FROM mapTimes WHERE mapID = %s"
sqlUpdate = "UPDATE mapTimes SET endTime = %s, totalDuration = %s WHERE mapID = %s" 
sqlCheckMapByID = "SELECT computed FROM mapchunks WHERE mapID = %s;"
sqlGetChunkEndTimes = "SELECT endTime FROM chunkTimes WHERE mapID = %s;"


app = Flask(__name__)

@app.route("/")
def showHome():
    return "TIME KEEPER SERVICE"
  

@app.route("/isMapComplete/<uuid:ID>", methods=["GET"])
def isMapComplete(ID):
    database = mysql.connector.connect(host=dbhost, database="maps", user="root", password="root")
    dbCursor = database.cursor()
    
    dbCursor.execute(sqlCheckMapByID, (str(ID),))
    result = dbCursor.fetchall()
    print("RESULT: ", result)
    database.disconnect()
    
    completed = True
    for mapchunkCompleted in result:
        if not mapchunkCompleted:
            completed = False
    return completed

    
    
@app.route("/saveMapTime", methods=["POST"])
def saveMapTime():
    database = mysql.connector.connect(host=timedbhost, database="times", user="root", password="root")
    dbCursor = database.cursor()
    data = json.loads(request.json)
    startTime = datetime.fromisoformat(data["startTime"])
    valuesToInsert = (data["mapID"], data["mapSize"], data["chunkCount"], data["numberOfWorkers"], startTime, data["endTime"], data["totalDuration"])
    dbCursor.execute(sqlMapInsert, valuesToInsert)
    database.commit()
    print(dbCursor.rowcount)
    print("saved maptime in db")
    database.disconnect()
    return "done"
    
    
def updateMapTime(mapID, endTime):
    database = mysql.connector.connect(host=timedbhost, database="times", user="root", password="root")
    dbCursor = database.cursor()
    data = json.loads(request.json)
    
    valuesToFetch = (mapID,)
    dbCursor.execute(sqlGetMapStartTime, valuesToFetch)
    row = dbCursor.fetchone()
    #if row is not None:
    totalDuration = int((endTime-row[0]).total_seconds()*1000)
    valuesToUpdate = (endTime, totalDuration, mapID)
    dbCursor.execute(sqlUpdate, valuesToUpdate)
    database.commit()
    print(dbCursor.rowcount)
    print("maptime updated")
    #else:
        #print("row not found")
    database.disconnect()
    return "done"
    
@app.route("/saveChunkTime", methods=["POST"])
def saveChunkTime():
    database = mysql.connector.connect(host=timedbhost, database="times", user="root", password="root")
    dbCursor = database.cursor()
    data = json.loads(request.json)
    valuesToInsert = (data["mapID"], data["chunkID"], datetime.fromisoformat(data["startTime"]), datetime.fromisoformat(data["endTime"]), data["chunkDuration"])
    dbCursor.execute(sqlChunkInsert, valuesToInsert)
    database.commit()
    print(dbCursor.rowcount)
    print("saved chunktime in db")
    database.disconnect()
    
    if isMapComplete(data["mapID"]):
        database = mysql.connector.connect(host=timedbhost, database="times", user="root", password="root")
        dbCursor = database.cursor()
        dbCursor.execute(sqlGetChunkEndTimes, (data["mapID"],))
        resultChunkEndTimes = dbCursor.fetchall()
        print("EndTimes: ", resultChunkEndTimes)
        print("")

        lastChunkEndTime = datetime.min
        for endTime in resultChunkEndTimes:
            if endTime[0] > lastChunkEndTime:
                lastChunkEndTime = endTime[0]
        
        database.disconnect()
        updateMapTime(data["mapID"], lastChunkEndTime)
        
    return "done"