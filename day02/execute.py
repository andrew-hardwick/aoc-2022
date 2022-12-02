# part1.py


def parse_table_entry(line):
	split = line.strip().split(',')

	return split[0], int(split[1])

def main(lkpfn, infn):
	with open(lkpfn, 'r') as f:
		lookup = dict([parse_table_entry(l) for l in f.readlines()])

	with open(infn, 'r') as f:
		games = [str.strip(l) for l in f.readlines()]

	result = sum([lookup[g] for g in games])

	print(result)

if __name__ == '__main__':
	main('part_1_lookup', 'test1.txt')
	main('part_2_lookup', 'test1.txt')
	#main('part_1_lookup', 'test2.txt')
	#main('part_2_lookup', 'test2.txt')
	main('part_1_lookup', 'input.txt')
	main('part_2_lookup', 'input.txt')
