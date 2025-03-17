import json
from kafka import KafkaConsumer




# KAFKA CONSUMER


print("create consumer..")
consumer = KafkaConsumer(bootstrap_servers = ["192.168.1.87:9092"], value_deserializer=json.loads)

print("subscribe topic..")
consumer.subscribe("maptickets")


print("start listening..")
while True:
    data = next(consumer)
    print("received: ", data)
