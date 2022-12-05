# part2.py

from part1 import parse_input


def execute_instruction(board, instruction):
	count, source, dest = instruction

	crane = []

	for i in range(count):
		crane.append(board[source - 1].pop())

	for i in range(count):
		board[dest - 1].append(crane.pop())

def get_top_of_each_column_on_board(board):
	return ''.join([br.pop() for br in board])

def main(infn):
	with open(infn, 'r') as f:
		board, instructions = parse_input(f.readlines())

	for instruction in instructions:
		execute_instruction(board, instruction)

	result = get_top_of_each_column_on_board(board)

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
