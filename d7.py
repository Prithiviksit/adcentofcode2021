from pipe import select, where
import numpy as np
import functools as ft
from collections import Counter

with open("input7.txt") as f:
    lines = f.read().replace("\n","")
    lines=np.fromstring(lines,dtype="int",sep=",") 



right_most=max(lines)

def cost(i):
	return(i*(i+1)/2)

def calc_moves (t):
	y=list(map(lambda x: cost(abs(x-t)),lines))
	return(sum(y))


min_moves=list(map(calc_moves,range(0,right_most+1)))


print(min(min_moves))
