import numpy as np


with open("input8.txt") as f:
    lines = f.read().split("\n")[:-1]
    # lines=np.fromstring(lines,dtype="int",sep=",") 

def extract_after(line):
	p=line.split("| ")
	return(p[1].split(" "))

def extract_before(line):
	p=line.split(" |")
	return(p[0].split(" "))


signals=np.concatenate(list(map(extract_after,lines))) 

digits=list(map(len,signals))




print(sum([ i in [2,4,3,7] for i in digits]))




############## for question 2

before=list(map(extract_before,lines))
after=list(map(extract_after,lines))


def find_digits(l):
	l_len=list(map(len,l))
	correct=[-1 for i in range(0,10)]
	
	correct[l_len.index(2)]=1
	correct[l_len.index(4)]=4
	correct[l_len.index(3)]=7
	correct[l_len.index(7)]=8

	# six has length 6 and has c, which is not in 1
	def find_six(l):
		for i in np.where(np.asarray(l_len))

	# five has length five and do not contrain c, the other missing letter is e





print(before[3])