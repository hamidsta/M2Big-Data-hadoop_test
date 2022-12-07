#!/usr/bin/env python
import sys

for line in sys.stdin:
	data = line.strip().split(",")
	print ("{0}\t{1}".format(data[2],1))
