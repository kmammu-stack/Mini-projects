import time
import random
import paho.mqtt.client as mqtt

# Using a public test broker
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "workspace/mini_project_7/data"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

print( "Connecting to broker..." )
client.connect(BROKER, PORT, 60)

try:
    while True:
        # Generate a random reading
        random_value = round(random.uniform(20.0, 35.0), 2)
        message = f"Sensor Reading: {random_value}°C"
        
        print(f"Publishing: {message}")
        client.publish(TOPIC, message)
        
        time.sleep(3)  # Publish every 3 seconds
except KeyboardInterrupt:
    print("\nPublisher stopped.")
    client.disconnect()