# part1.py


uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def parse_line(line):
	line = line.strip()

	half_len = int(len(line) / 2)

	fh = set(line[:half_len])
	sh = set(line[half_len:])

	intersection = list(fh & sh)[0]

	if intersection in uppers:
		# 'A' is 65 but we want it to be 27 so we subtract (65 - 27)->38
		priority = ord(intersection) - 38
	else:
		# 'a' is 97 but we want it to be 1 so we subtract (97 - 1)->96
		priority = ord(intersection) - 96

	return priority

def main(infn):
	with open(infn, 'r') as f:
		priorities = [parse_line(l) for l in f.readlines()]

	result = sum(priorities)

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
