import pika
import json

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_manager.settings")
django.setup()

from core.models import Character

params = pika.URLParameters('amqps://flfjxgri:Vie8bBa_zH67JkSMqoPdmsZrvdEJqjew@lionfish.rmq.cloudamqp.com/flfjxgri')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='api_manager')

def callback(ch, method, properties, body):
    print('Received in api_manager')
    id = json.loads(body)
    character = Character.objects.get(id=id)
    character.votes = character.votes + 1
    character.save()
    print('Character Vote Registered')


channel.basic_consume(queue='api_manager', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()
channel.close()