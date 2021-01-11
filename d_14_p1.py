from d_14_parse import input_parse
from functions import change_base

instructions = input_parse()
mask = instructions.pop(0)["value"]
memory = {}

for instruction in instructions:
	i, a, v = (instruction[k] for k in ("instruction", "address", "value"))
	if i == "mask":
		mask = v
	elif i == "mem":
		v = change_base(v, 10, 2, 36)
		memory[a] = "".join([v[j] if mask[j] == "X" else mask[j] for j in range(36)])

print(sum(map(lambda x: int(change_base(x, 2 ,10)), memory.values())))