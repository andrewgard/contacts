import yaml
from contacts import book

def load(name):
	return yaml.load( open( name, 'r') )
