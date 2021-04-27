import magpylib as magpy
import numpy as np
from matplotlib import pyplot as plt
from magpylib import Collection, displaySystem

#define current and distance between two line
current = 20 #A
dist = 20 #mm

s1 = magpy.source.current.Line(curr=current, vertices=[(-dist/2,-50,0),(-dist/2,50,0)])
s2 = magpy.source.current.Line(curr=-current, vertices=[(dist/2,-50,0),(dist/2,50,0)])

# create collection
c = Collection(s1, s2)


# calculate B-field on a grid
xs = np.linspace(-100,100,33)
zs = np.linspace(-100,100,44)
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

print(c.getB([0,0,0]))

plt.show()
