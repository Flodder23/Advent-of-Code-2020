import re

def input_parse():
	raw = open("d2_input.txt", "r").readlines()
	return list(map(
		lambda a: re.match("^(?P<a>\d+)-(?P<b>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)$", a).groupdict(),
		raw
	))

if __name__ == "__main__":
	print(input_parse())