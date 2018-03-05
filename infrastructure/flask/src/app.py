from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/process', methods=['GET', 'POST'])
def processLog():
  #TODO handle uploaded file with elbalang
  if request.method == 'POST':
    return request.data

# def auth():
  #TODO provide a token for users to use that allows access to the API

if __name__ == "__main__":
  app.run(debug = True, host = '0.0.0.0')