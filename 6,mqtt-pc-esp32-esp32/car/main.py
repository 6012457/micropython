import _thread#调试pid用
from pid import PID
import  mycar
car=mycar.car()

u1=UART(1,115200)
pidL= PID(p=0.064, i=0, d=0)
tt=120.01
lock = _thread.allocate_lock()
def cpid():
	lock.acquire()
	#写入countL
	car.countL=car.countR=0
	time.sleep_ms(100)
	#print(car.countL)
	u1.write('REAL_VALUE,'+str(car.countL)+'\r\n')
	#get count
	countL=car.countL

	errorL=tt-car.countL
	outputL=pidL.get_pid(errorL,1)
	#print(countL,errorL,outputL)
	car.r.pulse_width_percent(car.lv+outputL)
	lock.release()
def threadwhile():
	while(1):
		cpid()
def updatepid():
	global pidL,tt
	pid_params={
		'p':0.05,
		'i':0.05,
		'd':0.01

	}
	while(1):
		cmd=u1.readline()
		if cmd != None:
			#print (cmd)
			if ',' in cmd:
				cmd=str(cmd,'utf-8')
				cmd=cmd.strip()
				params = cmd.split(',')
    			cmd_name = params[0]
    			if cmd_name =='SET_PID':
    				#print(params)
    				#print(type(params[1]))
    				cp=float(params[1])
    				ci=float(params[2])
    				cd=float(params[3])
    				pidL=PID(p=cp,i=ci,d=cd)
    			elif(cmd_name=='SET_TARGET'):
    				tt=float(params[1])
    			else:
        			print("[ERROR] 非法指令 {}".format(cmd_name))
        			#print(cmd)

_thread.start_new_thread(threadwhile,(()))
_thread.start_new_thread(updatepid,(()))






