'''
Created on 2018/05/31

@author: Bruno Catao
'''

from flask import Flask
from flask import request
from flask import make_response
import pika
import uuid
import os

class SaikuRpcClient(object):
	def __init__(self):
		r = os.getenv('RABBITMQ_HOST', 'localhost')
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=r))
		self.channel = self.connection.channel()
		result = self.channel.queue_declare(exclusive=True)
		self.callback_queue = result.method.queue
		self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

	def on_response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

	def call(self):
		self.response = None
		self.corr_id = str(uuid.uuid4())
		self.channel.basic_publish(exchange='',
			routing_key='SAIKU',
			properties=pika.BasicProperties(
				reply_to = self.callback_queue,
				correlation_id = self.corr_id,
				),
			body='')
		while self.response is None:
			self.connection.process_data_events()
		return self.response

# Create the Saiku RPC Client
saiku_rpc = SaikuRpcClient()

# Create the Flask APP
app = Flask(__name__)

# Setup the webservice routes
@app.route("/")
def hello():
	response = make_response(saiku_rpc.call())
	response.headers.set('Content-Disposition', 'inline', filename='saiku_report.pdf')
	response.headers.set('Content-Type', 'application/pdf')
	return response

# Start the server
if __name__ == '__main__':
  app.run(port='5002', threaded=False)
