# part1.py

import itertools
import json


def validate_pair(a, b):
	if type(a) == int and type(b) == int:
		return a < b, a == b

	elif type(a) == list and type(b) == list:
		result = False, True

		index = 0
		while(result[0] == False and result[1] == True):
			if index >= len(b) and index >= len(a):
				return False, True
			elif index >= len(b):
				return False, False
			elif index >= len(a):
				return True, False

			result = validate_pair(a[index], b[index])
			index += 1

		return result
	elif type(a) == list and type(b) == int:
		return validate_pair(a, [b])

	elif type(a) == int and type(b) == list:
		return validate_pair([a], b)

	# unreachable
	return False, False

def parse_input(infn):
	with open(infn, 'r') as f:
		packet_source = (str.strip(l) for l in f.readlines())

	packet_pairs = (list(y) for x, y in itertools.groupby(packet_source, lambda z: z == '') if not x)

	return (tuple([json.loads(p) for p in pair]) for pair in packet_pairs)

def main(infn):
	packet_pairs = parse_input(infn)

	valid = ((i + 1, validate_pair(a, b)[0]) for i, (a, b) in enumerate(packet_pairs))

	valid_indices = (i for i, v in valid if v)

	print(sum(valid_indices))

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
