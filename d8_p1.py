from d8_parse import input_parse

class HandheldGameConsole:
	def __init__(self, instructions):
		self.acc = 0
		self.next_instruction = 0
		self.instructions = instructions
	def execute(self):
		instruction = self.instructions[self.next_instruction]["instruction"]
		if instruction == "acc":
			self.acc += self.instructions[self.next_instruction]["value"]
			self.next_instruction +=  1
		elif instruction == "jmp":
			self.next_instruction += self.instructions[self.next_instruction]["value"]
		elif instruction == "nop":
			self.next_instruction += 1
		else:
			raise ValueError(f"{instruction} invalid instruction.")

instructions = input_parse()

for instruction in instructions:
	instruction["already"] = False
hgc = HandheldGameConsole(instructions)

while not hgc.instructions[hgc.next_instruction]["already"]:
	hgc.instructions[hgc.next_instruction]["already"] = True
	hgc.execute()

print(hgc.acc)