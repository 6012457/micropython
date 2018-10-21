import _thread#tcpserver

#from pid import PID
import  mycar
import time
from pyb import Pin,UART
car=mycar.car()
cmds={
    'stop':car.stp,
    'forward':car.fwd,
    'back':car.bak,

}
u1=UART(1,115200)



def uartmain():
	while(1):
		strs=u1.readline()
		if(strs and '\r\n' in strs):
			print(strs)
			cmd=str(strs,'utf-8')
			cmd=cmd.strip('\r\n')
			if cmd in cmds.keys():
				print(cmd)
				cmds[cmd]()
				u1.write(str(car.allvd())+'\r\n')
uartmain()