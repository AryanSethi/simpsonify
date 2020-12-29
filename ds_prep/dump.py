import os
import cv2

imgs = os.listdir('../ds/people')
for img in imgs:
    img_path='../ds/people/'+img
    i =cv2.imread(img_path)
    if(i.shape!=(250,250,3)):
        print('here')