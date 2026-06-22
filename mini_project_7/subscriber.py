import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "workspace/mini_project_7/data"

# Callback when connecting to the broker
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected successfully. Subscribing to topic: {TOPIC}")
    client.subscribe(TOPIC)

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received Message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker...")
client.connect(BROKER, PORT, 60)

# Blocking loop that processes network traffic and dispatches callbacks
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber stopped.")
    client.disconnect()