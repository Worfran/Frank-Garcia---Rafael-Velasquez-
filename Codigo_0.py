
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as npl


class particle():
    def __init__(self,x_0,v_0, a_0,t, m, radius, Id):
        self.dt = t[1] - t[0] # creacion de atributo
        
        self.r=x_0
        self.v =v_0
        self.a=a_0

        self.rVector= np.zeros((len(t), len(x_0)))
        self.vVector= np.zeros((len(t), len(v_0)))
        self.aVector= np.zeros((len(t), len(a_0)))

        self.m=m
        self.radius=radius
        self.Id=Id


dt=0.01
tmax=10
t=np.arange(0,tmax+dt,dt)


x_0=np.array([0.])
v_0=np.array([20.])
a_0=np.array([2.])

p=particle(x_0,v_0,a_0,t,1,1,1)

print(p.radius)

p.radius=10
print(p.radius)