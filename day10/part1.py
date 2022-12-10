# part1.py

class machine_t():
	def __init__(self, instructions):
		self._instructions = instructions
		self._pc = 0
		self._reg_x = 1
		self._prior_active = 0

	def tick(self):
		if self._prior_active > 0:
			self._prior_active -= 1
			#print('waiting')
			return

		instr = self._instructions[self._pc]
		self._pc += 1

		if instr[0] == 'noop':
			#print('noop')
			return

		if instr[0] == 'addx':
			#print('starting add instruction')
			self._prior_active = 1
			self._reg_x += int(instr[1])

	def unfinished(self):
		return self._pc < len(self._instructions) or self._prior_active > 0

	def get_registers(self):
		return [self._reg_x]


def main(infn):
	with open(infn, 'r') as f:
		instructions = [l.strip().split(' ') for l in f.readlines()]

	machine = machine_t(instructions)

	count = 0

	while machine.unfinished():
		machine.tick()

		count += 1
		if count % 20 == 0:
			print(count, machine.get_registers())



if __name__ == '__main__':
	main('test1.txt')
	main('test2.txt')
