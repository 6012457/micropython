import paho.mqtt.client as mqtt
def on_message(client, userdata, msg):
    print('topic: {}'.format(msg.topic))
    print('message: {}'.format(str(msg.payload)))


client = mqtt.Client()
client.on_message = on_message

HOST_IP = '192.168.3.100' 
HOST_PORT = 1883 
TOPIC_ID = 'led_control' 


client.connect(HOST_IP, HOST_PORT, 60)

client.subscribe(TOPIC_ID)


client.loop_forever()