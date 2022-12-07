# part1.py


def find_first_unique_set(data, window_length):
	for w_s in range(len(data) - (window_length - 1)):
		if len(set(data[w_s:w_s + window_length])) == window_length:
			return w_s + window_length

	return -1

def main(infn, window_length):
	with open(infn, 'r') as f:
		data = str.strip(f.readline())

	result = find_first_unique_set(data, window_length)

	print(result)

if __name__ == '__main__':
	main('test1.txt', 4)
	main('test2.txt', 4)
	main('input.txt', 4)
