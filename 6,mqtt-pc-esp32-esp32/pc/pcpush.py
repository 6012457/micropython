#pcpush
import paho.mqtt.client as mqtt
import time

HOST_IP = 'localhost' # Server的IP地址
HOST_PORT = 1883 # mosquitto 默认打开端口
TOPIC_ID = 'carcontrol' # TOPIC的ID

# 创建一个客户端
client = mqtt.Client()
# 连接到服务器（本机）
client.connect(HOST_IP, HOST_PORT, 60)

count = 0
client.publish(TOPIC_ID,'forward')
