import pika
from DB import rabbitmq
pika.ConnectionParameters(host=rabbitmq['host'], port=int(rabbitmq['port']), heartbeat=0)
exchange = rabbitmq['exchange']
queue = rabbitmq['queue']