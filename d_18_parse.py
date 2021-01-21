from functions import binary_insert

def expression_to_list(expression):
	e_list = []
	i = 0
	while i < len(expression):
		if expression[i] == "(":
			b = 1
			d = 0
			while b > 0:
				d += 1
				if expression[i+d] == "(":
					b += 1
				elif expression[i+d] == ")":
					b -= 1
			e_list.append(expression_to_list(expression[i+1:i+d]))
			i += d
		elif expression[i] in ("+", "*"):
			e_list.append(expression[i])
		else:
			e_list.append(int(expression[i]))
		i += 1
	return e_list

def input_parse(filename="d_18_input.txt"):
	raw = open(filename, "r").read().split("\n")
	raw = list(map(lambda line: line.replace(" ", ""), raw))
	return list(map(expression_to_list, raw))

if __name__ == "__main__":
	print(input_parse())