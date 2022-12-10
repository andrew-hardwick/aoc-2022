# part1.py

from part1 import machine_t


def main(infn):
	with open(infn, 'r') as f:
		instructions = [l.strip().split(' ') for l in f.readlines()]

	machine = machine_t(instructions)

	output_str = ''

	# formatting
	print('\n')

	while machine.unfinished():
		(count, pixel), registers = machine.tick()

		output_str += '#' if pixel else '.'

		if count % 40 == 0:
			print(output_str)
			output_str = ''

	# formatting
	print('\n')

if __name__ == '__main__':
	#main('test1.txt')
	main('test2.txt')
	main('input.txt')
