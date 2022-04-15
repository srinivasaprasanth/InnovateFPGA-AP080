import time
import json
from unicodedata import name
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = "DefaultEndpointsProtocol=https;AccountName=ragpicker;AccountKey=iF/RKdYu6oAu8GwR2ysLYiuyZ99VWsJ/6Z2EYIuX2+VLvlZE5Tv7zqEROiGdJRVWtJy9M1DcfgYB+AStxUJfbw==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container1 = "ragpicker"
container1_client = blob_service_client.get_container_client(container=container1)
#d=dict()

# enabling this GPIO as input that receives the signal from rasp-pi whenever the bottle is picked
subprocess.Popen("echo in /sys/class/gpio/gpio1808/direction", shell=True, stdout=subprocess.PIPE)  

count=0

def send_to_cloud():
    import subprocess
    sp=subprocess.Popen("cat /sys/class/gpio/gpio1808/value", shell=True, stdout=subprocess.PIPE)
    var=sp.stdout.read()
    var=int(var.decode())
    #d=str(var)
    f=open("file.txt",'a')
    if(var==1):
    	f.write("Bottle picked")            
    	f.write("\n")
    	count=count+1
    	if(count==3):
        	f.write("Bin is full")   # showing the bin status   
        	f.write("\n")
        	count=0
    f.close()    
    print("Written to file")
    try:
        with open('file.txt', 'rb') as j:
            container1_client.upload_blob(data=j, name='test.txt',overwrite=True)
        print("Uploaded to Azure")
    except Exception as e:
        print(e)
        print("Not uploaded to Azure")
    time.sleep(5)
