
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

class Group:

	def __init__(self, name):
		self.name = name
		self.contacts = []

	def __str__(self):
		#todo
		pass

class Book:

	def __init__(self, data, name):
		self.groups = []
		self.name = name
		self.contacts = []

	def __str__(self):
		#todo
		pass