#8266server


import socket
import machine
import time 
import network
from html import *
from machine import Pin,UART
cmds={
    'left':'left',
    'right':'right',
    'stop':'stop',
    'forward':'fwd',
    'back':'bak',

}
SSID="MicroPython-23c3a2"
PASSWORD="micropythoN"
#默认ap
SSID="FAST"
PASSWORD="13606516240"
port=80
wlan=None
listenSocket=None
u2 = UART(2)   
u2.init( baudrate=115200, bits=8, parity=None, stop=1, tx=4, rx=0, rts=-1, cts=-1, timeout=0, timeout_char=1)
ss=Pin(32,Pin.OUT)
def connectWifi(ssid,passwd): #建立wifi连接
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True
def ap():
    global  wlan
    wlan = network.WLAN(network.AP_IF)  # create access-point interface
    wlan.active(True)  # activate the interface
    wlan.config(essid="car", authmode=network.AUTH_WPA_WPA2_PSK, password="12345678")
    print(wlan.ifconfig())

connectWifi(SSID,PASSWORD)
ip=wlan.ifconfig()[0]
listenSocket = socket.socket() #建立一个实例
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind((ip,port))  #绑定建立网路连接的ip地址和端口
listenSocket.listen(5) #开始侦听
print ('tcp waiting...')

def uartstr(strs):
  strs=str(strs,'utf-8')
  strs=strs.strip()
  return strs
while True:
    conn, addr = listenSocket.accept()
    request = conn.recv(1024)
    request = str(request)
    ss='None'
    for cmd in cmds.keys():
        if request.find('/?CMD='+cmd)==6:
            print("ok")
            u2.write(cmd+'\r\n')
            time.sleep(0.5)
            ss=u2.read()
            ss=uartstr(ss)
                
    response = html_header+html_body+ss+html_end #将html的网页定义装载在回应字段
    conn.send(response) #send到浏览器上，就形成了控制界面
    conn.close() 


