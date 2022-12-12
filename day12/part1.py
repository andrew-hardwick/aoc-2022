# part1.py

import heapq


def parse_line(line):
	return [ord(c) - 96 for c in line]

def parse_input(infn, height_upper_limit):
	with open(infn, 'r') as f:
		height_map = [parse_line(str.strip(l)) for l in f.readlines()]

	dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	y_limit = len(height_map)
	x_limit = len(height_map[0])

	edges = []

	allowed_height_deltas = range(height_upper_limit)

	for y, row in enumerate(height_map):
		for x, e in enumerate(row):
			if e == -13: # 'S'
				start = (x, y)
				height_map[y][x] = 1
			elif e == -27: # 'E'
				end = (x, y)
				height_map[y][x] = 26

	for y, row in enumerate(height_map):
		for x, e in enumerate(row):
			for d_x, d_y in dirs:
				c_x = x + d_x
				c_y = y + d_y

				if c_x >= 0 and c_y >= 0 and c_x < x_limit and c_y < y_limit:
					height_diff = height_map[c_y][c_x] - e

					if height_diff < 0 or height_diff in allowed_height_deltas:
						edges.append(((x, y), (c_x, c_y)))

	edges = list(set(edges))

	vertices = list(set([a for e in edges for a in e]))

	edge_map = {}

	for v in vertices:
		edge_map[v] = [b for a, b in edges if a == v]

	return start, end, edge_map, vertices

def reconstruct_path(prev, end):
	current = end

	path = [current]

	while current in prev.keys():
		current = prev[current]
		path.append(current)

	return path

def find_shortest_path(start, end, edges, vertices):
	dist = {}
	dist[start] = 0

	prev = {}

	max_length = (len(vertices) + 1) ** 2

	unprocessed = []

	for v in vertices:
		if not v == start:
			dist[v] = max_length

		heapq.heappush(unprocessed, (dist[v], v))

	while len(unprocessed) > 0:
		_, u = heapq.heappop(unprocessed)

		if u == end:
			return reconstruct_path(prev, u)

		for v in edges[u]:
			alt = dist[u] + 1

			if alt < dist[v]:
				dist[v] = alt
				prev[v] = u

				# remove and readd to heap
				unprocessed = [(d, unp) for d, unp in unprocessed if not unp == v]
				heapq.heapify(unprocessed)
				heapq.heappush(unprocessed, (alt, v))

	return vertices

def main(infn):
	start, end, edges, vertices = parse_input(infn, 2)

	shortest_path = find_shortest_path(start, end, edges, vertices)

	print(len(shortest_path) - 1)

if __name__ == '__main__':
	main('test1.txt')
	main('input.txt')
