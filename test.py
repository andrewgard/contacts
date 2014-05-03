

from contacts import Contact
from contacts import Group

groups = ['This', 'That']
contact1info = {}
contact1info['first'] = 'Bob'
contact1info['last'] = 'Jenkins'
contact1info['home'] = '1234'
contact1info['work'] = '1234'
contact1info['cell'] = '1234'
contact1info['group'] = groups

groups = ['This']
contact2info = {}
contact2info['first'] = 'Andrew'
contact2info['last'] = 'Gardner'
contact2info['home'] = '4567'
contact2info['work'] = '4567'
contact2info['cell'] = '4567'
contact2info['group'] = groups

contact1 = Contact(contact1info)
contact2 = Contact(contact2info)

print(contact1)

print(contact2)


groupA = Group('theName')
groupA.add(contact1)
groupA.add(contact2)

exists = []
flag = 0
'''for group in contact1.group:
	for nonew in exists:
		if(group == nonew.name):
			flag = 1
			nonew.add(contact1)
	if(flag == 0):	
		exists.append(Group(group))'''

print (groupA) 
