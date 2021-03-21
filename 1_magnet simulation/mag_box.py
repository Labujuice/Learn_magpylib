from magpylib.source.magnet import Box, Cylinder, Sphere

# Simuate a N38 5 * 5 *5 mm 
#https://www.leeyed.com/rare_earth_magnet.html
s_Box = Box(mag=(0,0,1220), dim=(5,5,5), pos=(0,0,-2.5))
s_Cylinder = Cylinder(mag=(0, 0, 1220), dim=(5, 5), pos=(0.0, 0.0, -2.5), angle=0.0, axis=(0.0, 0.0, 1.0), iterDia=50)
s_Sphere = Sphere(mag=(0.0, 0.0, 1220), dim=5.0, pos=(0.0, 0.0, -2.5), angle=0.0, axis=(0.0, 0.0, 1.0))

print(s_Box.getB([0,0,5]))
print(s_Cylinder.getB([0,0,5]))
print(s_Sphere.getB([0,0,5]))
