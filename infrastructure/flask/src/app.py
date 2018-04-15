from flask import Flask
from flask import request
from google.cloud import storage
import os
import analyze_dataset
import sys
import traceback

storage_client = storage.Client()
input_bucket = storage_client.get_bucket(os.environ['INPUT_BUCKET'])
output_bucket = storage_client.get_bucket(os.environ['OUTPUT_BUCKET'])

def download_log(object_path):
  # containerFP = object_path.decode().split('/')
  containerFP = object_path.split('/')
  localFP = containerFP[len(containerFP) - 1]
  print(localFP)
  print(containerFP)
  blob = input_bucket.blob(object_path)
  blob.download_to_filename(localFP)
  return './' + localFP

def upload_result(source_file_name, bucket_path):
    blob = output_bucket.blob(bucket_path)
    blob.upload_from_filename(source_file_name)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloElba():
  return 'Hello Elba'

@app.route('/process', methods=['GET', 'POST'])
def processLog():
  if request.method == 'POST':
    try:
      print(request.form)
      print(request.form['data'])
      experiment_data = download_log(request.form['data'])
      toReturn = analyze_dataset.analyze_one_file(experiment_data)
      if(toReturn != None):
        results = open(experiment_data, 'w')
        results.write(str(toReturn))
        results.close()
        upload_result(experiment_data, request.form['data'])
        os.remove(experiment_data)
        return 'Success', 200
      else:
        return 'Error', 500
    except Exception as e:
        print(e.message)
        return 'Error', 500

# def auth():
  #TODO provide a token for users to use that allows access to the API

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')