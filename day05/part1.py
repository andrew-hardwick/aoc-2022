# part1.py


def parse_input(lines):
	lines = [line.replace('\n', '').replace('\r', '') for line in lines]

	split_index = next(i for i, v in enumerate(lines) if v == '')

	board_source = lines[:split_index - 1]
	instructions = lines[split_index + 1:]

	# parse board
	board_count = len(lines[split_index - 1].replace(' ', ''))

	required_width = board_count * 4 + 1
	board_source = [br.ljust(required_width) for br in board_source]

	board_source = list(reversed(board_source))

	board = []

	for i in range(board_count):
		board.append([])

	for board_row in board_source:
		parsed_row = [board_row[(i * 4) + 1] for i in range(board_count)]

		for i in range(board_count):
			if not parsed_row[i] == ' ':
				board[i].append(parsed_row[i])

	# parse instructions
	instructions = [i.replace('move ', '').replace('from ', '').replace('to ', '') for i in instructions]
	instructions = [[int(e) for e in i.split(' ')] for i in instructions]

	return board, instructions

def execute_instruction(board, instruction):
	count, source, dest = instruction

	for i in range(count):
		board[dest - 1].append(board[source - 1].pop())

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
