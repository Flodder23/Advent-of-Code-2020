from d_08_parse import input_parse

class HandheldGameConsole:
	def __init__(self, instructions):
		self.acc = 0
		self.next_instruction = 0
		self.instructions = instructions
	
	def execute_instruction(self, instruction):
		if instruction["instruction"] == "acc":
			self.acc += instruction["value"]
			self.next_instruction +=  1
		elif instruction["instruction"] == "jmp":
			self.next_instruction += instruction["value"]
		elif instruction["instruction"] == "nop":
			self.next_instruction += 1
		else:
			raise ValueError(f"{instruction} invalid instruction.")
	
	def execute(self, every_loop=lambda self: self.acc, break_if=lambda self: False):
		while not break_if(self):
			every_loop(self)
			self.execute_instruction(self.instructions[self.next_instruction])

def mark_already(c):
	c.instructions[c.next_instruction]["already"] = True	

if __name__ == "__main__":
	hgc = HandheldGameConsole(input_parse())

	hgc.execute(
		every_loop = mark_already,
		break_if = lambda c: c.instructions[c.next_instruction]["already"]
	)

	print(hgc.acc)