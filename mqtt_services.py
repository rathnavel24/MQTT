from paho.mqtt import client as mqtt_client
import datetime
import os
import json

cur_time = int(datetime.datetime.now().timestamp())

broker = 'cbe.themaestro.in'
port = 1884
topic = "#"

client_id = f"mconnect{cur_time}"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            client.subscribe(topic) 
        else:
            print(f"Connection failed with code {rc}")

    def on_disconnect(client, userdata, rc):
        print(f"Disconnected with code {rc}", flush=True)
        print(f"Restarting PID: {os.getpid()}", flush=True)
        os._exit(1)

    client = mqtt_client.Client(client_id=client_id, clean_session=False)

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    return client


def on_message(client, userdata, msg):
    print("MESSAGE RECEIVED")
    print("Topic:", msg.topic)

    try:
        payload = msg.payload.decode()
        print("Payload:", payload)

        try:
            data = json.loads(payload)
            print("JSON:", data)
        except:
            print("Not JSON")

    except Exception as e:
        print("Error:", e)


def run():
    print("MQTT Initialize")

    client = connect_mqtt()
    client.on_message = on_message   # ✅ assign ONCE

    client.connect(broker, port)     # ✅ connect here
    client.loop_forever()


if __name__ == "__main__":
    run()