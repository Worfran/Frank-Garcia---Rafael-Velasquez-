
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as npl


class particle():

    def __init__(self, r,v, a,t, m,radius, Id, a=9.8):
        self.dt = t[1] - t[0] # creacion de atributo
        
        self.g=a
        self.x=r[0]
        self.y=r[1]
        self.vx =v[0]
        self.vy =v[1]
        self.a=a_0
        self.E=m*a*r[1]

        #self.rVector= np.zeros((len(t), len(x)))
        self.vVector= np.zeros((len(t), len(v_0)))
        self.aVector= np.zeros((len(t), len(a_0)))
        self.Evector=np.zeros((len(t), len()))

        self.m=m
        self.radius=radius
        self.Id=Id
    
    def colition(self):
        None

    def evolution(self):
        None
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