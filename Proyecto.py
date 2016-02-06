from math import*
from random import*
#estaOrdenado
def esta_ordenado(a):
	k = all(a[i]<=a[i+1] for i in range(len(a)-1))
	if k: print("Esta ordenado")
	else: print("Jodete")
##########################################################################################################################################

#Insertion sort
def insertionsort(A,p,r):
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

#Median-of-Three Quicksort
def quicksort(A,p,r):
	quicksort_loop(A,p,r)
	insertionsort(A,p,r)
def quicksort_loop(A,p,r):
	while r-p+1>15:
		m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
		if m-p >= r-m:
			quicksort_loop(A,m,r)
			r = m
		else:
			quicksort_loop(A,p,m)
			p = m+1
############################################################################################################################################

#Introsort
def introsort(A,p,r):
	introsort_loop(A,p,r,2*int(log(len(a),2)))
	insertionsort(A,p,r)
def introsort_loop(A,p,r,limit):
	while r-p+1>15:
		if limit == 0:
			print("comenzando heapsort para",p,"y",r)
			heapsort(A,p,r)
			return 
		else:
			limit-=1
			m = Partition(A,p,r,median_of_three(A[p],A[r],A[(p+r)//2]))
			introsort_loop(A,m,r,limit)
			r = m
############################################################################################################################################

a = [0+(1 if i%2 else 0) for i in range(40000000)]
introsort(a,0,len(a)-1)
esta_ordenado(a)