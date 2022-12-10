# part1.py


class machine_t():
	def __init__(self, instructions):
		self._instructions = instructions
		self._pc = 0
		self._reg_x = 1
		self._reg_x_waiting = 1
		self._prior_active = 0
		self._waiting = False
		self._scan_pos = 0

	def tick(self):
		if self._prior_active > 0:
			self._prior_active -= 1

		else:
			if self._waiting:
				self._reg_x = self._reg_x_waiting

			instr = self._instructions[self._pc]
			self._pc += 1

			self._handle_instruction(instr)

		return self._draw_pixel(), [self._reg_x]

	def _handle_instruction(self, instr):
		if instr[0] == 'noop':
			#print('noop')
			return

		if instr[0] == 'addx':
			#print(instr[0], instr[1])
			self._prior_active = 1
			self._waiting = True
			self._reg_x_waiting = self._reg_x +  int(instr[1])

	def _draw_pixel(self):
		min_sprite = self._reg_x - 1
		max_sprite = self._reg_x + 1

		self._scan_pos += 1

		return self._scan_pos, ((self._scan_pos - 1) % 40) in range(self._reg_x - 1, self._reg_x + 2)

	def unfinished(self):
		return self._pc < len(self._instructions) or self._prior_active > 0


def main(infn):
	with open(infn, 'r') as f:
		instructions = [l.strip().split(' ') for l in f.readlines()]

	machine = machine_t(instructions)

	count_interesting = [20 + (40 * i) for i in range(6)]

	result = 0

	while machine.unfinished():
		(count, pixel), registers = machine.tick()

		if count in count_interesting:

			result += count * registers[0]

	print(result)

if __name__ == '__main__':
	main('test1.txt')
	main('test2.txt')
	main('input.txt')
