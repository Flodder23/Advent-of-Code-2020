def input_parse(filename="d_13_input.txt"):
	raw = open(filename, "r").read().split("\n")
	return [int(raw[0]), list(map(lambda x: x if x == "x" else int(x), raw[1].split(",")))]

if __name__ == "__main__":
	print(input_parse())