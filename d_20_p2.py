from d_20_parse import input_parse
from math import prod

def get_sides(tile):
	return [
		[row[-1] for row in tile],
		tile[-1],
		[row[0] for row in tile],
		tile[0]
	]

def crop(tile):
	return [row[1:-1] for row in tile[1:-1]]

def rotate(tile, rot, flip):
	for _ in range(rot):
		tile = [[tile[-1-i][j] for i in range(len(tile))] for j in range(len(tile[0]))]
	return tile[::-1] if flip else tile

def get_side_matched(matches, id0, id1):
	for s in matches[id0]:
		if matches[id0][s]["id"] == id1:
			return s

def same_side(s0, s1):
	return all([s0[p] == s1[p] for p in range(len(s0))])

def common_side(t0, t1):
	s0s, s1s = get_sides(t0), get_sides(t1)
	for i in range(4):
		for j in range(4):
			for f in (True, False):
				if same_side(s0s[i], s1s[j][::-1] if f else s1s[j]):
					return i, j, f
	return None, None, None


tiles = input_parse("d_20_input_example.txt")
ids = list(tiles.keys())
matches = {i: {} for i in ids}

for i in range(len(ids) - 1):
	id0 = ids[i]
	for j in range(i + 1, len(ids)):
		id1 = ids[j]
		s0, s1, flip = common_side(tiles[id0], tiles[id1])
		if not s0 is None:
			matches[id0][s0] = {
				"id": id1,
				"side": s1,
				"flip": flip
			}
			matches[id1][s1] = {
				"id": id0,
				"side": s0,
				"flip": flip
			}
#tiles = {key: crop(tile) for key, tile in tiles.items()}

#get first corner piece
for prev_id in ids:
	if len(matches[prev_id]) == 2:
		break
for side in range(4):
	if side in matches[prev_id] and (side+1)%4 in matches[prev_id]:
		next_id = matches[prev_id][side]["id"]
		break

image = [[prev_id]]
print(prev_id)
tiles[prev_id] = rotate(tiles[prev_id], (-side) % 4, False)
flipped = False

while True:
	while True:
		print(next_id)
		image[-1].append(next_id)
		left_side = get_side_matched(matches, next_id, prev_id)
		right_side = (left_side + 2) % 4
		flipped = flipped != matches[next_id][left_side]["flip"]
		tiles[next_id] = rotate(tiles[next_id], left_side, flipped)
		prev_id = next_id
		if not right_side in matches[prev_id]:
			break
		next_id = matches[prev_id][right_side]["id"]
	above_id = image[-1][0]
	right_side = get_side_matched(matches, above_id, image[-1][1])
	down_side = (right_side + 1) % 4
	if matches[above_id][right_side]["flip"]:
		down_side = (down_side + 2) % 4
	if not down_side in matches[above_id]:
		break
	prev_id = matches[above_id][down_side]["id"]
	image.append([prev_id])
	up_side = matches[above_id][down_side]["side"]
	if matches[above_id][down_side]["flip"]:
		up_side = (up_side + 2) % 4
	tiles[prev_id] = rotate(tiles[prev_id], (up_side - 1) % 4, matches[above_id][down_side]["flip"])
	next_id = matches[prev_id][(up_side + 1) % 4]["id"]
	

for tile_row in image:
	print()
	for tile_id in tile_row:
		print()
		print(tile_id)
		for row in tiles[tile_id]:
			print("".join(row))