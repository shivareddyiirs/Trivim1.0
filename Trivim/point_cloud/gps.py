from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import sys
import LatLongUTMconversion as con
import logging

#function to get photos from the directory
def getPhotosFromDirectory(photoDir):
    return[f for f in os.listdir(photoDir) if os.path.isfile(os.path.join(photoDir, f)) and os.path.splitext(f)[1].lower()==".jpg"]
 
def get_exif_data(image):
    """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
 
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
 
    return exif_data
 
def _get_if_exist(data, key):
    if key in data:
        return data[key]
		
    return None
	
def _convert_to_degress(value):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)
 
    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)
 
    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)
 
    return d + (m / 60.0) + (s / 3600.0)
 
def get_lat_lon(exif_data):
    """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
    lat = None
    lon = None
    alt= None

    gps_altitude=0
 
    if "GPSInfo" in exif_data:		
        gps_info = exif_data["GPSInfo"]
 
        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')
        gps_altitude=gps_info.get('GPSAltitude')
        gps_altitude_ref=gps_info.get('GPSAltitudeRef')
 
        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat = 0 - lat
 
            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon
                
    if gps_altitude:
        altn,altd=gps_altitude
        alt=float(altn)/float(altd)
    
    return lat, lon,alt
 
################
# Example ######
################
def run(a):
    # load an image through PIL's Image object
    if len(a) < 2:
        print "Error! No image file specified!"
        print "Usage: %s <filename>" % a[0]
        sys.exit(1)
    inp=open(a[1],"w")
    p=getPhotosFromDirectory(a[0])
    inp.write("cam_x\tcam_y\tcam_z\tdescriptor\n")
    i=1
    for path in p:
        #print(path)
        photopath=os.path.join(a[0],path)
        #print photopath
        photoHandle = Image.open(photopath)        
        exif_data = get_exif_data(photoHandle)
        lat,lon,alt=get_lat_lon(exif_data)
              
        if lat==None or lon==None or alt==None:
            inp.write("none none none")
            inp.write('\n')
            
        else:
            (z, e, n) = con.LLtoUTM(23,lon,lat)
            inp.write(str(e)+'\t'+str(n)+'\t'+str(alt)+"\tphoto_"+str(i)+'\n')
        i=i+1
