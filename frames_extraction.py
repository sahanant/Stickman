# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:50:14 2019

@author: Anant
"""

import cv2
import os
def frames(path,location):
    if not os.path.exists(location):
        os.mkdir(location)
    
    cap=cv2.VideoCapture(path)
    count=0
    while(cap.isOpened()):
        
        ret,frame=cap.read()    
        
        if ret==True:
            print("No of %d frames"%count,ret)
            cv2.imwrite(os.path.join(location,"frame{:d}.jpg".format(count)),frame)
            count+=1
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    
def main():
    frames('videoplayback.mp4','animation')
    
    
main()
        