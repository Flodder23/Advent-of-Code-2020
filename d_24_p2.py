from d_24_parse import input_parse
from d_24_p1 import ref2coords, set_black_tiles

black_tiles = set_black_tiles(input_parse())

rel_adjacent = tuple(map(ref2coords, (["e"], ["se"], ["sw"], ["w"], ["nw"], ["ne"])))

for _ in range(100):
	adjacent_black = {}
	for tile in black_tiles:
		for rel in rel_adjacent:
			adjacent_tile = (tile[0] + rel[0], tile[1] + rel[1])
			if adjacent_tile in adjacent_black:
				adjacent_black[adjacent_tile] += 1
			else:
				adjacent_black[adjacent_tile] = 1
	
	new_black = set()
	for tile in adjacent_black:
		if (
			adjacent_black[tile] == 2
			) or (
			tile in black_tiles and adjacent_black[tile] == 1
			):
			new_black.add(tile)
	black_tiles = new_black

print(len(black_tiles))