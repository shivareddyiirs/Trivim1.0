from PIL import Image
import os
import numpy as np
import shutil

def crop_image(image,mask,database,filename,main_directory):
    pic_name=filename[:filename.find("_")]
    cropBox = (mask[0],mask[1],mask[2],mask[3])
    image1=Image.open(image)
    image1.load()
    image_data1=np.asarray(image1)
    image_data_new = image_data1[cropBox[0]:cropBox[1], cropBox[2]:cropBox[3] , :]
    new_image = Image.fromarray(image_data_new)
    if os.path.isdir(main_directory+"\\"+pic_name) == True:
        print main_directory+"\\"+pic_name
        dst=main_directory+"\\"+pic_name
        print filename
        new_image.save(dst+"\\"+filename+".jpg")
        shutil.copy(database,dst+"\\"+filename+".txt")
        print "save"
    else:
        os.mkdir(main_directory+"\\"+pic_name)
        dst=main_directory+"\\"+pic_name
        print filename
        new_image.save(dst+"\\"+filename+".jpg")
        shutil.copy(database,dst+"\\"+filename+".txt")
        print "new building save"
##crop_image("C://Trivim2.0//DSC01008.JPG",[1000,10000,1000,10000],"build1_1","C://Trivim2.0//segmentation test")
