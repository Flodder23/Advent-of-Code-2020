def input_parse(filename="d_15_input.txt"):
	return list(map(int, open(filename, "r").read().split(",")))

if __name__ == "__main__":
	print(input_parse())
	