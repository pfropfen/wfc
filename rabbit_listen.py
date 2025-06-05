import pika

def callback(ch, method, properties, body):
    print("Message:", body)
    # ch.basic_ack(delivery_tag=method.delivery_tag)  # Don't call this if you want to requeue

connection = pika.BlockingConnection(pika.ConnectionParameters(host='139.6.65.27', port=31673))
channel = connection.channel()

channel.basic_consume(queue='your_queue_name', on_message_callback=callback, auto_ack=False)
channel.start_consuming()
