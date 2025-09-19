def list_keys(table: dict, name: str = None, debug: bool = None):
"""Reads dictionary as input and provides list of 
"""

	subtable_names = []

	if any(isinstance(value, dict) for value in table.values()):	# If any value returned is a dictionary, return true
		subtable_names.append(value)

		if debug is not None:
			if name is not None:
				print ("Sub-tables for ", name, ":")
			else:
				print ("Sub-tables found:")

			# Print all keys in the initial dictionary
			for key in table:
				print (key)

			# Print sub-tables for any identified nested dictionaries 
			for key in value:
				print (key)

		return subtable_names
