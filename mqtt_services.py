from paho.mqtt import client as mqtt_client
import requests
import datetime
import time
import os

from insert_services import insert_data

cur_time = int(datetime.datetime.now().timestamp())

broker = 'cbe.themaestro.in'
port = 1884

topic = "test/data" # Replace with the topic you want to subscribe to

client_id = f"mconnect{cur_time}"

import json

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            # Subscribe to the topic when connected
            client.subscribe(topic)
        else:
            print(f"Connection failed with code {rc}")
    def on_disconnect(client, userdata, rc):
        print(f"Disconnected from MQTT Broker with result code {rc}", flush=True)
        """Kill the current process to trigger a restart via Supervisor."""
        print(f"Restarting process with PID: {os.getpid()}", flush=True)
        os._exit(1)

    client = mqtt_client.Client(client_id=client_id,clean_session=False)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg): 
        print(msg.topic)
        print("RECEIVED MQTT DATA") #msg.payload,
        try:
            #data=msg.payload.decode()
            payload = json.loads(msg.payload.decode())
            insert_data(payload)
            print(payload)
        except:
            data = ""
            print(f"Received data error {cur_time}")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    print("MQTT Initialize")
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()