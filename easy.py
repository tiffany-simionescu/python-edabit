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

