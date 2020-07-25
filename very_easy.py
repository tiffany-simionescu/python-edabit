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

# Concatenating Two Integer Lists
def concat(lst1, lst2):
		return lst1 + lst2

print(concat([1, 3, 5], [2, 6, 8])) # [1, 3, 5, 2, 6, 8]

# The Farm Problem
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs
def animals(chickens, cows, pigs):
		return (chickens * 2) + (cows * 4) + (pigs * 4)

print(animals(2, 3, 5)) # 36 legs

# Are the Numbers Equal?
def is_same_num(num1, num2):
		if num1 == num2:
				return True
		else:
				return False

print(is_same_num(4, 8)) # False
print(is_same_num(2, 2)) # True

# Maximum Difference
def difference(nums):
		return max(nums) - min(nums)

print(difference([10, 15, 20, 2, 10, 6])) # 20 - 2 = 18

# Find the Smallest Number in a List
def find_smallest_num(lst):
		return min(lst)

print(find_smallest_num([34, 15, 88, 2])) # 2

# Difference of Max and Min Numbers in List
def difference_max_min(lst):
		return max(lst) - min(lst)

print(difference_max_min([44, 32, 86, 19])) # 67

# Is the Number Less than or Equal to Zero?
def less_than_or_equal_to_zero(num):
		if num <= 0:
				return True
		return False

print(less_than_or_equal_to_zero(5)) # False
print(less_than_or_equal_to_zero(0)) # True
print(less_than_or_equal_to_zero(-2)) # True

# Squared
def squared(b):
		return b**2

print(squared(5)) # 25

# Football Points
# win = 3 points
# draw = 1 point
# loss = 0 points
def football_points(wins, draws, losses):
		return (wins * 3) + draws

print(football_points(3, 4, 2)) # 13

# Less than 100
def less_than_100(a, b):
		if a + b < 100:
				return True
		return False

print(less_than_100(22, 15)) # True
print(less_than_100(83, 34)) # False

# Get the Sum of All List Elements
def get_sum_of_elements(lst):
		sum = 0
		for elem in lst:
				sum += elem
		return sum

print(get_sum_of_elements([2, 7, 4])) # 13

# Multiple of 100
def divisible(num):
		if num % 100 == 0:
				return True
		return False

print(divisible(1)) # False
print(divisible(1000)) # True

# Is the String Empty?
def is_empty(s):
		if len(s) == 0:
				return True
		return False
		
print(is_empty("")) # True
print(is_empty(" ")) # False
print(is_empty("a")) # False