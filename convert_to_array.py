import numpy as np
import os 
import argparse
import cv2
#import matplotlib.pyplot as plt


#creating arguments
parser = argparse.ArgumentParser(description = 'image_to_array')
parser.add_argument('-l','--frame_location',type = str, metavar = '', help = 'location of animations' )
parser.add_argument('-a','--array_location',type = str, metavar = '', help = 'location of arrays' )
args = parser.parse_args()



training_data=[]

#check if animations exist
def start(frame_location,array_location):
    if os.path.exists(frame_location):
        convert(frame_location,array_location)
    else:
        print('Does not exist')

#convert to array
def convert(frame_location,array_location):
    for path in os.listdir(frame_location):
            img=cv2.imread(frame_location, cv2.IMREAD_UNCHANGED)
            training_data.append(img)
    path2=os.path.join(array_location,"training_data.npy")
    np.save(path2, training_data)


if __name__ == '__main__':
    start(args.frame_location,args.array_location)

os.chdir(r"E:\projects\video")

path_=r"E:\projects\video\animation"


    



