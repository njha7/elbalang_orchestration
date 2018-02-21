import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
for x in range(1,100):
  channel.basic_publish(exchange='', routing_key='hello', body='%d' % x)
connection.close()