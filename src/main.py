import os
import pika

mq_host = os.getenv('MQ_HOST', 'localhost')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host))
channel = connection.channel()

channel.exchange_declare(exchange='shadow',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='shadow',
                   queue=queue_name,
                   routing_key='#')

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
