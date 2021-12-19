import numpy as np
import functools as ft
from collections import Counter

with open("input6.txt") as f:
    lines = f.read().replace("\n","")
    lines=np.fromstring(lines,dtype="int",sep=",") 


lines=dict(Counter(lines))

def add_zero(dic):
	dic2={}
	for i in range(0,9):
		if i not in dic:
			dic2[i]=0
		else:
			dic2[i]=dic[i]
	return(dic2)


number=list(add_zero(lines).values())

def one_day(v):
	v2=v[1:]+v[:1]
	v2[6]+=v[0]
	return(v2)




for i in range(0,256):
	number=one_day(number)





print(sum(number))
print(number)