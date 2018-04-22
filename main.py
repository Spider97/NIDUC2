import numpy as np
from Controller import Controller
import random

frames=5
frame_size=8
one=0
myList=[]

c=Controller(frame_size,frames,myList)
c.generate()
c.display()
c.addParity()
print()
c.display()
c.BSC()
print()
c.display()

c.saw()




