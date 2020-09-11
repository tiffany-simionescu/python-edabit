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

# Characters in Shapes
def count_characters(lst):
	if lst is "" or None:
		return 0
	
	count = 0
	for i in lst:
		count += len(i)
	
	return count
    
print(count_characters([
  "###",
  "###",
  "###"
])) # 9

# Where's Bob?
def find_bob(names):
	if "Bob" in names:
		return names.index("Bob")
	else:
		return -1
        
print(find_bob(["Jimmy", "Layla", "Bob"])) # 2


# Frames Per Second
def frames(minutes, fps):
	return minutes * 60 * fps

print(frames(10, 1)) # 600

# Retrn Something to Me!
def give_me_something(a):
	return "something " + a

print(give_me_something("is better than nothing")) # "something is better than nothing"

# Is Last Character N?
def is_last_character_n(word):
	return word[-1] == "n"

# Evaluate an expression
def eq(evaluate):
	return eval(evaluate)

# Long Burp
def long_burp(num):
	return "Bu" + ("r" * num) + "p"

# Flip the Boolean
def flip_bool(b):
	if b:
		return 0
	return 1

