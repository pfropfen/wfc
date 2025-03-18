import json
from kafka import KafkaProducer



# KAFKA TESTER
print("create producer...")
producer = KafkaProducer(bootstrap_servers = ["192.168.1.33:9092"],value_serializer=lambda v: json.dumps(v).encode("utf-8"))



test = "HALLO TEST"

print("sending data: ", test)
producer.send("maptickets",test)
producer.flush()


print("finished..")