import yaml
from contacts import Book


def load(name):
	return yaml.load( open( name, 'r') )
