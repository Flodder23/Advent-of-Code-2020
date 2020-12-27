def input_parse(filename="d_11_input.txt"):
	raw = open(filename, "r").read().split("\n")
	return list(map(list, raw))

if __name__ == "__main__":
	print(input_parse())