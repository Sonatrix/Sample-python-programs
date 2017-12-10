def reverse(a,start,stop):
	if start>=stop:
		return a
	else:
		a[start],a[stop-1] = a[stop-1],a[start]
		reverse(a,start+1,stop-1)


if __name__ == '__main__':
	a =  reverse([3,7,198,32],0,3)
	print a

#print reverse([1,2,3,4],0,3)
