# part2.py

from part1 import parse_input, determine_dir_total_size, filter_directories


def main(infn, disk_size, req_space):
	dir_contents, file_sizes, root = parse_input(infn)

	total_size, dir_and_file_sizes = determine_dir_total_size(dir_contents, file_sizes, root)

	dir_sizes = filter_directories(dir_and_file_sizes, file_sizes)

	min_del_size = dir_sizes['/'] - (disk_size - req_space)

	size_only = (s for s in list(sorted(dir_sizes.values())) if s > min_del_size)

	print(next(size_only))

if __name__ == '__main__':
	main('test1.txt', 70000000, 30000000)
	main('input.txt', 70000000, 30000000)
