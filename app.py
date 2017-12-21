# example_publisher.py
import pika
import os
import logging
import sys

msg = sys.argv[1]
print(msg)
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)

connection = pika.BlockingConnection(
    pika.ConnectionParameters('127.0.0.1'))  # Connect to rabbitMq
channel = connection.channel()  # start a channel
channel.queue_declare(queue='sampleQueue')  # Declare a queue
# send a message

channel.basic_publish(
    exchange='', routing_key='sampleQueue', body=msg)
print("[x] Message sent to consumer")
connection.close()
