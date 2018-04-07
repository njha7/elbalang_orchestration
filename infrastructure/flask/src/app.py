from flask import Flask
from flask import request
import os
import analyze_dataset
app = Flask(__name__)

@app.route('/process', methods=['GET', 'POST'])
def processLog():
  #TODO handle uploaded file with elbalang
  if request.method == 'POST':
    print(request.data)
    # experiment_data = open(request.data.name, 'w')
    # experiment_data.write(request.data.log)
    # toReturn = analyze_dataset.analyze_one_file(request.data.name)
    # if(toReturn):
    #   os.remove(request.data.name)
    #   return toReturn
    # return "An Error has Occured"
    return 200

# def auth():
  #TODO provide a token for users to use that allows access to the API

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')