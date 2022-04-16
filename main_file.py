import cv2
import time
import send
import bot_control
import subprocess
from threading import *

thres = 0.45 # Threshold to detect object

subprocess.Popen("echo out >/sys/class/gpio/gpio1807/direction", shell=True, stdout=subprocess.PIPE) # Enabling GPIO pin to send a signal to rasp-pi

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('n').split('n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

#-----------------------------------This is the main class which contains the processing part-------------------------------------------
class Process(Thread):    
	def run(self):
		count=0
		while True:
			success,img = cap.read()
			classIds, confs, bbox = net.detect(img,confThreshold=thres)
			tup = (0, 0, 0, 0)
			width= cap.get(3)
			height = cap.get(4)
			framecx=(width)/2
			framecy=(height)/2
    
			frheight=50
			frwidth=160

			topx = (int(framecx) - (frwidth) / 2)
			topy = (int(framecy) - (frheight) / 2)
			botx = (int(framecx) + (frwidth / 2))
 			boty = (int(framecy) + (frheight) / 2)

			cv2.circle(img, (int(framecx),int(framecy)), 7, (0, 255, 255), -1)
			cv2.rectangle(img, (int(topx), int(topy)), (int(botx), int(boty)), (230, 255, 255), 3)
			cv2.line(img, (0, int(framecy)), (int(width), int(framecy)), (0, 255, 0), 2)
			cv2.line(img, (int(framecx), int(height)), (int(framecx), 0), (0, 255, 0), 2)

			cx=0
			cy=0
	
			if len(classIds) != 0:
				for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
					if classId == 44:
						tup=box
                				cx = (tup[0] + (tup[0] + tup[2])) / 2
                				cy = (tup[1] + (tup[1] + tup[3])) / 2
						time.sleep(0.2)
						dum=box
						if(tup.all()==box.all()):
							if(dum.all()==box.all()):
                						cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                						cv2.circle(img, (int(cx), int(cy)), 7, (0, 0, 255), -1)
                				if (topy < cy < boty) and (topx < cx < botx):
                					print("stop")
                					time.sleep(1)
                				if (topy < cy < boty) and (topx < cx < botx):
							print("pick the bottle")
                    					subprocess.Popen("echo 1 >/sys/class/gpio/gpio1807/value", shell=True, stdout=subprocess.PIPE)
							time.sleep(1)
							subprocess.Popen("echo 0 >/sys/class/gpio/gpio1807/value", shell=True, stdout=subprocess.PIPE)

						elif (0 < cx < topx):
                    					print("left")
                    					bot_control.left()

                				elif (botx < cx < width):
                    					print("right")
                    					bot_control.right()

                				elif (topx < cx < botx) and (0 < cy < topy):
                    					print("forward")
                    					bot_control.forward()

                				elif (topx < cx < botx) and (boty < cy < height):
                    					print("backward")
                    					bot_control.backward()

					elif (cy==0) and (cx==0):
                				print("no bottle")
						Process.count = Process.count + 1
                    
			cv2.imshow("Output",img)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		cap.release()
		cv2.destroyAllWindows()

#-----------------------The below thread is used to send the data to the cloud------------------------------------
class Cloud(Thread):
	def run(self):
		while True:
			send.send_to_cloud()

#----------------------The below thread executes when there is no bottle present infront of the bot---------------
class Nobottle(Thread):
	mov=0 
	def run(self):
		while True:
			if(Process.count == 5):
				Process.count=0
				Nobottle.mov = Nobottle.mov + 1
				print("mov=",Nobottle.mov)
				if(Nobottle.mov<=10):
					bot_control.forward()
				else:
					bot_control.right()
					bot_control.right()
					bot_control.right()
					Nobottle.mov=0


t1=Process()
t2=Cloud()
t3=Nobottle()

t1.start()
t2.start()
t3.start()


			 
			
		
