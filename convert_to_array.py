import numpy as np
import os 
import argparse

#creating arguments
parser = argparse.ArgumentParser(description = 'image_to_array')
parser.add_argument('-l','--frame_location',type = str, metavar = '', help = 'location of animations' )
parser.add_argument('-a','--array_location',type = str, metavar = '', help = 'location of arrays' )
args = parser.parse_args()

#check if animations exist
def start(frame_location,array_location):
    if os.path.exists(frame_location):
        convert(frame_location,array_location)
    else:
        print('Does not exist')

#convert to array
def convert(frame_location,array_location):
    dirs = os.listdir(frame_location)
    for file in dirs:
       temp = np.asarray(file)
       np.savez_compressed(array_location,temp,'arrays') 


if __name__ == '__main__':
    start(args.frame_location,args.array_location)
