import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(29,GPIO.IN)

leftdown=GPIO.PWM(32,50)
rightdown=GPIO.PWM(37,50)
rightup=GPIO.PWM(35,50)
leftup=GPIO.PWM(15,50)
bincap=GPIO.PWM(36,50)

leftdown.start(0)
rightdown.start(0)
rightup.start(0)
leftup.start(0)
bincap.start(0)
time.sleep(0.5)

def pick():

    for i in range(90,5,-5):
        duty=((1/18)*i)+2
        leftdown.ChangeDutyCycle(duty)
        rightdown.ChangeDutyCycle(duty)
        time.sleep(0.09)
    time.sleep(1)

    for i in range(0,90,5):
        x=90-i
        y=90+i
        duty=((1/18)*i)+2 
        duty1=((1/18)*x)+2
        duty2=((1/18)*y)+2
        leftup.ChangeDutyCycle(duty1)
        rightup.ChangeDutyCycle(duty2)
        bincap.ChangeDutyCycle(duty)
        time.sleep(0.09)
    time.sleep(1)

    for i in range(5,90,5):
        duty=((1/18)*i)+2
        leftdown.ChangeDutyCycle(duty)
        rightdown.ChangeDutyCycle(duty)
        time.sleep(0.09)
    time.sleep(1)

    for i in range(0,90,5):
        x=i
        y=180-i
        z=90-i
        duty1=((1/18)*x)+2
        duty2=((1/18)*y)+2
        duty3=((1/18)*z)+2
        leftup.ChangeDutyCycle(duty1)
        rightup.ChangeDutyCycle(duty2)
        bincap.ChangeDutyCycle(duty3)
        time.sleep(0.09)
    time.sleep(1)

    leftdown.start(0)
    rightdown.start(0)
    rightup.start(0)
    leftup.start(0)
    bincap.start(0)
    time.sleep(1)

while True:
	i=GPIO.input(29)
	if(i==1):
		pick()
		GPIO.output(24, 1)
		time.sleep(3)
		GPIO.output(24, 0)
	else:
		GPIO.output(24, 0)		