import sys
import tomllib

def read_conf(config):
	try:
		with open(config, 'rb') as f:
			return tomllib.load(f)
	# add FileNotFound
	# add FilePermission

	except Exception as e:
		print(f"Error loading config: {e}")
		sys.exit(1)

