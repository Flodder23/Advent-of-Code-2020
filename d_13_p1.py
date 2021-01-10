from d_13_parse import input_parse

earliest, ids = input_parse()#"d_13_input_example.txt")
min_wait, min_bus = None, None

for i in ids:
	if i != "x":
		if min_wait is None or i - earliest % i < min_wait:
			min_wait, min_bus = i - earliest % i, i
print(min_wait * min_bus)