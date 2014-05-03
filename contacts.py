
class Contact:

	def __init__(self, data):
		self.first = data['first']
		self.last = data['last']
		self.home = data['home']
		self.work = data['work']
		self.cell = data['cell']
		self.group = []
		for group in data['group']:
			self.group.append(group)

	def __str__(self):
		return("{0}, {1}\n\tHome #: {2}\n\tWork #: {3}\n\tCell #: {4}".format(self.last, self.first, self.home, self.work, self.cell))

	def edit(self, param):
		new_str = input('New vlaue: ')
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

class Group:

	def __init__(self, name):
		self.name = name 
		self.members = [] 	
		

	def __str__(self):
		return self.name + "\nmembers: " + ", ".join(str(self.members[0]))		
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
		if(searchparam == 'last'):
			for contact in self.members:
				if(contact.last == val):
					result.append( contact )
			return result
		if(searchparam == 'home'):
			for contact in self.members:
				if(contact.home == val):
					result.append( contact )
			return result
		if(searchparam == 'work'):
			for contact in self.members:
				if(contact.work ==val):
					result.append( contact ) 
			return result
		if(searchparam == 'cell'):
			for contact in self.members:
				if(contact.cell == val):
					result.append( contact )
			return result
					
		 	
		

class Book:

	def __init__(self, data, name):
		self.groups = []
		self.name = name
		self.contacts = []

	def __str__(self):
		pass
