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
		a = change_base(a, 10, 2, 36)
		a = "".join([a[j] if mask[j] == "0" else mask[j] for j in range(36)])
		adds = [""]
		for j in range(len(a)):
			if a[-1-j] == "X":
				adds = ["0" + add for add in adds] + ["1" + add for add in adds]
			else:
				adds = [a[-1-j] + add for add in adds]
		for add in adds:
			memory[add] = int(v)

print(sum(memory.values()))