import numpy as np
from collada import *
import os
import shutil
import UTM as con

projPath=""

def makekmz(outputPath):
    path = os.getcwd()
    print path
    shutil.make_archive(outputPath, "zip", outputPath)
    print "Zip created!"
    os.rename(outputPath+".zip",outputPath+".kmz")


def makeKML(path,outputpath,imageName,height,hkml,a,b,filename,inputPath):
    
    print "inside make kml",path,outputpath,imageName,height
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
        print "directory created"
    outputPath=outputpath;
    
    mesh = Collada()  
    axis = asset.UP_AXIS.Z_UP
    mesh.assetInfo.upaxis = axis
    texture_image=os.path.join(path,imageName)
    shutil.copy(texture_image,outputpath)
    print "this is image",texture_image
    image = material.CImage("material_0_1_0-image", texture_image)
    surface = material.Surface("material_0_1_0-image-surface", image)
    sampler2d = material.Sampler2D("material_0_1_0-image-sampler", surface)
    map1 = material.Map(sampler2d, "UVSET0")
    effect1 = material.Effect("material_0_0-effect", [], "lambert", emission=(0.0, 0.0, 0.0, 1),\
                         ambient=(0.0, 0.0, 0.0, 1), diffuse=(0.890196, 0.882353, 0.870588, 1),\
                         transparent=(1, 1, 1, 1), transparency=0.0, double_sided=True)
    effect2 = material.Effect("material_0_1_0-effect", [surface, sampler2d], "lambert", emission=(0.0, 0.0, 0.0, 1),\
                         ambient=(0.0, 0.0, 0.0, 1),  diffuse=map1, transparent=map1, transparency=0.0, double_sided=True)
    mat1 = material.Material("material_0_0ID", "material_0_0", effect1)
    mat2 = material.Material("material_0_1_0ID", "material_0_1_0", effect2)
    mat3 = material.Material("material_0_1_1ID", "material_0_1_1", effect1)
    mesh.effects.append(effect1)
    mesh.effects.append(effect2)
    mesh.materials.append(mat1)
    mesh.materials.append(mat2)
    mesh.materials.append(mat3)
    mesh.images.append(image)
    h = float(height)
   # w = l
    print "testpycollada a is", a
    print "testpycollada b is", b
    #m1position = [0,0, 0, 0, b, 0, w, b, 0, w, 0, 0, 0, 0, h, 0, b, h, w, b, h, w, 0, h]
    m1position = [a[2], b[2], 0,a[1], b[1], 0,0,0, 0,a[3], b[3], 0,a[2],b[2], h,a[1], b[1], h,0,0, h,a[3], b[3],h]
    m1normal = [1, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1]
    m1uv = [1, 1, 0, 0, 1, 0, 0, 1]
   
    m1position_src = source.FloatSource("mesh1-geometry-position", np.array(m1position), ('X', 'Y', 'Z'))
    m1normal_src = source.FloatSource("mesh1-geometry-normal", np.array(m1normal), ('X', 'Y', 'Z'))
    m1uv_src = source.FloatSource("mesh1-geometry-uv", np.array(m1uv), ('S', 'T'))
    geom = geometry.Geometry(mesh, "mesh1-geometry", "mesh1-geometry", [m1position_src, m1normal_src, m1uv_src])
    geom1 = geometry.Geometry(mesh,"mesh1-geometry1","mesh1-geometry1",[m1position_src, m1normal_src, m1uv_src])
    geom2 = geometry.Geometry(mesh,"mesh1-geometry2","mesh1-geometry2",[m1position_src,m1normal_src, m1uv_src])
    input_list = source.InputList()
    input_list.addInput(0, 'VERTEX', "#mesh1-geometry-position") 
    input_list1 = source.InputList()
    input_list1.addInput(0, 'VERTEX', "#mesh1-geometry-position")
    input_list1.addInput(1, 'TEXCOORD', "#mesh1-geometry-uv", set="0")
    input_list2 = source.InputList()
    input_list2.addInput(0, 'VERTEX', "#mesh1-geometry-position")
    input_list2.addInput(1, 'TEXCOORD', "#mesh1-geometry-uv", set="0")
    indices1 = np.array([0, 1, 2, 2, 3, 0, 0, 1, 5, 5, 0, 4, 7, 2, 6, 2, 7, 3, 4, 3, 7, 3, 4, 0]) 
    indices2 = np.array([2, 1, 1, 2, 5, 0, 5, 0, 6, 3, 2, 1])
    indices3 = np.array([6,1,5,2,4,0,4,0,7,3,6,1])
    triset1 = geom.createTriangleSet(indices1, input_list, "material_0_0")
    triset2 = geom1.createTriangleSet(indices2, input_list1, "material_0_1_0")
    triset3 = geom2.createTriangleSet(indices3, input_list2, "material_0_1_1")
    geom.primitives.append(triset1)
    geom1.primitives.append(triset2)
    geom2.primitives.append(triset3)
    mesh.geometries.append(geom)
    mesh.geometries.append(geom1)
    mesh.geometries.append(geom2)
    matnode1 = scene.MaterialNode("material_0_0", mat1, inputs=[])
    matnode2 = scene.MaterialNode("material_0_1_0", mat2, inputs=[])
    matnode3 = scene.MaterialNode("material_0_1_1", mat3, inputs=[])
    geomnode1 = scene.GeometryNode(geom, [matnode1])
    geomnode2 = scene.GeometryNode(geom1, [matnode2])
    geomnode3 = scene.GeometryNode(geom2, [matnode3])
    node = scene.Node("Model", children=[geomnode1, geomnode2, geomnode3])
    myscene = scene.Scene("SketchUpScene", [node])
    mesh.scenes.append(myscene)
    mesh.scene = myscene
    xx= os.path.join(inputPath,filename)
   
    os.chdir(xx)
    for dir1 in xx:
        fcoord = open(filename +'.txt','r')
        cstr = fcoord.readline()
        fcoord.close()
        longi = (cstr.split('\t'))[1]
        print longi,"longi"
        lat = (cstr.split('\t'))[2]
