import pika
import json

params = pika.URLParameters('amqps://flfjxgri:Vie8bBa_zH67JkSMqoPdmsZrvdEJqjew@lionfish.rmq.cloudamqp.com/flfjxgri')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='api_manager', body=json.dumps(body), properties=properties)