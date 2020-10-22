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

# Class Notes
memory = [
	1,
	1,
	1,
	2
]
running = True
count = 0

while running:
	index = memory[count]

	if index == 1:
		print("hi")
		count += 1

	elif index == 2:
		print("bye")
		running = False
		count += 1

def foobar(number):
	# if n divisible by 3 print "foo"
	# if n divisible by 5 print "bar"
	# if n divisible by 3 and 5 print "foobar"
	for n in range(0, number):
		if n % 3 == 0 and n % 5 == 0:
			print("foobar")
		elif n % 5 == 0:
			print("bar")
		elif n % 3 == 0:
			print("foo")
		else:
			print(n)

print(foobar(16))