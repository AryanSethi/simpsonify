import os
import random

random = random.Random()

image_names = os.listdir('../ds/simps')
#4142
deleted=[]
while(len(deleted)!=400):
    ix = random.randint(0,len(image_names))
    file_name = os.path.join('..\\ds\\simps',image_names[ix])
    try:
        os.remove(file_name)
        deleted.append(ix)
    except:
        pass
