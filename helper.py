import yaml

def load(name):
	return yaml.load( open( name, 'r') )
