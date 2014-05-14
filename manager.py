#!/usr/bin/env python3
import helper as h
import sys
from contacts import Contact
from contacts import Group
from contacts import Book
def print_help():
	print("Commands:")
	print("add [contact <last name> <first name> | group <group name>]\t-Add a new contact or group to the current contact book.")
	print("print [contact <last name> <first name> | group <group name> | all]\t-Prints corresponding value or all contacts in the book.")
	print("search [last <last name> | first <first name> | home <phone #> | work <work #> | cell <cell #>]\t-Search a group or all contacts.")
	print("edit <first name> <last name> [set_first_name | set_last_name | set_home_phone | set_work_phone | set_cell_phone]\t-Edit correspondingfield.")
	print("add_to_group <last name> <first name> <group name>")
	print("quit\t-Exit the program")
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
thebook = Book(data, 'Book 1')



run = True

while(run):
	command_string = input('> ')
	args = command_string.split(' ')
	args.append("")
	if(args[0] == 'add' and args[1] == 'contact'):
		args[1] = args [2]
		args[0] = args [3]
		args[2] = input('home:')
		args[3] = input('work:')
		args[4] = input('cell:')
		args.append("")
		temp = Contact(args)
		thebook.add(temp)
		print(thebook)	

	elif(args[0] == 'add' and args[1] == 'group'):
		thebook.addGroup(args[2])
		print(thebook)

	elif(args[0] == 'print' and args[1] == 'contact'):
		temp = thebook.search('last', args[2])
		print(temp[0].print_details())		

	elif(args[0] == 'print' and args[1] == 'group'):
		group = thebook.findGroup(args[2])
		print(group)	
	
	elif(args[0] == 'print' and args[1] == 'all'):
		print(''.join([str(l) for l in thebook.contacts]))

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
	elif(args[0] == 'quit'):
		run = False
	else:
		print("Unrecognized command. Type 'help' for list of commands.")
				
