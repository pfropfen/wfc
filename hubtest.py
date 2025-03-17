import requests
import json
import uuid

# HUB TESTER


url = "http://localhost:5002/getMapChunkByChunkID/5d15b112-42b9-4569-8ad2-e2e146337afc"


result = requests.get(url)

print("result: ", result.content)
