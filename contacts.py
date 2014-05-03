
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
<<<<<<< HEAD
				
class Group:
=======
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

>>>>>>> 2a223d14b09b667634d4e2a3b53a8dea9c6044fb
	def __init__(self, name):
		self.name = name 
		self.members = [] 	
		

	def __str__(self):
<<<<<<< HEAD
		return self.name + "\nmembers: " + ", ".join(self.members)		

	def add(self, contact):
		self.members.append(contact)

	def remove(self, firstname, lastname):
		for contact in self.members:
			if (contact.first == firstname && contact.last == lastname):
				self.members.remove(contact)
	
	def search(self, searchparam, val):
		if(searchparam == 'first'):
			for contact in self.members:
				if(contact.first == val):
					return contact

		 	
		
=======
		#todo
		pass

>>>>>>> 2a223d14b09b667634d4e2a3b53a8dea9c6044fb
class Book:

	def __init__(self, data, name):
		self.groups = []
		self.name = name
		self.contacts = []

	def __str__(self):
<<<<<<< HEAD
=======
		#todo
		pass
>>>>>>> 2a223d14b09b667634d4e2a3b53a8dea9c6044fb
