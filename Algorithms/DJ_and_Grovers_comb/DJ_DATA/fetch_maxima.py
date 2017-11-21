import os
import numpy as np
folders = os.listdir()

for i in folders:
    try:
        os.chdir(i)
    except:
        continue

    for f in os.listdir():
        if f.endswith(".txt"):
            a= np.loadtxt(f)[-1]
            print(i,f)
            print(a)
            print(np.max(a))
    os.chdir("./../")
    