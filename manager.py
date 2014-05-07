#!/usr/bin/env python3

import helper as h
import sys

def print_help():
	print("Commands:")
	print("add [contact <last name> <first name> | group <group name>]\t-Add a new contact or group to the current contact book.")
	print("print [contact <last name> <first name> | group <group name> | all]\t-Prints corresponding value.")
	print("search [last <last name> | first <first name> | etc.]\t-Search a group or all contacts.")
	print("edit <first name> <last name> [set_first_name | last | home | work | cell | address]")
	print("add_to_group <last name> <first name> <group name>")
	print("help\t-prints this message")

def get_contact(last):
	cont = thebook.search('last', last)
	if(len(cont) == 0):
		print("No contact with last name '{0}' found".format(last))
		return None
	else:
		return(cont[0])

if(len(sys.argv) < 2):
	print("Need a contact book .yaml file")
	sys.exit()

data = h.load(sys.argv[1])
thebook = h.Book(data, 'Book 1')

run = True

while(run):
	command_string = input('> ')
	args = command_string.split(' ')
	args.append("")

	if(args[0] == 'add' and args[1] == 'contact'):

	elif(args[0] == 'add' and args[1] == 'group'):

	elif(args[0] == 'print' and args[1] == 'contact'):

	elif(args[0] == 'print' and args[1] == 'group'):

	elif(args[0] == 'print' and args[1] == 'all'):

	elif(args[0] == 'search'):
		if(len(args) < 3):
			print("Not eneough arguments")
		else:
			param = args[1]
			value = args[2]
			conts = thebook.search(param, value)
		if(len(conts) == 0):
			print("No results")
		else:
			for cont in conts:
				print(cont.print_details())

	elif(args[0] == 'edit'):
		last = args[1]
		param = args[3]
		cont = get_contact(last)
		if(cont != None):
			cont.edit(param)
			print(cont.print_details())

	elif(args[0] == 'add_to_group'):
		last = args[1]
		gname = args[3]
		found = False
		cont = get_contact(last)
		for group in thebook.groups:
			if(group.name == gname and cont != None):
				group.add(cont)
				found = True
				break
		if(found == False):
			print("Group with name '{0}' not found".format(gname, last))

	elif(args[0] == 'help'):
		print_help()
	else:
		print("Unrecognized command. Type 'help' for list of commands.")
				
