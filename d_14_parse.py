import re

def input_parse(filename="d_14_input.txt"):
	raw = open(filename, "r").read().split("\n")
	return list(map(lambda line: re.match(
		r"(?P<instruction>mask|mem)(\[(?P<address>\d+)\])? = (?P<value>(\d|X)+)",
		line).groupdict(), raw))

if __name__ == "__main__":
	print(input_parse())