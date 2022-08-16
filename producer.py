
import pika
import time
import random
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('13.214.190.7')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

messageID = 1
while(True):
    message = f"hello I want to broadcast this message: {messageID}"
    channel.basic_publish(exchange="pubsub", routing_key="", body=message)
    print(f"sent message: {message}")
    time.sleep(random.randint(1, 4))
    messageID+=1





