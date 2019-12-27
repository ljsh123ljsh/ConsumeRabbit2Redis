
from Consume import *
from DB import rabbitmq
import pika

class bind:
    def __init__(self):
        channel = RABBITMQ = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq['host'], port=int(rabbitmq['port']), credentials=pika.PlainCredentials(password=rabbitmq['password'], username=rabbitmq['user']))).channel()
        channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)
        binding_key = 'data.msm'
        channel.queue_declare(queue=queue, durable=True)
        channel.queue_bind(exchange=exchange, queue=queue, routing_key=binding_key)
    def __del__(self):
        pass