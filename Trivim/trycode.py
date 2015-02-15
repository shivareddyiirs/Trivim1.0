import os
import numpy as np
from collada import * 

mesh = Collada()
Model = 123
modal = scene.Node("Model")
def drawBuilding(list,h_in,h,f,address): 
  # Get handles to our model and the Entities collection it contains.
 
    if (modal==0):
        print "Failed to grab model"
    else:
        ents = modal.entities
        mats = modal.materials

            #new material front
        mat_front = mats.add("face-pic")

        #add automated file name
        mat_front.texture = address

        iterator = list[0].to_i

        pts = []
        #UI.messagebox("iterator")
        #UI.messagebox(iterator)
        for i in 1..iterator:
         pts[i-1] = [((list[2*i+f])-(list[2+f])).m, ((list[1+2*i+f])-(list[3+f])).m, h.m]
        end
        #UI.messagebox("Pts is")
        #UI.messagebox(pts)
        print pts

        # Call methods on the Entities collection to draw stuff.
        new_face = ents.add_face(pts)
                
        #add footprint coordinates in a circular fashion...so that we donot get folded edge type models
        if(new_face.normal==[0,0,-1]):
                h_curr_floor = -1*h_in.m
        else:
                h_curr_floor = h_in.m


        
        new_face.pushpull(h_curr_floor)

        #########
        pts1 = []
        print pts1
        pts1[0] = [0,0,h]
        pts1[1] = [(list[4+f]-list[2+f]).m,(list[5+f]-list[3+f]).m,h.m]
        pts1[2] = [(list[4+f]-list[2+f]).m,(list[5+f]-list[3+f]).m,h.m+h_in.m]
        pts1[3] = [0,0,h+h_in]
        print pts1

        face1 = ents.add_face(pts1)

        pt_array = []
        pt_array[0] = geometry.Geometry.np.array(0,0,h)
        pt_array[1] = geometry.Geometry.np.array(0,0,0)
        pt_array[2] = geometry.Geometry.np.array((list[4+f]-list[2+f]),(list[5+f]-list[3+f]),h)
        pt_array[3] = geometry.Geometry.np.array(1,0,0)
        pt_array[4] = geometry.Geometry.np.array((list[4+f]-list[2+f]),(list[5+f]-list[3+f]),h+h_in)
        pt_array[5] = geometry.Geometry.np.array(1,1,0)
        pt_array[6] = geometry.Geometry.np.array(0,0,h+h_in)
        pt_array[7] = geometry.Geometry.np.array(0,1,0)
                
        on_front = true
        face1.position_material(mat_front, pt_array, on_front)
            ##########


os.chdir(".")
path= os.getcwd()
print path
temp_display_file = os.popen(path+r"/3d-modelling/temp_for_display.txt","w")	
tempfile = path+"/curr_proj.txt"


base_address = file.readlines(file(tempfile))
os.chdir(os.path.join(path,"/Trivim2/25/input"))

count = []
path= os.getcwd()
y = [os.curdir.count(path)]

print y

for i in 2..y.length:
	if(file is dir):
            a = (str(y[i])
                 for j in y
                          if(str(y[i])== "build#{j-1}")
##			    i = i+ 1

		
     
for i in range(count(y))
	h_file = base_address[0].to_s+"\\input\\build#{i}\\heights.txt"
	b_file = base_address[0].to_s+"\\input\\build#{i}\\build#{i}.txt"
	list = parameters_file(h_file,b_file)
	
	floors = list[2].to_i
	f = list[2] + 1                     #floor number
	x = list[2+f]
	y = list[3+f]
	ht = 0.0
	f = f.to_int
	list1 = [0.0,x,y]
	# Create a series of "points", each a 3-item array containing x, y, and z. # keep points in any one plane  # and pull along the plane whose coordinate is zero
	iterator = list[0].to_i
	for j in 1..iterator:
		temp = [list[2*j+1+f],list[2*j+f]]
		latlong = Geom.LatLong.new(temp)
		list[2*j+f] = latlong.to_utm.x
		list[1+2*j+f] = latlong.to_utm.y
	end
	for j in 1..floors:
		pic_address = base_address[0].to_s+"\\input\\build#{i}\\build#{i}_#{j}.jpg"
		if(file.exist(pic_address)):
			pic_address = base_address[0].to_s+"\\input\\build#{i}\\build#{i}_#{j}.png"
			if(file.exist(pic_address)):
				pic_address = base_address[0].to_s+"\\input\\build#{i}_#{j}.bmp"		### keep file format jpg or png or bmp onllyyy
			end
		end
		#UI.messagebox("list is")
		#UI.messagebox(list)
		model = drawBuilding(list,list[2+j],ht,f,pic_address)
		assignGeoData_shadow(model,list1)
		
		output_address = IO.readlines(drr+"/bin/curr_proj.txt")[0]+"/output/build"
		name = output_address+i.to_s+'_' + j.to_s + '.kmz'
		exportBuilding(model,name)
		#UI.messagebox("model is")
		#UI.messagebox(model)
		#exportBuilding(model,name)
		ht = ht + list[2+j]
##		Sketchup.active_model.entities.clear!
##		Sketchup.active_model.materials.remove "face-pic"
##	end
	temp_display_file.write("\ndone build#{i}......")

