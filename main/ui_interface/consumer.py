import pika
import json

from main import app
from db import db, Character

params = pika.URLParameters('amqps://flfjxgri:Vie8bBa_zH67JkSMqoPdmsZrvdEJqjew@lionfish.rmq.cloudamqp.com/flfjxgri')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'character_created':
        with app.app_context():
            character = Character(id=data['id'], name=data['name'], origin=data['origin'])
            db.session.add(character)
            db.session.commit()
        print('Character Created')

    elif properties.content_type == 'character_updated':
        with app.app_context():
            character = Character.query.get(data['id'])
            character.name = data['name']
            character.creator = data['creator']['name']
            character.origin = data['origin']   
            db.session.commit()
        print('Character Updated')

    elif properties.content_type == 'character_deleted':
        with app.app_context():
            character = Character.query.get(data)
            db.session.delete(character)
            db.session.commit()
        print('Character Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()
channel.close()