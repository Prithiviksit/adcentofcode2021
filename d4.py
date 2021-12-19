from pipe import select, where
import numpy as np
import functools as ft

with open("input4.txt") as f:
    lines = f.read() 
    move = list(map(int,lines.split('\n\n')[0].split(",")))
    board = lines.split('\n\n')[1:]

def string_to_matrix(m):
	if m[-1]=="\n":
		m=m[0:-1]
	m=np.asmatrix(m.replace("\n",";"))
	return(m)

board=list(map(string_to_matrix,board))

state=[np.zeros((5,5),dtype=int) for i in range(0,len(board))]

def check_bingo (m):
	m=np.asarray(m)
	l=np.concatenate((m,m.transpose(),[np.diag(m)],[np.diag(np.fliplr(m))]))
	# bingo=list(l
	# 	|select(lambda v:ft.reduce(lambda x,y:x*y,v))
	# 	|lambda x,y: x|y
	# 	)
	bingo=ft.reduce(lambda x,y: x|y,map(lambda v:ft.reduce(lambda x,y:x*y,v),l))
	return(bingo)


def find_matching(m,s,v):
	x=np.where(m==v)
	if(len(x)>0):
		s[x]=1
	return(s)


def match_through(key):
	return(list(map(ft.partial(find_matching,v=key),board,state)))


for key in move:
	bingo0=list(map(check_bingo,state))

	state=match_through(key)
	bingo=list(map(check_bingo,state))
	if sum(bingo)-sum(bingo0)==1 and sum(map(lambda x:1-x,bingo))==0:
		break

print(key)

lastwinner=bingo0.index(0)
notcircled=np.where(state[lastwinner]==0)
print(sum(np.asarray(board[lastwinner][notcircled])[0]))




