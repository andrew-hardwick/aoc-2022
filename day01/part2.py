# part2.py

import itertools

from part1 import parse_list


def main(infn):
	with open(infn, 'r') as f:
		lines = (str.strip(l) for l in f.readlines())

	data = parse_list(lines)

	totals = sorted([sum(e) for e in data], reverse=True)

	result = sum(totals[:3])

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
