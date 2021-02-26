def input_parse(filename="d_25_input.txt"):
	return list(map(int, open(filename, "r").read().split("\n")))
	

if __name__ == "__main__":
	print(input_parse())