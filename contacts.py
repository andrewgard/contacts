
class Contact:

	def __init__(self, data):

	def __str__(self):
				
class Group:
	def __init__(self, name):
		self.name = name 
		self.members = [] 	
		

	def __str__(self):
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

		 	
		
class Book:

	def __init__(self, data, name):
		self.groups = []
		self.name = name
		self.contacts = []

	def __str__(self):
