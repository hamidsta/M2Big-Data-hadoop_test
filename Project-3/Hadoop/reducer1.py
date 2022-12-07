#!/usr/bin/env python

import sys

DeathTotal=0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data)!=2:
		continue
        
	thisKey, thisValue = data
	if oldKey and oldKey != thisKey:
		print("{0}\t{1}".format(oldKey,DeathTotal))
		DeathTotal=0
	oldKey=thisKey
	DeathTotal+=float(thisValue)
if oldKey!=None:
	print(oldKey,"\t",DeathTotal)
