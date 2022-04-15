import subprocess
import time

# Enabling GPIO pins as OUTPUT

subprocess.Popen("echo out >/sys/class/gpio/gpio1803/direction", shell=True, stdout=subprocess.PIPE)
subprocess.Popen("echo out >/sys/class/gpio/gpio1804/direction", shell=True, stdout=subprocess.PIPE)
subprocess.Popen("echo out >/sys/class/gpio/gpio1805/direction", shell=True, stdout=subprocess.PIPE)
subprocess.Popen("echo out >/sys/class/gpio/gpio1806/direction", shell=True, stdout=subprocess.PIPE)

def stop():
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1803/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1804/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1805/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1806/value", shell=True, stdout=subprocess.PIPE)

def right():
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1803/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1804/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1805/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1806/value", shell=True, stdout=subprocess.PIPE)
	time.sleep(0.1)
	stop()
	time.sleep(1)

def left():
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1803/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1804/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1805/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1806/value", shell=True, stdout=subprocess.PIPE)
	time.sleep(0.1)
	stop()
	time.sleep(1)

def backward():
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1803/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1804/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1805/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1806/value", shell=True, stdout=subprocess.PIPE)
	time.sleep(0.1)
	stop()
	time.sleep(1)

def forward():
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1803/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1804/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 0 >/sys/class/gpio/gpio1805/value", shell=True, stdout=subprocess.PIPE)
	subprocess.Popen("echo 1 >/sys/class/gpio/gpio1806/value", shell=True, stdout=subprocess.PIPE)
	time.sleep(0.1)
	stop()
	time.sleep(1)