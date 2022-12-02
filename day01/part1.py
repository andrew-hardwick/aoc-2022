# part1.py


def parse_list(source):
	result = {}
	index = 0
	result[0] = []

	for line in source:
		if line == '':
			index += 1
			result[index] = []
		else:
			result[index].append(int(line))

	return result

def main(infn):
	with open(infn, 'r') as f:
		lines = [str.strip(l) for l in f.readlines()]

	data = parse_list(lines)

	totals = [sum(data[e]) for e in data]
	result = max(totals)

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
