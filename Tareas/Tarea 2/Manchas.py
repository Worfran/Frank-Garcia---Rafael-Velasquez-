from importlib.resources import path
import numpy as np 
import matplotlib.pyplot as plt
import Utilities.reader as reader

file="Data/manchas.dat"
url="https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionales/ManchasSolares.dat"
filtro=1900.


df=reader(file, url)

#masking
mask=df[:,0] >= filtro

df=df[mask]

#valor medio
mean=np.mean(df[:,2])
df[:,2]-=mean



