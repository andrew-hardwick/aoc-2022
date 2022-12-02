# part2.py


def parse_game(line):
	split = line.strip().split(' ')

	# 65 is 'A' and 88 is 'X'

	return ord(split[0]) - 65, ord(split[1]) - 88

def score_game(game):
	oc, unscored_result = game

	game_result = unscored_result * 3

	pc = (unscored_result + oc - 1) % 3 + 1

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
