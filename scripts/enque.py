import pika
import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--root', help='Root directory of files to enque')
parser.add_argument('--regex', help='Regex of files to enque')
parser.add_argument('--uri', help='URI of the queue')
parser.add_argument('--port', help='Port queue is listening on')
parser.add_argument('--user', help='Username to authenticate to queue')
parser.add_argument('--password', help='Password to authenticate to queue')
args = parser.parse_args()
#Regex for matching log files in directory
logFiles = re.compile(args.regex)

credentials = pika.PlainCredentials(args.user, args.password)
connection = pika.BlockingConnection(
  pika.ConnectionParameters(args.uri, args.port, '/', credentials))
channel = connection.channel()
#================================
#TODO: better handling of queues
#Make sure queue exists
channel.queue_declare(queue='logs')
#Clean queue out, mostly for testing purposes
channel.queue_purge(queue='logs')
#================================
for root, dirs, files in os.walk(args.root):
  for f in files:
    if logFiles.search(f) != None:
      log = open(os.path.join(root,f), 'r') 
      channel.basic_publish(exchange='', routing_key='logs', body=log.read())
connection.close()