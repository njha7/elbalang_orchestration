from flask import Flask
from flask import request
from google.cloud import storage
import os
import analyze_dataset

storage_client = storage.Client()
input_bucket = storage_client.get_bucket(os.environ['INPUT_BUCKET'])
output_bucket = storage_client.get_bucket(os.environ['OUTPUT_BUCKET'])

def download_log(object_path):
  print(object_path)
  containerFP = object_path.decode().split('/')
  localFP = containerFP[len(containerFP) - 1]
  blob = input_bucket.blob(object_path)
  blob.download_to_filename(localFP)
  return './' + localFP

# def upload_result(file):


app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloElba():
  return 'Hello Elba!'

@app.route('/process', methods=['GET', 'POST'])
def processLog():
  if request.method == 'POST':
    print(request.data)
    experiment_data = download_log(request.data)
    toReturn = analyze_dataset.analyze_one_file(experiment_data)
    if(toReturn != None):
      os.remove(experiment_data)
      # return toReturn
      return 'Success', 200
    else:
      return 'Error', 500

# def auth():
  #TODO provide a token for users to use that allows access to the API

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')