import numpy as np
import cv2
import os
from common import splitfn
import sys, getopt
from glob import glob
from PIL import Image
from PIL.ExifTags import TAGS
from os.path import expanduser
home = expanduser("~")


USAGE = '''
USAGE: calib.py [--save <filename>] [--debug <output path>] [--square_size] [<image mask>]
'''
def _getExif(photoHandle):
        exif = {}
        info = photoHandle._getexif()
        if info:
            for attr, value in info.items():
                decodedAttr = TAGS.get(attr, attr)
                if decodedAttr in exifAttrs: exif[decodedAttr] = value
        return exif
    
def run():
    trivim_dir= open(os.path.join(home,"Trivim.txt")).readline()
    count=0
    os.chdir(trivim_dir)
    with open('camera_calibration\\value.txt', 'w') as myFile:
            myFile.write("0")
    f = open("camera_calibration\\path.txt","r")
                #Read whole file into data
    photoDir=f.read()
    path=photoDir+"\\*.jpg"
    print path

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
    args = dict(args)
    try: img_mask = img_mask[0]
    except: img_mask = path
    img_names = glob(img_mask)
    debug_dir = args.get('--debug')
    square_size = float(args.get('--square_size', 1.0))

    pattern_size = (9, 6)
    pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 )
    pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = 0, 0
    width=3872
    flag=False
    
    for fn in img_names:
        count=count+1
        print count
        with open('camera_calibration\\value.txt', 'w') as myFile:
            myFile.write(str(count))
        print 'processing %s...' % fn,
        img = cv2.imread(fn, 0)
        h, w = img.shape[:2]
        found, corners = cv2.findChessboardCorners(img, pattern_size)
        if found:
            if flag==False:
                inputFileName = os.path.join(photoDir, fn)
                photoHandle = Image.open(inputFileName)
                # get EXIF information as a dictionary
                exif = _getExif(photoHandle)
                if 'ExifImageWidth' in exif:
                    width = float(exif['ExifImageWidth'])
                    Flag=True
            term = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1 )
            cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)
        if debug_dir:
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.drawChessboardCorners(vis, pattern_size, corners, found)
            path, name, ext = splitfn(fn)
            cv2.imwrite('%s/%s_chess.bmp' % (debug_dir, name), vis)
        if not found:
            print 'chessboard not found'
            continue
        img_points.append(corners.reshape(-1, 2))
        obj_points.append(pattern_points)
        print 'ok'

    try:
        rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h))

        f = open(r"camera_calibration\sensor_value.txt","r")
                #Read whole file into data
        value=f.read()
        value=value.split('-')
        sensor_value=float(value[len(value)-1])
        f.close()
        
        focalPixels=camera_matrix[0][0]
        focalLength=(focalPixels*sensor_value)/width;

        with open('camera_calibration\\calib_temp.txt', 'w') as myFile:
            myFile.write("Camera Name : "+str(value[0])+"\n")
            myFile.write("Sensor Width : "+str(sensor_value)+"\n")
            myFile.write("Root Mean Square(RMS) value : "+str(rms)+"\n")
            myFile.write("Distortion Coefficients : ")
            for log in dist_coefs.ravel():
                myFile.write(str(log)+"\t")
            myFile.write("\n"+"Camera Matrix : "+"\n")
            for log in camera_matrix:
                myFile.write(str(log)+"\n")
            myFile.write("Focal Length(mm) : " + str( focalLength )+"\n")
        with open('camera_calibration\\finish.txt', 'w') as myFile:
            myFile.write("finish")
    except:
        with open('camera_calibration\\finish.txt', 'w') as myFile:
            myFile.write("failed")  
    
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()
