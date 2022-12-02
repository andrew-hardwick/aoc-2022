# part1.py


def parse_game(line):
	split = line.strip().split(' ')

	# 65 is 'A' and 88 is 'X'
	# using 87 to get the RPS offset of the player to 1
	# need 1-based instead of 0-based to make the math
	# work out in scoring

	return ord(split[0]) - 65, ord(split[1]) - 87

def score_game(game):
	oc, pc = game

	game_result = 3 * (((pc - oc) + 3) % 3)

	return pc + game_result

def main(infn):
	with open(infn, 'r') as f:
		games = [parse_game(l) for l in f.readlines()]

	result = sum([score_game(g) for g in games])

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	#main('test2.txt')
	main('input.txt')
