# part1.py


def parse_line(line):
	split = line.strip().split(' ')

	return split[0], int(split[1])

def model_rope_link_step(h_x, h_y, t_x, t_y):
	d_x = h_x - t_x
	d_y = h_y - t_y

	ns_x = int((d_x) / 2)
	ns_y = int((d_y) / 2)

	es_x = 0
	es_y = 0

	m_d_x = abs(d_x)
	m_d_y = abs(d_y)

	if m_d_x > 0 and m_d_y > 0:
		es_x = d_x if m_d_y > m_d_x else 0
		es_y = d_y if m_d_x > m_d_y else 0

	n_t_x = ns_x + es_x + t_x
	n_t_y = ns_y + es_y + t_y

	return n_t_x, n_t_y

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
	main('test1.txt', 2)
	main('input.txt', 2)
