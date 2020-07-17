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