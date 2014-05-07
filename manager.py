#!/usr/bin/env python3

import helper as h
import sys

def print_help():
	print("Commands:")
	print("add [contact <last name> <first name> | group <group name>]\t-Add a new contact or group to the current contact book.")
	print("print [contact <last name> <first name> | group <group name> | all]\t-Prints corresponding value.")
	print("search <last name> <first name> [group <group name> | all]\t-Search a group or all contacts.")
	print("edit <first name> <last name> [first | last | home | work | cell | address]")
	print("add_to_group <last name> <first name> <group name>")
	print("help\t-prints this message")

if(len(sys.argv) < 2):
	print("Need a contact book .yaml file")
	sys.exit()

data = h.load(sys.argv[1])
thebook = h.Book(data, 'Book 1')
print_help()
