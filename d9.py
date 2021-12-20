import numpy as np


with open("input9.txt") as f:
    lines = f.read().split("\n")[:-1]
    # lines=np.fromstring(lines,dtype="int",sep=",") 

def string2list(s):
	return(list(map(int,list(s))))

dt=list(map(string2list,lines))
sp=np.asarray(dt).shape

low=[]
dt=np.asarray(dt)
print(dt)
for x,y in np.ndindex(sp):
	if [x,y] ==[0,0]:
		if dt[x,y]<dt[x+1,y] and dt[x,y]<dt[x,y+1]:
			low+=[dt[x,y]]
	elif [x,y] ==[0,100]:
		if dt[x,y]<dt[x+1,y] and dt[x,y]<dt[x,y-1]:
			low+=[dt[x,y]]
	elif [x,y] ==[100,0]:
		if dt[x,y]<dt[x-1,y] and dt[x,y]<dt[x,y+1]:
			low+=[dt[x,y]]
	elif [x,y] ==[100,100]:
		if dt[x,y]<dt[x-1,y] and dt[x,y]<dt[x,y-1]:
			low+=[dt[x,y]]
	elif x==0:
		if dt[x,y]<dt[x,y-1] and dt[x,y]<dt[x,y+1] and dt[x,y]<dt[x+1,y]:
			low+=[dt[x,y]]
	elif x==99:
		if dt[x,y]<dt[x,y-1] and dt[x,y]<dt[x,y+1] and dt[x,y]<dt[x-1,y]:
			low+=[dt[x,y]]
	elif y==0:
		if dt[x,y]<dt[x-1,y] and dt[x,y]<dt[x+1,y] and dt[x,y]<dt[x,y+1]:
			low+=[dt[x,y]]
	elif y==99:
		if dt[x,y]<dt[x-1,y] and dt[x,y]<dt[x+1,y] and dt[x,y]<dt[x,y-1]:
			low+=[dt[x,y]]
	else:
		if dt[x,y]<dt[x-1,y] and dt[x,y]<dt[x+1,y] and dt[x,y]<dt[x,y-1] and dt[x,y]<dt[x,y+1]:
			print(dt[x,y])
			low+=[dt[x,y]]
			
print(sum(low)+len(low))
print(low)



#print(np.fromstring(lines[1],dtype="int",sep=""))

