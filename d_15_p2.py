from d_15_parse import input_parse

numbers = input_parse()
last_said = {numbers[i]: i for i in range(len(numbers))}
next_number = 0

for i in range(len(numbers), 30000000):
	if not next_number in last_said:
		last_said[next_number] = i
	last_number = next_number
	next_number = i - last_said[last_number]
	last_said[last_number] = i
print(last_number)
