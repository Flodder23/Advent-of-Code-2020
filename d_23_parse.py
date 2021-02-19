def input_parse(filename="d_23_input.txt"):
	return list(map(int, open(filename, "r").read()))
	

if __name__ == "__main__":
	print(input_parse())