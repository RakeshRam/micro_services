import pika
import json

params = pika.URLParameters('amqps://flfjxgri:Vie8bBa_zH67JkSMqoPdmsZrvdEJqjew@lionfish.rmq.cloudamqp.com/flfjxgri')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='api_manager')

def callback(ch, method, properties, body):
    print('Received in api_manager')
    print(body)


channel.basic_consume(queue='api_manager', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()
channel.close()