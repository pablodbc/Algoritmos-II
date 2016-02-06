from math import*
from random import*
#Insertion sort
def insertionsort(A,p,r):
	print(p,r)
	for i in range(p+1,r+1):
		key = A[i]
		j = i-1
		while j>=p and A[j] > key:
			A[j+1] = A[j]
			j-=1
		A[j+1] = key
##########################################################################################################################################

#Heapsort
def maxHeapify(A, i, heapSize,p):
	left  = 2*i + 1-p
	right = 2*i + 2-p
	if left-p < heapSize and A[left] > A[i]:
		largest = left
	else:
		largest = i

	if right-p < heapSize and A[right] > A[largest]:
		largest = right

	if largest != i:
		A[largest], A[i] = A[i], A[largest]
		maxHeapify(A, largest, heapSize,p)
def buildMaxHeap(A, heapSize,p,r):
	for i in range(r-heapSize // 2, p-1, -1):
		maxHeapify(A, i, heapSize,p)
def heapsort(A,p,r):

	heapSize = r-p+1
	buildMaxHeap(A, heapSize,p,r)

	for i in range(p,r):
		A[p], A[p+heapSize -1] = A[p+heapSize - 1], A[p]
		heapSize -= 1
		maxHeapify(A, p, heapSize,p)
##########################################################################################################################################

#Hoare Partition
def Partition(A,p,r,x):
	i = p-1
	j = r+1
	while True:
		while True:
			j-=1
			if A[j]<=x: break
		while True:
			i+=1
			if A[i]>=x: break
		if i < j:
			A[i],A[j] = A[j],A[i]
		else:
			return j
##########################################################################################################################################
 
 #Median of 3
def median_of_three(a,b,c):
	B = [a,b,c]
	B.sort()
	return B[1]
##########################################################################################################################################

def quicksort(A,p,r):
	while r-p+1>15:
		m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
		if m-p >= r-m:
			quicksort(A,m,r)
			r = m
		else:
			quicksort(A,p,m)
			p = m
	insertionsort(A,p,r)
############################################################################################################################################
a = [randint(0,5000) for i in range(5000)]
quicksort(a,0,len(a)-1)