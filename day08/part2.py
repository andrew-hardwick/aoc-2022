# part2.py

from part1 import print_map


def calculate_score_for_tree(forest_map, x, y, side):
	north = 1
	edge_i = side - 1

	if x == 0 or y == 0 or x == edge_i or y == edge_i:
		return 0

	deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	score = 1

	for d_x, d_y in deltas:
		dir_height = 0
		height = forest_map[y][x]
		dir_score = 0

		c_x = x + d_x
		c_y = y + d_y

		while dir_height < height and c_x >= 0 and c_y >= 0 and c_x <= edge_i and c_y <= edge_i:
			check_height = forest_map[c_y][c_x]
			if dir_height < check_height:
				dir_height = check_height

			dir_score += 1

			c_x += d_x
			c_y += d_y

		score *= dir_score

	return score

def calculate_scenic_score(forest_map):
	side = len(forest_map)

	assert(side == len(forest_map[0]))

	score_map = [[0 for _ in range(side)] for __ in range(side)]

	for x in range(side):
		for y in range(side):
			score_map[y][x] = calculate_score_for_tree(forest_map, x, y, side)

	return score_map

def main(infn):
	with open(infn, 'r') as f:
		forest_map = [[int(e) for e in str.strip(l)] for l in f.readlines()]

	score_map = calculate_scenic_score(forest_map)

	print(max(max(e) for e in score_map))

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
