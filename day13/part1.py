# part1.py

import itertools


def parse_packet(packet_source):
	result =
	for c in packet_source:


def parse_input(infn):
	with open(infn, 'r') as f:
		packet_source = [str.strip(l) for l in f.readlines()]

	# split monke_source by blank lines
	packet_pairs = [list(y) for x, y in itertools.groupby(packet_source, lambda z: z == '') if not x]

	packet_pairs = [[parse_packet(p) for p in pair] for pair in packet_pairs]

	for pair in packet_pairs:
		print(pair[0])
		print(pair[1])
		print('\n\n')

def main(infn):
	packet_pairs = parse_input(infn)

if __name__ == '__main__':
	main('test1.txt')
