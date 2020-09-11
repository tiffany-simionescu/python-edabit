# Drunken Python
def int_to_str(n):
	return int(n)

def str_to_int(s):
	return str(s)

# FizzBuzz
def fizz_buzz(num):
	if num % 3 == 0 and num % 5 == 0:
		return "FizzBuzz"
	elif num % 5 == 0:
		return "Buzz"
	elif num % 3 == 0:
		return "Fizz"
	else:
		return str(num)