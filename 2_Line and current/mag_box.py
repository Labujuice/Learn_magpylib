#Reference from here: https://magpylib.readthedocs.io/en/latest/_autogen/magpylib.source.current/
from magpylib import source

#模擬一條線流過十安培的電流
cd = source.current.Line(curr=10,vertices=[(2,0,0),(-2,0,0)])
B = cd.getB([0,0,2])
print(B)

##模擬一條圓圈有十安培電流經過
cd = source.current.Circular(curr=10,dim=2)
B = cd.getB([0,0,2])
print(B)




