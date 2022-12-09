# part2.py

from part1 import parse_line, model_rope_link_step


def model_full_rope_step(rope, rope_length):
	for i in range(rope_length - 1):
		h_x, h_y = rope[i]
		t_x, t_y = rope[i + 1]

		rope[i + 1] = model_rope_link_step(h_x, h_y, t_x, t_y)

def simulate(moves, rope_length):
	rope = [(0, 0) for _ in range(rope_length)]

	tail_pos_history = [(0, 0)]

	dirs = {'R': (1, 0), 'L':(-1, 0), 'U': (0, 1), 'D': (0, -1)}

	for direction, distance in moves:
		d_x, d_y = dirs[direction]

		for u in range(distance):
			h_x, h_y = rope[0]

			n_h_x = h_x + d_x
			n_h_y = h_y + d_y

			rope[0] = (n_h_x, n_h_y)

			model_full_rope_step(rope, rope_length)

			tail_pos_history.append(rope[-1])

	return tail_pos_history

def main(infn, rope_length):
	with open(infn, 'r') as f:
		moves = [parse_line(l) for l in f.readlines()]

	states = simulate(moves, rope_length)

	print(len(set(states)))

if __name__ == '__main__':
	main('test1.txt', 10)
	main('test2.txt', 10)
	main('input.txt', 10)
