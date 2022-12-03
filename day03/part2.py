# part2.py

from functools import partial, reduce


uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_group_indices(base_index):
	start = base_index * 3

	return start, start + 1, start + 2

def evaluate_group(source, group_indices):
	groups = [set(source[i]) for i in group_indices]

	intersection = list(reduce(lambda a,b: a & b, groups))[0]

	if intersection in uppers:
		# 'A' is 65 but we want it to be 27 so we subtract (65 - 27)->38
		priority = ord(intersection) - 38
	else:
		# 'a' is 97 but we want it to be 1 so we subtract (97 - 1)->96
		priority = ord(intersection) - 96

	return priority

def main(infn):
	with open(infn, 'r') as f:
		source = [str.strip(l) for l in f.readlines()]

	group_count = int(len(source) / 3)

	indices = (generate_group_indices(i) for i in range(group_count))

	func = partial(evaluate_group, source)

	priorities = [func(group_indices) for group_indices in indices]

	result = sum(priorities)

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
