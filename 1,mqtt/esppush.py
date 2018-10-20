from umqtt.simple import MQTTClient
import time

SERVER = '192.168.3.100'
CLIENT_ID = 'PYESPCAR_A0' # 客户端的ID
TOPIC = b'led_control' # TOPIC的ID

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


for i in range(1,10000):
	time.sleep(1)
	client.publish(TOPIC,str(i))