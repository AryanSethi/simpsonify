import cv2
import os

def resize(source_path,dest):
    image_number = 0
    all_image_names = os.listdir(source_path)

    for image_name in all_image_names:
           try:
                image_path = os.path.join(source_path,image_name)
                image = cv2.imread(image_path)
                image = cv2.resize(image,(256,256))

                dest_image_name = 'image'+str(image_number)+'.jpg'
                dest_path = os.path.join(dest,dest_image_name)
                cv2.imwrite(dest_path,image)

                image_number=image_number+1
           except:
               print('broken image'+image_path)

resize('../ds/simpsons','../ds/simps')
resize('../ds/people','../ds/peeps')






