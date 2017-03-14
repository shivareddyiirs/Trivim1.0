import numpy as np
import transformations as trans
from PIL import Image
import os
import urlparse
import os.path

def twod(seg_image,projPath):
    imagecoor=os.path.join(projPath,"PointCloud/ImageCoor")
    os.chdir(imagecoor)
    imgno1=seg_image[7:]
    print imgno1
    f=open('imagenew'+ str(int(imgno1))+'.txt','r')
  #  f=open('imagenew'+ str(int(imgno1))+'.txt','r')
    
    arr1=np.genfromtxt(f, usecols=(1,2))
    data = np.matrix(arr1, copy=False)
    data5= add1(data.T)
    print "2d",data5
    return data5


def threed(seg_image,projPath):
    imagecoor=os.path.join(projPath,"PointCloud/ImageCoor")
    os.chdir(imagecoor)
    imgno1=seg_image[7:]
    print imgno1
    f=open('imagenew'+ str(int(imgno1))+'.txt','r')

  #  f=open('imagenew'+ str(int(imgno1))+'.txt','r')
    arr2=np.genfromtxt(f, usecols=(3,4,5))
    data1 = np.matrix(arr2, copy=False)
    print "3d", data1.T
    return data1.T

def change(data1,data5,image_data1,image_data2,filename,projPath):

    Tr = trans.superimposition_matrix(data1,data5,True)
    print "Transformation", Tr
    print "shape of TR", np.shape(Tr)
    #print trans.decompose_matrix(Tr)
    Coords1 = applyTransform(Tr,image_data1)
    Coords2 = applyTransform(Tr,image_data2)
    print "Coords1", Coords1
    print "Coords2", Coords2
    os.chdir(projPath)
    imagecoor=os.path.join(projPath,"Height")
    os.chdir(imagecoor)
   # os.mkdir('Height')
    with open(filename+'.txt','w') as output:
        np.savetxt(output,Coords1,fmt="%s")
        np.savetxt(output,Coords2,fmt="%s")
    


    
def add1(x):
    
    columns= np.shape(x)
    #print "shape", columns
    ones= np.ones(columns[1])
   # print "ones",ones
    temp=np.vstack((x,ones))
    print temp
    return temp

def applyTransform(Tr,image_data1):
    
    x = add1(image_data1)
    #print "mdlcoords", x
    y= np.dot(Tr,x)
    return y.T

def imagematrix(mask):
   # image="00000000.jpg"
    #image1=Image.open(image)
    #image1.load()
    #image_data1=np.asarray(image1)
  #  print "image_matrix", image_data1
    #x= 549.56879682
    #y=328.83977985
    #mask=[ 353.30087143,  578.34291393 , 131.28413087,  693.88923712]

    im1=np.asarray([[mask[3],mask[0]]])
    im2=np.asarray([[mask[3],mask[1]]])            
  #  image_data1=add1(image_data2)
    print "first",im1.T
    print "second",im2.T
    image_data1=add1(im1.T)
    image_data2=add1(im2.T)
    print image_data1
    print image_data2
    print  np.shape(image_data1)
    print  np.shape(image_data1)
    return image_data1,image_data2



def run(mask,filename,projPath,seg_image):
    data1=twod(seg_image,projPath)
    data5=threed(seg_image,projPath)
    image_data1,image_data2=imagematrix(mask)
    print "shape of 2d", np.shape(data1)
    print "shape of 3d", np.shape(data5)
    print "shape of image1",np.shape(image_data1)
    print "shape of image2",np.shape(image_data2)
   
    change(data1,data5,image_data1,image_data2,filename,projPath)
    
#run(mask,filename,projPath,seg_image)





            
