# Curzon Numbers
def is_curzon(num):
	part1 = 2**num + 1
	part2 = 2 * num + 1
	return part1 % part2 == 0

print(is_curzon(5)) # True
print(is_curzon(10)) # False

