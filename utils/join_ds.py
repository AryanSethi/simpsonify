import os
import shutil

def join_ds(base_src,base_dest):
    all_dirs = os.listdir(base_src)
    index = 0
    for dir in all_dirs:
        src = os.path.join(base_src, dir)
        imgs = os.listdir(src)
        for img in imgs:
            shutil.copy(os.path.join(src, img), os.path.join(base_dest, img))
            img_name = 'image_' + str(index) + '.jpg'
            os.rename(os.path.join(base_dest, img), os.path.join(base_dest, img_name))
            index = index + 1

#join_ds('../simpsons_dataset','../ds/simpsons')
join_ds('../faces','ds/people')

