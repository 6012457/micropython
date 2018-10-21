from machine import ADC, Pin,UART
import time

x = ADC(Pin(34))            #����IO36Ϊģ��IO��
x.atten(ADC.ATTN_11DB)      #����˥����
x.width(ADC.WIDTH_10BIT)    #����12λ���ݿ��

y = ADC(Pin(35))            #����IO36Ϊģ��IO��
y.atten(ADC.ATTN_11DB)      #����˥����
y.width(ADC.WIDTH_10BIT)    #����12λ���ݿ��

u = UART(2)   
u.init( baudrate=9600, bits=8, parity=None, stop=1, tx=4, rx=0, rts=-1, cts=-1, timeout=0, timeout_char=1)
ss=Pin(32,Pin.OUT)
ss.value(0)
def jdytest():
    print("jdytest")
    for s in ('BAUD','RFID','DVID','RFC','CLSS'):
        u.write('AT+'+s+'\r\n')
        time.sleep(1)
        print (u.read())
jdytest()
u.write('AT+CLSSA0\r\n')
time.sleep(2)
print(u.read())

ss.value(1)
led=Pin(21,Pin.OUT)
st=Pin(33,Pin.IN)
s1=Pin(25,Pin.IN)
s2=Pin(19,Pin.IN)
s3=Pin(14,Pin.IN)
s4=Pin(18,Pin.IN)
s5=Pin(13,Pin.IN)
s6=Pin(2,Pin.IN)
cmds1={
	'forward':s1,
	'back':s2,
}
cmds2={
	'add':s3,
	'dec':s4,
	'stop':st

}
lastx=x.read()
lasty=''
lastcmd=''
if ss.value():
	led(1)
print('command is start')
while(1):
	xnum=x.read()
	ynum=y.read()

	if (abs(lastx-xnum)>30):
		u.write(str(xnum)+'\r\n')
		print(xnum)
	if  y.read()>500 and 'forward' != lasty:
		u.write('backr\n')
		print('forward')
		lasty='forward'
	if y.read()< 450 and 'back' != lasty:
		u.write('forward\r\n')
		print('back')
		lasty='back'
	for cmd in cmds1.keys() :
		if cmds1[cmd].value()==0 :
			time.sleep(0.1)
			if cmds1[cmd].value()==0 and lastcmd !=cmd :
				print(lastcmd,cmd)
				u.write(cmd+'\r\n')
				print(cmd)
				print(lastcmd,cmd)
				lastcmd=cmd
				break
	for cmd2 in cmds2.keys():
		if cmds2[cmd2].value()==0:
			u.write(cmd2+'\r\n')
			print(cmd2)
			print(cmd2+' down')
			if cmd2=='stop':
				lastcmd=''
			while (cmds2[cmd2].value()==0):
				pass
			print(cmd2+' up')
			break

	time.sleep(0.05)
	lastx=xnum
