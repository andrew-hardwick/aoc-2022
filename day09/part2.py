# part2.py

from part1 import parse_line, simulate


def main(infn, rope_length):
	with open(infn, 'r') as f:
		moves = [parse_line(l) for l in f.readlines()]

	states = simulate(moves, rope_length)

	print(len(set(states)))

if __name__ == '__main__':
	main('test1.txt', 10)
	main('test2.txt', 10)
	main('input.txt', 10)
