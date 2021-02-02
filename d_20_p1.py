from d_20_parse import input_parse
from math import prod

def get_sides(tile):
	return [
		tile[0],
		[row[-1] for row in tile],
		tile[-1],
		[row[0] for row in tile]
	]

def same_sides(s0, s1):
	return all(s0[p] == s1[p] for p in range(len(s0))) or all(s0[-1-p] == s1[p] for p in range(len(s0)))

def common_side(t0, t1):
	s0s, s1s = get_sides(t0), get_sides(t1)
	return any([any([same_sides(s0, s1) for s1 in s1s]) for s0 in s0s])


tiles = input_parse()
ids = list(tiles.keys())
matches = {i: 0 for i in ids}

for i in range(len(ids) - 1):
	id0 = ids[i]
	for j in range(i + 1, len(ids)):
		id1 = ids[j]
		if common_side(tiles[id0], tiles[id1]):
			matches[id0] += 1
			matches[id1] += 1

#corner pieces will have exactly two matches
print(prod([int(i) for i in ids if matches[i] == 2]))