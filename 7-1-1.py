# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:22:17 2023

@author: zxv95
"""


import numpy as np 

a=np.array([12,8,20,17,15])
print(a)
a.sort()
print(a)
#print(dir(a))
print(type(a))
a.shape
b=np.array([[12,3,4.0],[1,4,5]])
print(b.dtype)
print(a.dtype)  #캡쳐
b.ndim
b.shape 
c=np.array([[[1,3,0,1],[1,1,4,2],[3,3,4,1]],[[2,1,2,1],[1,0,1,0],[1,5,6,2]]])
print(c)
c.shape
d=np.zeros([2,3])
print(d)
print(d.dtype) #캡쳐
e=np.random.random([2,5])
print(e)
f=np.arange(1,20,2.5)
print(f)
x=10
y=12
print(x,y)
a=np.array([10,20,30,40])
b=a
b[0]=-10
print(a,b)
c=a.copy()
c[1]=-20
print(a,c)
a=np.array([1,2,3,4,5,6])
b=a.reshape([2,3])
print(a)
a[4]=-5
print(b)
a=np.array([[1,2,3],[4,5,6]])
b=a.T
print(b)
a=np.array([[3,2,-2,0,1],[2,-3,4,5,2],[0,1,-2,-3,2]])
print(a)
print(a.sum())
print(a.sum(axis=1))
print(a.cumsum(axis=0))
print(a.max(axis=1))  #캡처
print(a.argmax(axis=0))
positive=a>0
print(positive)
b=a[positive]
print(b)
b.sum()
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([[7,8,9],[1,4,7]])
x=np.vstack([a,b])
print(x)
y=np.vstack([a,c])
print(y)
z=np.hstack([a,b])
print(z)
#zz=np.hstack([a,c])  #에러뜨는 것 캡처
a=np.array([1,2,3,4,5])
b=np.array([0,-1,2,6,1])
c=np.array([np.pi/2,np.pi,np.pi*2])
print(c)
print(np.add(a,b))
print(np.log10(a))
print(np.greater(a,b))
print(np.maximum(a,b))
print(c.round(2))
a=np.array([[1,2,3,4],[0,1,2,3],[-1,0,1,2]])
b=np.array([[1,1,2,2]])
print(a+b)     #캡쳐