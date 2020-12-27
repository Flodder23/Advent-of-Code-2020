from d_08_parse import input_parse
from d_08_p1 import HandheldGameConsole, mark_already

instructions = input_parse()

for instruction in instructions:
	if instruction["instruction"] == "jmp":
		instruction["instruction"] = "nop"
	elif instruction["instruction"] == "nop":
		instruction["instruction"] = "jmp"
	else:
		continue
	
	hgc = HandheldGameConsole(instructions)
	hgc.execute(
		every_loop = mark_already,
		break_if = lambda c: c.next_instruction == len(c.instructions) or c.instructions[c.next_instruction]["already"]
	)
	if hgc.next_instruction == len(hgc.instructions):
		print(hgc.acc)
		break

	if instruction["instruction"] == "jmp":
		instruction["instruction"] = "nop"
	elif instruction["instruction"] == "nop":
		instruction["instruction"] = "jmp"
	
	for instruction in instructions:
		instruction["already"] = False