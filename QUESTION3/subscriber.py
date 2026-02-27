import paho.mqtt.client as mqtt

port=1883 #defien the port
broker="test.mosquitto.org"
topic="home/alert" #give the topic alert

def on_message(client,userdata,msg):
    print(f"Received message: {msg.paylod.decode()}")

client = mqtt.Client(
    client_id="Subscriber",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1 #type: ignore
)
client.connect(broker,port) #connect the subscriber to the broker

client.subscribe(topic)
client.on_message= on_message
print("listening for messages")
client.loop_forever() #run an infinite loop
