import pika
from redis import StrictRedis
from DB import rabbitmq
from time import strftime, localtime
from Consume import *

def callback(ch, method, properties, body):
    body = bytes.decode(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    produce2redis(body)
    dates = body.split(',')
    try:
        codingredis('a'+dates[1], 'p'+dates[4], strftime('%Y-%m-%d %H:%M:%S', localtime(float(dates[2]))))
    except:
        pass
    return body

def produce2redis(data):
    r = StrictRedis(connection_pool=REDIS.REDIS_pool)
    r.lpush(RABBITMQ.exchange, data)

def codingredis(id, port, data):
    r = StrictRedis(connection_pool=REDIS.REDIS_pool)
    r.lpush(id+':'+port, data)
    print((id+':'+port, data))


class rabbitmqchannel():
    def __init__(self):
        self.channel = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq['host'], port=int(rabbitmq['port']),
                                                                    credentials=pika.PlainCredentials(
                                                                        password=rabbitmq['password'],
                                                                        username=rabbitmq['user']))).channel()
    def getData4Rabbit(self):
        try:
            self.channel.basic_consume(queue, callback, False)
        except:
            from Consume import bind
            b = bind.bind()
            del b
            self.channel = pika.BlockingConnection(
                pika.ConnectionParameters(host=rabbitmq['host'], port=int(rabbitmq['port']),
                                          credentials=pika.PlainCredentials(
                                              password=rabbitmq['password'],
                                              username=rabbitmq['user']))).channel()
            self.channel.basic_consume(queue, callback, False)
        print(" [*] Waiting for messages. ")
        self.channel.start_consuming()  # 监听数据
