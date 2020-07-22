# How Edabit works
def hello():
	  return "hello edabit.com"

print(hello())

# Return the Sum of Two Numbers
def addition(a, b):
    return a + b

print(addition(3, 2))  # 5
print(addition(-3, -6))  # -9
print(addition(7, 3))  # 10

# Area of a Triangle
def tri_area(base, height):
    return (base * height) / 2

print(tri_area(3, 2)) # 3
print(tri_area(7, 4)) # 14
print(tri_area(10, 10)) # 50

# Convert Hours into Seconds
def how_many_seconds(hours):
		return hours * 3600

print(how_many_seconds(2))  # 7200
print(how_many_seconds(10))  # 36000
print(how_many_seconds(24))  # 86400

# Return the First Element in a List
def get_first_value(number_list):
	  return number_list[0]

print(get_first_value([1, 2, 3]))  # 1
print(get_first_value([80, 5, 100]))  # 80
print(get_first_value([-500, 0, 50]))  # -500

# Return the Remainder from Two Numbers
def remainder(x, y):
    return x % y

print(remainder(1, 3))  # 1
print(remainder(3, 4))  # 3
print(remainder(5, 5))  # 0
print(remainder(7, 2))  # 1

# String to Integer and Vice Versa
def to_int(txt):
	  return int(txt)

def to_str(num):
	  return str(num)

print(to_int("77"))  # 77
print(to_int("532")) # 532
print(to_str(77))  # "77"
print(to_str(532))  # "532"

# Convert Minutes into Seconds
def convert(minutes):
		return minutes * 60

print(convert(5)) # 300
print(convert(3)) # 180
print(convert(2)) # 120

# Return the Next Number from the Integer Passed
def addition2(num):
		return num + 1

print(addition2(0)) # 1
print(addition2(9)) # 10
print(addition2(-3)) # -2

# Find the Perimeter of a Rectangle
def find_perimeter(length, width):
		return 2 * (length + width)

print(find_perimeter(6, 7)) # 26
print(find_perimeter(20, 10)) # 60
print(find_perimeter(2, 9)) # 22

# To the Power of _____
def calculate_exponent(num, exp):
		return num**exp

print(calculate_exponent(5, 5)) # 3125
print(calculate_exponent(10, 10)) # 10000000000
print(calculate_exponent(3, 3)) # 27

