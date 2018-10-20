from pyb import Pin, Timer, ExtInt, UART, Servo, ADC
import time
import math

class car(object):
	def __init__(self):
		self.vd = ADC(Pin(Pin.cpu.A2))
		self.servo=Servo(4)
		self.curr_angle=self.center_angle=48
		self.f2b=0
		self.r1 = Pin(Pin.cpu.C4, Pin.OUT)
		self.r2 = Pin(Pin.cpu.A4, Pin.OUT)
		self.t2 = Timer(2, freq=1000)
		self.l = self.t2.channel(2, Timer.PWM, pin=Pin(Pin.cpu.B3))
		self.l1 = Pin(Pin.cpu.B9, Pin.OUT)
		self.l2 = Pin(Pin.cpu.B0, Pin.OUT)
		self.t8 = Timer(8, freq=1000)
		self.r = self.t8.channel(3, Timer.PWM_INVERTED, pin= Pin(Pin.cpu.B15))
		self.lv = 0
		self.rv = 0
		self.v = 25
		self.countR=self.countL=0
		self.turn(self.center_angle)
		self.dinit_encoder()
		self.init_encoder()

	def turn(self,angle):
		if angle <3:
			angle=3
		if angle >93:
			anlge=93
		self.servo.angle(angle)
		self.curr_angle=angle
		self.run()
	def bak(self):
		self.r1.value(0), self.r2.value(1)
		self.l1.value(1), self.l2.value(0)
		self.f2b=1
		self.run()
	def fwd(self):
		self.r1.value(1), self.r2.value(0)
		self.l1.value(0), self.l2.value(1)
		self.f2b=-1
		self.run()
	def stp(self):
		self.r1.value(1), self.r2.value(1)
		self.l1.value(1), self.l2.value(1)
		self.f2b=0
		self.run()
	
	def run(self):
		self.turn_angle=self.curr_angle-self.center_angle
		if self.v>68:
			self.v=68
		if self.v <38:
			self.v=38
		self.lv=int(self.v*(1-self.f2b*(140/2/152)*math.tan(math.pi*self.turn_angle/180)))
		self.rv=int(self.v*(1+self.f2b*(140/2/152)*math.tan(math.pi*self.turn_angle/180)))
		self.r.pulse_width_percent(self.lv)
		self.l.pulse_width_percent(self.rv)
	
	def allvd(self):
		return self.vd.read()*0.003316877506942302
	def callbackR(self,p):
		self.countR =self.countR +1
	def callbackL(self,p):
		self.countL=self.countL+1
 	def add(self):
 		self.v+=5
 		if self.v>95:
 			self.v=95

 		self.run()
 	def dec(self):
 		self.v-=5
 		if self.v <38:
 			self.v=38
 		self.run()
	def init_encoder(self):   
		ExtInt(Pin.cpu.A1,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=lambda t: self.callbackR(t))
		ExtInt(Pin.cpu.A0,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=lambda t: self.callbackR(t))
		ExtInt(Pin.cpu.B8,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=lambda t: self.callbackL(t))
		ExtInt(Pin.cpu.C7,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=lambda t: self.callbackL(t))
	def dinit_encoder(self):   
		ExtInt(Pin.cpu.A1,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=None)
		ExtInt(Pin.cpu.A0,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=None)
		ExtInt(Pin.cpu.B8,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=None)
		ExtInt(Pin.cpu.C7,ExtInt.IRQ_RISING_FALLING,Pin.PULL_UP,callback=None)


