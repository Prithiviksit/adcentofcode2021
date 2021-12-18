from pipe import select, where
import numpy as np
import functools as ft

with open("input5.txt") as f:
    lines = f.read().split("\n") 
#    move = list(map(int,lines.split('\n\n')[0].split(",")))
#    board = lines.split('\n\n')[1:]


def extract_position(x):
	x=list(map(lambda v: np.fromstring(v,dtype=int,sep=","),x.split(" -> ")) )
	return(x)




lines=list(map(extract_position,lines))
lines.pop(-1)


## find the maximum position
pos_max=max(np.concatenate(np.concatenate(lines)))
board=np.zeros((pos_max+1,pos_max+1),dtype=int)


def draw_lines(v):
	x1,y1=v[0]
	x2,y2=v[1]
	if x1==x2:
		for j in range(min(y1,y2),max(y1,y2)+1):
			board[x1,j]+=1
	if y1==y2:
		for j in range(min(x1,x2),max(x1,x2)+1):
			board[j,y1]+=1
	if y2-y1==x2-x1 and x2>x1:
		for j in range(0,x2-x1+1):
			board[x1+j,y1+j]+=1
	if y2-y1==x2-x1 and x2<x1:
		for j in range(0,x1-x2+1):
			board[x2+j,y2+j]+=1	
	if y2-y1==x1-x2 and x2>x1:
		for j in range(0,x2-x1+1):
			board[x1+j,y1-j]+=1
	if y2-y1==x1-x2 and x2<x1:
		for j in range(0,x1-x2+1):
			board[x2+j,y2-j]+=1

result=list(map(draw_lines,lines))




print(sum(sum(board>=2)))
