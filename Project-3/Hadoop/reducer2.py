#!/usr/bin/env python

import sys

AgeTotal=0
AvgAge = 0
num = 0;
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data)!=2:
		continue
        
	thisKey, thisValue = data
	if oldKey and oldKey != thisKey:
		AvgAge = AgeTotal/num
		print("{0}\t{1}".format(oldKey,AvgAge))
		AgeTotal=0
		num=0
	oldKey=thisKey
	AgeTotal+=float(thisValue)
	num +=1
if oldKey!=None:
	print(oldKey,"\t",AvgAge)
