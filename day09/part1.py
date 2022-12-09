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

def simulate(moves):
	h_x = 0
	h_y = 0
	t_x = 0
	t_y = 0

	tail_pos_history = [(t_x, t_y)]

	dirs = {'R': (1, 0), 'L':(-1, 0), 'U': (0, 1), 'D': (0, -1)}

	for direction, distance in moves:
		d_x, d_y = dirs[direction]

		for u in range(distance):
			h_x = h_x + d_x
			h_y = h_y + d_y

			t_x, t_y = model_rope_link_step(h_x, h_y, t_x, t_y)

			tail_pos_history.append((t_x, t_y))

	return tail_pos_history

def main(infn):
	with open(infn, 'r') as f:
		moves = [parse_line(l) for l in f.readlines()]

	states = simulate(moves)

	print(len(set(states)))

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
