def input_parse(filename="d6_input.txt"):
	return list(map(lambda group: group.split("\n"), open(filename, "r").read().split("\n\n")))

if __name__ == "__main__":
	print(input_parse())