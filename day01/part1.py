# part1.py

import itertools

def parse_list(source):
	source = (int(i) if not i == '' else 0 for i in source)

	elves = itertools.groupby(source, key=lambda x: x == 0)
	elves = (list(e) for i, e in elves if not i)

	return elves

def main(infn):
	with open(infn, 'r') as f:
		lines = (str.strip(l) for l in f.readlines())

	data = parse_list(lines)

	totals = [sum(e) for e in data]
	result = max(totals)

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
