from d_18_parse import input_parse

def evaluate(expression):
	total = expression[0] if type(expression[0]) is int else evaluate(expression[0])
	for e in expression[1:]:
		if e in ("+", "*"):
			next_op = e
			continue
		if type(e) is int:
			v = e
		else:
			v = evaluate(e)
		if next_op == "+":
			total += v
		else:
			total *= v
	return total

if __name__ == "__main__":
	print(sum([evaluate(expression) for expression in input_parse()]))