# Saiku Python Client

This is an implementation of a Python client for the Saiku core features. It exposes those features as a REST webservice.

## Architecture

The architecture is based on a messaging queue service, [RabbitMQ](https://www.rabbitmq.com/). Saiku core is implemented in Java, it exposes its functionalities as RPC functions. On the other side, there's a Python RPC client which connects to the message queue, sends messages to the Java RPC server. 

## Requirements

1. Install Erlang (http://www.erlang.org/downloads)
2. Install RabbitMQ (https://www.rabbitmq.com)
3. Download the Saiku Report Viewer Server
```
git clone -b development https://github.com/OSBI/saiku-report-viewer-server
```
4. Download the Saiku Python RPC Client
```
git clone https://github.com/OSBI/python_saiku_report_viewer_server
```

## Running
1. Run the RabbitMQ service
2. Run the Saiku service (org.saiku.reportviewer.server.Main)
3. Run the Python client (python -m saiku.main)
4. Open the following URL on a browser: http://127.0.0.1:5002/