import re

def input_parse(filename="d_02_input.txt"):
	raw = open(filename, "r").readlines()
	return list(map(
		lambda a: re.match(r"^(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)$", a).groupdict(),
		raw
	))

if __name__ == "__main__":
	print(input_parse())