import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep

# setup mqtt client
client = mqtt.Client()
client.connect("MASUKKAN IP ADDRES RASPI") 
client.loop_start()

def subscribe(client: mqtt, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

kirim = "Japran Badai"

while True:
  # Mengirim data dengan Publish
	print("Mengirim text mqtt")
	client.publish("MASUKKAN TOPIC", kirim, 0) #Urutannya adalah (TOPIC, DATA, QOS) => QOS bisa diisi 0 aja

  # Menerima data dengan Subscribe
  subscribe(client, "MASUKKAN TOPIC")
	sleep(1)
