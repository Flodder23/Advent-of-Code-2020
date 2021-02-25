from d_24_parse import input_parse

# Approximate grid by coordinates (x, y) where:
# 	x is how far right (or left if neg.) from origin
# 	y is how far ne (or sw if neg.) to go
# This representation should be unique for each hexagon

def ref2coords(ref):
	coords = [0, 0]
	for d in ref:
		if d == "e":
			coords[0] += 1
		elif d == "se":
			coords[0] += 1
			coords[1] -= 1
		elif d == "sw":
			coords[1] -= 1
		elif d == "w":
			coords[0] -= 1
		elif d == "nw":
			coords[0] -= 1
			coords[1] += 1
		elif d == "ne":
			coords[1] += 1
	return coords

references = input_parse()
black_tiles = set()

for ref in references:
	coords = tuple(ref2coords(ref))
	if coords in black_tiles:
		black_tiles.remove(coords)
	else:
		black_tiles.add(coords)

print(len(black_tiles))
