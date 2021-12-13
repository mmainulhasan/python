def convert_to_celsius(fahrenheit):
	""" (number) -> float

	Return the number of Celsius degrees equivalent to fahrenheit degrees.

	>>> convert_to_celsius(75)
	23.888888889
	"""

	return (fahrenheit - 32.0) * 5.0 / 9.0


def above_freezing(celsius):
	""" (number) -> bool

	Return True iff temperature celsius degrees is above freezing.

	>>> above_freezing(5.2)
	True
	>>> above_freezing(-2)
	False
	"""

	return celsius > 0

print(__name__)

# __name__ this magic operator is helpful when we import a script in another script

if __name__ == '__main__':
	fahrenheit = float(input('Enter the temperature in degrees Fahrenheit: '))
	celsius = convert_to_celsius(fahrenheit)
	if above_freezing(celsius):
		print('It is above freezing.')
	else:
		print('It is below freezing.')