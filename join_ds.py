import os
import shutil

base_src = 'simpsons_dataset'
base_dest = 'ds/simpsons'

all_dirs = os.listdir('simpsons_dataset')
index = 0
for dir in all_dirs:
    src = os.path.join(base_src,dir)
    imgs = os.listdir(src)
    for img in imgs:
        shutil.copy(os.path.join(src,img), os.path.join(base_dest,img))
        img_name = 'image_'+str(index)+'.jpg'
        os.rename(os.path.join(base_dest,img),os.path.join(base_dest,img_name))
        index=index+1

