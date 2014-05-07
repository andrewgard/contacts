#!/usr/bin/env python3

import helper as h
import sys

def print_help():
	print("Commands:")
	print("\tadd contact <last name> <first name>\t\t\t\t-Add a new contact to the current contact book.")
	print("\tadd group <group name>\t\t\t\t\t\t-Add a new group to the current contact book.")
	print("\tprint [contact <last name> <first name> | group <name> | all]\t-Prints corresponding value.")
	print("\tsearch <first name> <last name> [group <name> | all]\t\t-Search a group or all contacts.")

if(len(sys.argv) < 2):
	print("Need a contact book .yaml file")
	sys.exit()

data = h.load(sys.argv[1])
thebook = h.Book(data, 'Book 1')
print(thebook)
print_help()

run = True

while(run):
	command_string = input('> ')
	args = command_string.split(' ')
	if(args[0] == 'add' and args[1] == 'contact'):
		
	elif(args[0] == 'add' and args[1] == 'group'):

	elif(args[0] == 'print' and args[1] == 'contact'):

	elif(args[0] == 'print' and args[1] == 'group'):

	elif(args[0] == 'print' and args[1] == 'all'):

	elif(args[0] == 'search' and arg[3] == 'group'):

	elif(args[0] == 'search' and arg[3] == 'all'):

	elif(args[0] == 'edit'):

	elif(args[0] == 'add_to_group'):

	else:
		print_help()
				
