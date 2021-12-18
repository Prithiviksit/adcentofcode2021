def MyMergeSort(l):
	n=len(l)
	if (n<=1):
		return(l)
	if n%2==0:
		m=int(n/2)
	else:
		m=int((n+1)/2)
	l2=MyMergeSort(l[0:m])+MyMergeSort(l[m:n])
	for j in range(m,n):
		for i in range(0,m):
			if l2[j]<l2[i]:
				l2[i],l2[j]=l2[j],l2[i]
	return(l2)


		
