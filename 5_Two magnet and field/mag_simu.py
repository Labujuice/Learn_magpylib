import numpy as np
import matplotlib.pyplot as plt
from magpylib.source.magnet import Box,Cylinder
from magpylib import Collection, displaySystem

#distance between magnets
dis = 10

# magnet size and field
mag_size_x = 1
mag_size_y = 4
mag_size_z = 2

mag_field_x = 1300
mag_field_y = 0
mag_field_z = 0

pos_x = (dis + mag_size_x/2*2)/2
pos_z = - mag_size_z/2

# create magnets
sL = Box(mag=(mag_field_x,mag_field_y,mag_field_z), dim=(mag_size_x,mag_size_y,mag_size_z), pos=(-pos_x,0,pos_z))
sL_1 = Box(mag=(mag_field_x,mag_field_y,mag_field_z), dim=(mag_size_x,mag_size_y,mag_size_z), pos=(-pos_x,0,pos_z))
sL_2 = Box(mag=(mag_field_x,mag_field_y,mag_field_z), dim=(mag_size_x,mag_size_y,mag_size_z), pos=(-pos_x,0,pos_z))
sR = Box(mag=(mag_field_x,mag_field_y,mag_field_z), dim=(mag_size_x,mag_size_y,mag_size_z), pos=(pos_x,0,pos_z))
sR_1 = Box(mag=(mag_field_x,mag_field_y,mag_field_z), dim=(mag_size_x,mag_size_y,mag_size_z), pos=(pos_x,0,pos_z))
sR_2 = Box(mag=(mag_field_x,mag_field_y,mag_field_z), dim=(mag_size_x,mag_size_y,mag_size_z), pos=(pos_x,0,pos_z))

#move copy bos
sL_1.move((-mag_size_x,0,0))
sR_1.move((mag_size_x,0,0))
sL_2.move((-2*mag_size_x,0,0))
sR_2.move((2*mag_size_x,0,0))

# create collection
c = Collection(sL,sL_1,sL_2,sR,sR_1,sR_2)

# calculate B-field on a grid
xs = np.linspace(-10,10,33)
zs = np.linspace(-10,10,44)
POS = np.array([(x,0,z) for z in zs for x in xs])
Bs = c.getB(POS).reshape(44,33,3)     #<--VECTORIZED

# create figure
fig = plt.figure(figsize=(9,5))
ax1 = fig.add_subplot(121, projection='3d')  # 3D-axis
ax2 = fig.add_subplot(122)                   # 2D-axis

# display system geometry on ax1
displaySystem(c, subplotAx=ax1, suppress=True)

# display field in xz-plane using matplotlib
X,Z = np.meshgrid(xs,zs)
U,V = Bs[:,:,0], Bs[:,:,2]
ax2.streamplot(X, Z, U, V, color=np.log(U**2+V**2))

print(c.getB([0,0,2]))

plt.show()
