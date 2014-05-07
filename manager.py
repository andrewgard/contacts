#!/usr/bin/env python3

import helper as h
import sys

if(len(sys.argv) < 2):
	print("Need a contact book .yaml file")
	sys.exit()

data = h.load(sys.argv[1])
print(thebook)
