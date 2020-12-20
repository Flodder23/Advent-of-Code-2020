def input_parse(filename="d3_input.txt"):
	raw = list(map(lambda x: x.strip("\n"), open(filename, "r").readlines()))
	return list(map(lambda x: "".join(x), raw))

if __name__ == "__main__":
	print(input_parse())