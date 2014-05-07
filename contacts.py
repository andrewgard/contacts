
class Contact:

	def __init__(self, data):
		if(type(data) is dict):
			self.first = data['first']
			self.last = data['last']
			self.home = data['home']
			self.work = data['work']
			self.cell = data['cell']
			self.group = []
			for group in data['group']:
				self.group.append(group)
		else:
			self.first = data[0]
			self.last = data[1]
			self.home = data[2]
			self.work = data[3]
			self.cell = data[4]
			self.group = []
			for item in data[5]:
				self.group.append(item)

	def __str__(self):
		return ("{0}, {1}\n".format( self.last, self.first))

	def print_details(self):
		return("{0}, {1}\n\tHome #: {2}\n\tWork #: {3}\n\tCell #: {4}\n\tGroups: {5}".format(self.last, self.first, self.home, self.work, self.cell, ", ".join(self.group)))

	def edit(self, param):
		new_str = input('New value: ')
		action = getattr(self, param)
		action(new_str)

	def set_first_name(self, new_str):
		self.first = new_str

	def set_last_name(self, new_str):
		self.last = new_str

	def set_home_phone(self, new_str):
		self.home = new_str

	def set_work_phone(self, new_str):
		self.work = new_str

	def set_cell_phone(self, new_str):
		self.cell = new_str
	def add_to_group(self, new_str):
		self.group.append(new_str)

class Group:

	def __init__(self, name):
		self.name = name 
		self.members = [] 	
		

	def __str__(self):
		return self.name + '\n' + ''.join(str(contact) for contact in self.members)		

	def add(self, contact):
		self.members.append(contact)

	def remove(self, firstname, lastname):
		for contact in self.members:
			if (contact.first == firstname and contact.last == lastname):
				self.members.remove(contact)
	
	def search(self, searchparam, val):
		result = []
		if(searchparam == 'first'):
			for contact in self.members:
				if(contact.first == val):
					result.append( contact )
			return result
		else if(searchparam == 'last'):
			for contact in self.members:
				if(contact.last == val):
					result.append( contact )
			return result
		else if(searchparam == 'home'):
			for contact in self.members:
				if(contact.home == val):
					result.append( contact )
			return result
		else if(searchparam == 'work'):
			for contact in self.members:
				if(contact.work ==val):
					result.append( contact ) 
			return result
		else if(searchparam == 'cell'):
			for contact in self.members:
				if(contact.cell == val):
					result.append( contact )
			return result

class Book:

	def __init__(self, data, name):
		self.groups = []
		self.name = name
		self.contacts = []

		for key in data:
			self.contacts.append(Contact(data[key]))

		for cont in self.contacts:
			for group in cont.group:
				if(group_exists(name, match)):
					match.add(cont)
				else:
					temp = Group(name)
					temp.add(name)
					self.groups.append(temp)

	def __str__(self):
		return ("".join(str(self.groups)))

	def group_exists(self, name, match):
		exists = False
		for group in self.groups:
			if(group.name == name):
				match = group
				exists = True
				break
		return exists
		
