from django import template

register = template.Library()

# now write a function, that will be our custom template filter.

def cut(value, arg):
	"""
	This cuts out all value of 'arg' from the string!

	"""
	return value.replace(arg,'')

register.filter('cut', cut)
    # second cut is function name therefore it is not a string, 
    # first one is what we want to call the filter (variable)