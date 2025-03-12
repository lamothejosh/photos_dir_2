#import libraries 
from picamera2 import Picamera2 
import cv2 as cv 
from libcamera import controls
import time
import os
import sys

filename= "background"

picam2 = Picamera2()

num = 10

#configure the picamera
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous}) #sets auto focus mode

if(not  os.path.isdir(filename)):
        os.mkdir(filename)

picam2.start() #must start the camera before taking any images
time.sleep(1)

curr_elements =  len(os.listdir(filename))

for t in range(curr_elements + num)[curr_elements:]:
    image_name=filename+"/"+str(t)+".jpg"
    picam2.capture_file(image_name) #take image
    time.sleep(0.01)

picam2.stop() #stop the picam 
