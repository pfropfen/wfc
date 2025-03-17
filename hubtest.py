import requests
import json
import uuid

# HUB TESTER


url = "http://localhost:5000/saveChunks"

content = json.dumps(["hure", "sohn"])

data1 = {"mapID":str(uuid.uuid4()),"chunkID":str(uuid.uuid4()), "locX":1,"locY":2,"content":content}
data2 = {"mapID":str(uuid.uuid4()),"chunkID":str(uuid.uuid4()), "locX":3,"locY":4,"content":content}
data3 = {"mapID":str(uuid.uuid4()),"chunkID":str(uuid.uuid4()), "locX":4,"locY":5,"content":content}

data = [data1,data2,data3]

obj = json.dumps(data)
result = requests.post(url, json=obj)

print("result: ", result)