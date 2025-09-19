def _convert_valuetype(value_str:str):
	"""
	Helper function that will attempt to find and return the correct ValueType from a string.

	As I understand, helper functions are to be specific in scope. Is it overkill? 
	To be determined, but I got to prefix my function with underscore and that makes me feel smart. 
	"""
	# Integer?
	try:
		return int(value_str)
	except ValueError:
		pass

	# Float?
	try:
		return float(value_str)
	except ValueError:
		pass

	# Boolean?
	if value_str.lower() == 'true':
		return True
	if value_str.lower() == 'false':
		return False

	# JSON?
	# Try converting from JSON 
	# This could misinterpret simple [valid JSON] strings, so proceed with caution
	# However, I feel like it could be useful for structured data so I'm leaving here for now.
	#if (value_str.startswith('[') and value_str.endswith(']')) or \
	#	(value_str.startswith('{') and value_str.endswith('}')):
	#	try:
	#		return json.loads(value_str)
	#	except json.JSONDecodeError:
	#		pass

	# If all else fails, return a string that's totally "more better"
	return value_str
