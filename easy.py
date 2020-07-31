# Curzon Numbers
def is_curzon(num):
	part1 = 2**num + 1
	part2 = 2 * num + 1
	return part1 % part2 == 0

print(is_curzon(5)) # True
print(is_curzon(10)) # False

# Convert Number to String of Dashes
def num_to_dashes(num):
    if num > 0:
        dashes = "" 
        for _ in range(num):
            dashes += "-"
        return dashes

print(num_to_dashes(5)) # "-----"

# Is the Word Singular or Plural?
def is_plural(word):
	  return word[-1] == "s"

print(is_plural("changes")) # True
print(is_plural("change")) # False

# Check Equals
def check_equals(lst1, lst2):
    return lst1 == lst2

print(check_equals([1, 2], [1, 2])) # True
print(check_equals([1, 2], [1, 3])) # False

# Solve the Equation
def equation(s):
	  return eval(s)

print(equation("1+1")) # 2
print(equation("7*4-2")) # 26