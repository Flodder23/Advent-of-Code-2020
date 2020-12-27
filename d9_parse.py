def input_parse(filename="d9_input.txt"):
	raw = open(filename, "r").readlines()
	return list(map(int, raw))

if __name__ == "__main__":
	print(input_parse())