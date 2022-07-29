#!/usr/local/bin/python3
import sys

list=[1,2,3,4] #create iterator object
it = iter(list)

#for x in it:
#	print(x, end=" ")   #output the next element of the iterator

while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()