def minHeapify(A,i):
	limit = len(A)
	l = (i+1)*2-1
	r = l + 1
	if l<limit and A[i] > A[l]:
		minindex = l
	else:
		minindex = i
	if r<limit and A[minindex] > A[r]:
		minindex = r
	if minindex != i:
		tmp = A[i]
		A[i] = A[minindex]
		A[minindex] = tmp
		minHeapify(A,minindex)
	return 0
