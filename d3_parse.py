def input_parse(filename="d3_input.txt"):
	raw = list(map(list, open(filename, "r").readlines()))
	for line in raw:
		line.pop(-1)
	return list(map(lambda x: "".join(x), raw))

if __name__ == "__main__":
	print(input_parse())