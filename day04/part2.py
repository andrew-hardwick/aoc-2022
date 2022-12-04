# part2.py


def parse_line(line):
	split = [s.split('-') for s in line.split(',')]

	return ((int(s[0]), int(s[1])) for s in split)

def main(infn):
	with open(infn, 'r') as f:
		sections = (parse_line(l) for l in f.readlines())

	result = sum([(a[0] <= b[0] and a[1] >= b[0]) or (b[0] <= a[0] and b[1] >= a[0]) for a, b in sections])

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
