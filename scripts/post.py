import requests
import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--root', help='Root directory of files to enque')
parser.add_argument('--regex', help='Regex of files to enque')
parser.add_argument('--uri', help='URI of the queue')
parser.add_argument('--port', help='Port queue is listening on')
# parser.add_argument('--user', help='Username to authenticate to queue')
# parser.add_argument('--password', help='Password to authenticate to queue')
args = parser.parse_args()
#Regex for matching log files in directory
logFiles = re.compile(args.regex)

#================================

#================================
for root, dirs, files in os.walk(args.root):
  for f in files:
    if logFiles.search(f) != None:
      payload = { 'name': f, 'log': open(os.path.join(root,f), 'rb') }
      r = requests.post(args.uri + ':' + args.port + '/process', data=payload)
      print(r.text)