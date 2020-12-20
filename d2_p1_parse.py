import re

def input_parse(filename="d2_p1_input.txt"):
	raw = open(filename, "r").readlines()
	return list(map(
		lambda a: re.match("^(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)$", a).groupdict(),
		raw
	))

if __name__ == "__main__":
	print(input_parse())