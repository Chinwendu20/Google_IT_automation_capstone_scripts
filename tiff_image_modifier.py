#!/usr/bin/env python3
from PIL import Image
import os
directory=os.listdir(os.getcwd()+'/supplier-data/images')

def image_edit():
        list_im=[]
        for file in directory:
                if file.endswith('.tiff'):
                        im=Image.open(os.getcwd()+'/supplier-data/images/'+file)
                        new_im=im.resize((600,400)).rotate(90).convert('RGB')
                        new_im.save(os.getcwd()+'/supplier-data/images/'+'/{}.jpeg'.format(file[0:-5]))
                        list_im.append('{}.jpeg'.format(file[0:-5]))
                        im.close()
        return list_im