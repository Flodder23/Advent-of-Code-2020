def input_parse(filename="d_05_input.txt"):
	raw = list(map(lambda line: line.strip(), open(filename, "r").readlines()))
	return list(map(lambda seat: {"row": seat[0:7], "col": seat[7:len(seat)]}, raw))

if __name__ == "__main__":
	print(input_parse())