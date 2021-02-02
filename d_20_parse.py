import re

def input_parse(filename="d_20_input.txt"):
	raw = open(filename, "r").read().split("\n\n")
	tiles = {}
	for tile in raw:
		tile = tile.split("\n")
		n = re.match(r"Tile (?P<n>\d+):", tile.pop(0)).groupdict()["n"]
		tiles[n] = [list(line) for line in tile]
	return tiles

if __name__ == "__main__":
	print(input_parse())