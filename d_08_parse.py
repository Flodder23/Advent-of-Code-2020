import re

def input_parse(filename="d_08_input.txt"):
	raw = open(filename, "r").read().split("\n")
	instructions = list(map(lambda line: re.fullmatch(r"(?P<instruction>\w+) (?P<value>(\+|-)\d+)", line).groupdict(), raw))
	for instruction in instructions:
		instruction["value"] = int(instruction["value"])
		instruction["already"] = False
	return instructions

if __name__ == "__main__":
	print(input_parse())