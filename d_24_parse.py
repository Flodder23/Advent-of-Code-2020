import re

def input_parse(filename="d_24_input.txt"):
	raw = open(filename, "r").read().split("\n")
	return list(map(
		lambda line: re.findall(r"e|se|sw|w|nw|ne", line),
		raw
	))
	

if __name__ == "__main__":
	print(input_parse())