##    data = np.loadtxt((r'Outputcoordinates.txt'), delimiter = ',')
    path2 = os.chdir(outputpath)
    print path2
    mesh.write("untitled.dae")
    print "Cheers! The COLLADA file has been generated. Please check the local working directory."
    string = '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n'
    str1 = '<Document>\n<name>\n'
    strx = '\n</name>\n'
    f = open('doc.kml','w')
    str2 = '<Style id="default">\n</Style>\n<Style id="default0">\n</Style>\n<StyleMap id= "default1">\n<Pair>\n<key>normal</key>\n<styleUrl>#default</styleUrl>\n</Pair>\n<Pair>\n<key>highlight</key>\n<styleUrl>#default0</styleUrl>\n</Pair>\n</StyleMap>\n'
    str3 = '<Placemark>\n<name>Model</name><styleUrl>#default1</styleUrl>\n<Model id="model_1">\n<altitudeMode>relativeToGround</altitudeMode>\n<Location>\n'
    f.write(string)
    f.write(str1)
    f.write(imageName)
    f.write(strx)
    f.write(str2)
    f.write(str3)
    str4_1 = '<longitude>\n'
    str4_2 = '\n</longitude>\n<latitude>\n'
    str4_3 = '\n</latitude>\n<altitude>\n'
    str4_4 = '\n</altitude>\n</Location>\n'
    str5_1 = '<Orientation>\n<heading>\n'
    str5_2 = '\n</heading>\n<tilt>0</tilt>\n<roll>0</roll>\n</Orientation>\n<Scale>\n<x>1</x>\n<y>1</y>\n<z>1</z>\n</Scale>\n<Link>\n<href>untitled.dae</href>\n</Link>'
    str5_3 = '\n</Model>\n</Placemark>\n</Document>\n</kml>'
    print "path as after string lines",path
    print m1position
    str_final = str4_1 +str(longi) + str4_2 + str(lat) + str4_3 + str(hkml) + str4_4 + str5_1+ str5_2 + str5_3
    f.write(str_final)
    f.close()
    print "Great! KML file generated! Please check the local directory."
    makekmz(outputPath);





