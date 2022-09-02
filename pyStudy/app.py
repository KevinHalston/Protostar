import numpy as np
import sys

with open("D:\Python\pyStudy\dawn2.txt") as f:
    lines = f.read().split('\n')
dim = len(lines[0])

conv = {'.': 0,'_': 1,'\\': 2, '-': 3, '/': 4, '|': 5, '*': 6}
matrix = np.array([[conv[y] for y in x] for x in lines])
matrix -= 2  
grow = np.tile(np.arange(dim-1, -1, -1), (dim, 1))
grow[matrix <= 0] = 0  
matrix += grow
print("Flag: " + str((matrix >= 6).sum()))