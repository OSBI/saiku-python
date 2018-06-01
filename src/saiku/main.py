'''
Created on 2018/05/31

@author: Bruno Catao
'''

from flask import Flask
from flask import request

# Create the Flask APP
app = Flask(__name__)

# Setup the webservice routes
@app.route("/")
def hello():
  return "It's alive"

# Start the server
if __name__ == '__main__':
  app.run(port='5002', threaded=False)
