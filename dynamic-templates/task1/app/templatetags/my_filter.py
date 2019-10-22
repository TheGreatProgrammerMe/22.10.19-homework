from django import template

register = template.Library()

@register.filter
def float_color(x):
	if x != '-':
		if float(x) < 0:
			value = 'green'
		elif (float(x) > 1 and float(x) <= 2):
			value = '#FFE4E1'
		elif (float(x) > 2 and float(x) <= 5):
			value = '#FFB6C1'
		elif float(x) > 5:
			value = 'red'
		else:
			value = 'white'
	else:
		value = 'white'
	return value