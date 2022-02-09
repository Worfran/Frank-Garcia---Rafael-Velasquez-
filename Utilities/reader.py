import os.path as path
import wget
import numpy as np


def reader(file, url):
    if not path.exists(file):
        Path_ = wget.download(url,file)
    else:
        Path_ = file
    
    df=np.loadtxt(Path_)
    return df

print("hola mundo")