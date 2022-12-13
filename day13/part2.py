# part2.py

import functools
import json

from part1 import validate_pair


def compare_pair(a, b):
	return 1 if validate_pair(a, b)[0] else -1

def parse_input(infn):
	with open(infn, 'r') as f:
		packet_source = (str.strip(l) for l in f.readlines())

	packet_source = (p for p in packet_source if not p == '')

	return [json.loads(p) for p in packet_source]

def main(infn):
	packets = parse_input(infn)

	a = [[2]]
	b = [[6]]

	packets.append(a)
	packets.append(b)

	key_func = functools.cmp_to_key(compare_pair)

	sorted_packets = sorted(packets, key=key_func, reverse=True)

	a_i = sorted_packets.index(a) + 1
	a_b = sorted_packets.index(b) + 1

	print(a_i * a_b)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
