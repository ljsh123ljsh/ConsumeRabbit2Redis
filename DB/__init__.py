from configparser import ConfigParser
from os import path
conf_path = path.join(path.abspath(path.dirname(path.dirname(__file__))), 'conf.ini')
cf = ConfigParser()
try:
    cf.read(conf_path, encoding='ANSI')
except:
    cf.read(conf_path)

rabbitmq = {
    'host': cf.get('rabbitmq', 'host'),
    'port': cf.get('rabbitmq', 'port'),
    'user': cf.get('rabbitmq', 'user'),
    'password': cf.get('rabbitmq', 'password'),
    'exchange': cf.get('rabbitmq', 'exchange'),
    'queue': cf.get('rabbitmq', 'queue')
}

redis = {
    'host': cf.get('redis', 'host'),
    'port': cf.get('redis', 'port'),
    'password': cf.get('redis', 'password'),
    'db': cf.get('redis', 'db')
}
