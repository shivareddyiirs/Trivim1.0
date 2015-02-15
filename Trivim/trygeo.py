import os
bundir = r"/Trivim2/cxexe/PointCloud/bundle"
f = os.listdir(bundir)
print f
for file in f:
    if file.endswith(".ply"):
        f= [(file)]
        print f
print "output"


for item in f:
    print [item]

CamCoords = str(item)
print CamCoords


