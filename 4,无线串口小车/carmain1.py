from pyb import Pin,Timer,ExtInt,UART,Servoimport timeu=UART(3,9600)ss=Pin(Pin.cpu.A13,Pin.OUT)from car import *import re,timecmds={	'back':back2,	'forward':forward2,	'stop':stop,	'add':add,	'dec':dec,}ss.value(0)def jdytest():	print("jdytest")	for s in ('BAUD','RFID','DVID','RFC'):		u.write('AT+'+s+'\r\n')		while not u.any():			pass		print (u.read())jdytest()u.write('AT+CLSSA0\r\n')time.sleep(2)print(u.read())ss.value(1)print(ss.value())while(1):	s=u.readline()	if s:		print(s)		try:			s=str(s,'utf-8')		except:			continue		if '\r\n' in s:			s=s.strip('\r\n')			if s.isdigit():			print(s)			d=int(s)			d=int(d*40/1023)			print(d)			servo.duty(80+d)			time.sleep(1)			#print(d)		else:			for cmd in cmds.keys():				if cmd==s:					cmds[s]()					break	time.sleep(0.1)